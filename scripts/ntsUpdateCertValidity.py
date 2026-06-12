#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "PyYAML",
# ]
# ///
"""
ntsUpdateCertValidity.py - Update certificate validity values in nts-sources.yml file

This script reads an nts-sources.yml file, queries each hostname to get the current
certificate validity using openssl, and updates the file with the values.
"""

import argparse
import logging
import re
import subprocess
import sys
from datetime import datetime
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


def get_cert_validity(hostname, logger):
    """
    Get certificate validity for a hostname using openssl
    Returns the validity as string or None if not found
    """
    try:
        # Step 1: Get raw certificates
        cmd_s_client = [
            'openssl', 's_client',
            '-connect', f'{hostname}:4460',
            '-showcerts',
            '-servername', hostname
        ]
        s_client_proc = subprocess.Popen(
            cmd_s_client,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True
        )

        # Step 2: Extract dates from certificate
        cmd_x509 = ['openssl', 'x509', '-noout', '-dates']
        x509_proc = subprocess.run(
            cmd_x509,
            input=s_client_proc.communicate(timeout=10)[0],
            capture_output=True,
            text=True,
            timeout=5
        )

        if x509_proc.returncode == 0:
            dates = {}
            for line in x509_proc.stdout.split('\n'):
                if '=' in line:
                    key, value = line.split('=', 1)
                    dates[key] = value.strip()

            if 'notBefore' in dates and 'notAfter' in dates:
                # Format: Feb 17 21:30:57 2026 GMT
                fmt = "%b %d %H:%M:%S %Y %Z"
                try:
                    start = datetime.strptime(dates['notBefore'], fmt)
                    end = datetime.strptime(dates['notAfter'], fmt)
                except ValueError:
                    # Try without %Z just in case
                    fmt_no_tz = "%b %d %H:%M:%S %Y"
                    # Strip GMT/UTC from end
                    start_str = ' '.join(dates['notBefore'].split()[:-1])
                    end_str = ' '.join(dates['notAfter'].split()[:-1])
                    start = datetime.strptime(start_str, fmt_no_tz)
                    end = datetime.strptime(end_str, fmt_no_tz)

                delta = end - start
                days = delta.days

                if days >= 365:
                    years = round(days / 365.25, 1)
                    if years == 1.0:
                        return "1 year"
                    if years == int(years):
                        return f"{int(years)} years"
                    return f"{years} years"
                elif days >= 30:
                    months = round(days / 30.44, 1)
                    if months == 1.0:
                        return "1 month"
                    if months == int(months):
                        return f"{int(months)} months"
                    return f"{months} months"

                if days == 1:
                    return "1 day"
                return f"{days} days"

        logger.warning(f"Could not determine certificate validity for {hostname}")
        return None

    except Exception as e:
        logger.error(f"Error getting certificate validity for {hostname}: {e}")
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
        # Dump with allow_unicode=True to preserve non-ASCII characters
        yaml_content = yaml.dump(
            data,
            default_flow_style=False,
            sort_keys=False,
            indent=2,
            allow_unicode=True
        )

        # Post-process to add blank lines between server entries
        lines = yaml_content.split('\n')
        formatted_lines = []

        for i, line in enumerate(lines):
            formatted_lines.append(line)
            # Add blank line after entry if the next line starts with "- hostname:"
            if i + 1 < len(lines) and lines[i + 1].strip().startswith('- hostname:'):
                formatted_lines.append('')

        # Write the formatted content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(formatted_lines))

        return True
    except Exception as e:
        logger.error(f"Error saving YAML file {filepath}: {e}")
        return False


def update_cert_values(data, logger, dry_run=False):
    """
    Update certificate validity values for all servers in the data
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

        current_validity = server.get('certificate_validity', 'unknown')
        logger.info(f"Server {i}/{total_servers}: Checking {hostname} (current validity: {current_validity})")

        # Get actual validity
        actual_validity = get_cert_validity(hostname, logger)

        if actual_validity is None:
            logger.warning(f"Server {i}: Could not determine certificate validity for {hostname}")
            continue

        # Compare and update if different
        if current_validity != actual_validity:
            if dry_run:
                logger.info(f"Server {i}: [DRY RUN] Would update {hostname}: {current_validity} -> {actual_validity}")
            else:
                logger.info(f"Server {i}: Updating {hostname}: {current_validity} -> {actual_validity}")
                server['certificate_validity'] = actual_validity
            changes_made = True
        else:
            logger.info(f"Server {i}: {hostname} certificate validity is correct ({actual_validity})")

    return data, changes_made, total_servers


def main():
    parser = argparse.ArgumentParser(
        description="Update certificate validity values in nts-sources.yml file"
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

    # Update certificate validity values
    updated_data, changes_made, total_servers = update_cert_values(data, logger, args.dry_run)

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
        logger.info("No changes needed - all certificate validity values are correct")

    logger.info(f"Processed {total_servers} servers")


if __name__ == '__main__':
    main()
