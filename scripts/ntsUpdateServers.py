#!/usr/bin/env python3
"""
ntsUpdateSources.py - Update stratum values in nts-sources.yml file

This script reads an nts-sources.yml file, queries each hostname to get the current
stratum value using ntpdate, and updates the file with the correct stratum values.
"""

import argparse
import logging
import re
import subprocess
import sys
from pathlib import Path
import yaml


def setup_logging(verbose=False):
    """Setup logging configuration"""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(__name__)


def extract_hostname(hostname_field):
    """
    Extract hostname from various formats:
    - Plain text: "time.cloudflare.com"
    - Markdown link: "[time.cloudflare.com](https://time.cloudflare.com)"
    """
    if not hostname_field:
        return None
    
    # Check if it's a markdown link format [text](url)
    markdown_match = re.match(r'\[([^\]]+)\]', hostname_field)
    if markdown_match:
        return markdown_match.group(1)
    
    # Otherwise, assume it's plain text
    return hostname_field.strip()


def get_stratum(hostname, logger):
    """
    Get stratum for a hostname using ntpdate
    Returns the stratum as integer or None if not found
    """
    try:
        # Run: ntpdate -q hostname
        cmd = ['ntpdate', '-q', hostname]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            # Parse output to find stratum
            # Example output: "2025-05-23 02:57:29.980318 (+0000) +0.000214 +/- 0.003723 time.cloudflare.com 162.159.200.1 s3 no-leap"
            for line in result.stdout.split('\n'):
                line = line.strip()
                if line and hostname in line:
                    # Look for pattern like "s3" or "s1" etc.
                    stratum_match = re.search(r'\bs(\d+)\b', line)
                    if stratum_match:
                        return int(stratum_match.group(1))
        
        # If ntpdate fails, try alternative approach with timeout
        logger.warning(f"ntpdate failed for {hostname}, trying alternative method")
        
        # Alternative: use ntpq if available
        try:
            cmd_alt = ['timeout', '10', 'ntpq', '-p', hostname]
            result_alt = subprocess.run(cmd_alt, capture_output=True, text=True)
            if result_alt.returncode == 0:
                # Parse ntpq output for stratum
                for line in result_alt.stdout.split('\n'):
                    if hostname in line or '*' in line or '+' in line:
                        parts = line.split()
                        if len(parts) >= 3 and parts[2].isdigit():
                            return int(parts[2])
        except Exception:
            pass
        
        logger.warning(f"Could not determine stratum for {hostname}")
        return None
        
    except Exception as e:
        logger.error(f"Error getting stratum for {hostname}: {e}")
        return None


def load_yaml_file(filepath, logger):
    """Load and parse YAML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as e:
        logger.error(f"Error loading YAML file {filepath}: {e}")
        return None


def save_yaml_file(filepath, data, logger):
    """Save data to YAML file with custom formatting"""
    try:
        # First, dump to string with PyYAML
        yaml_content = yaml.dump(data, default_flow_style=False, sort_keys=False, indent=2)
        
        # Post-process to add blank lines between server entries and fix quoting
        lines = yaml_content.split('\n')
        formatted_lines = []
        
        for i, line in enumerate(lines):
            # Replace single quotes with double quotes for strings that need quoting
            if "'" in line and ':' in line:
                # Find the colon and replace quotes in the value part
                colon_index = line.find(':')
                if colon_index != -1:
                    key_part = line[:colon_index + 1]
                    value_part = line[colon_index + 1:]
                    value_part = value_part.replace("'", '"')
                    line = key_part + value_part
            
            formatted_lines.append(line)
            # Add blank line after "vm:" field if the next line starts with "- hostname:"
            if (line.strip().startswith('vm:') and 
                i + 1 < len(lines) and 
                lines[i + 1].strip().startswith('- hostname:')):
                formatted_lines.append('')
        
        # Write the formatted content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(formatted_lines))
        
        return True
    except Exception as e:
        logger.error(f"Error saving YAML file {filepath}: {e}")
        return False


def update_stratum_values(data, logger, dry_run=False):
    """
    Update stratum values for all servers in the data
    Returns tuple (updated_data, changes_made, total_servers)
    """
    if not data or 'servers' not in data:
        logger.error("Invalid YAML structure: missing 'servers' key")
        return data, False, 0
    
    changes_made = False
    total_servers = len(data['servers'])
    
    logger.info(f"Processing {total_servers} servers...")
    
    for i, server in enumerate(data['servers'], 1):
        if 'hostname' not in server:
            logger.warning(f"Server {i}: Missing hostname field")
            continue
        
        hostname_raw = server['hostname']
        hostname = extract_hostname(hostname_raw)
        
        if not hostname:
            logger.warning(f"Server {i}: Could not extract hostname from '{hostname_raw}'")
            continue
        
        current_stratum = server.get('stratum', 'unknown')
        logger.info(f"Server {i}/{total_servers}: Checking {hostname} (current stratum: {current_stratum})")
        
        # Get actual stratum
        actual_stratum = get_stratum(hostname, logger)
        
        if actual_stratum is None:
            logger.warning(f"Server {i}: Could not determine stratum for {hostname}")
            continue
        
        # Compare and update if different
        if current_stratum != actual_stratum:
            if dry_run:
                logger.info(f"Server {i}: [DRY RUN] Would update {hostname}: {current_stratum} -> {actual_stratum}")
            else:
                logger.info(f"Server {i}: Updating {hostname}: {current_stratum} -> {actual_stratum}")
                server['stratum'] = actual_stratum
            changes_made = True
        else:
            logger.info(f"Server {i}: {hostname} stratum is correct ({actual_stratum})")
    
    return data, changes_made, total_servers


def main():
    parser = argparse.ArgumentParser(
        description="Update stratum values in nts-sources.yml file"
    )
    parser.add_argument(
        'input_file',
        nargs='?',
        default='nts-sources.yml',
        help='Input YAML file (default: nts-sources.yml)'
    )
    parser.add_argument(
        '--output', '-o',
        help='Output file (default: overwrite input file)'
    )
    parser.add_argument(
        '--dry-run', '--dryrun',
        action='store_true',
        help='Show proposed changes without modifying the file'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose logging'
    )
    
    args = parser.parse_args()
    
    # Setup logging
    logger = setup_logging(args.verbose)
    
    # Check if input file exists
    input_path = Path(args.input_file)
    if not input_path.exists():
        logger.error(f"Input file not found: {input_path}")
        sys.exit(1)
    
    # Determine output file
    output_path = Path(args.output) if args.output else input_path
    
    logger.info(f"Input file: {input_path}")
    if args.dry_run:
        logger.info("DRY RUN MODE - No changes will be made")
    else:
        logger.info(f"Output file: {output_path}")
    
    # Load YAML data
    logger.info("Loading YAML file...")
    data = load_yaml_file(input_path, logger)
    if data is None:
        sys.exit(1)
    
    # Update stratum values
    updated_data, changes_made, total_servers = update_stratum_values(data, logger, args.dry_run)
    
    # Save results
    if changes_made and not args.dry_run:
        logger.info("Saving updated file...")
        if save_yaml_file(output_path, updated_data, logger):
            logger.info(f"Successfully updated {output_path}")
        else:
            logger.error("Failed to save updated file")
            sys.exit(1)
    elif changes_made and args.dry_run:
        logger.info("DRY RUN: Changes would be made to the file")
    else:
        logger.info("No changes needed - all stratum values are correct")
    
    logger.info(f"Processed {total_servers} servers")


if __name__ == '__main__':
    main()
