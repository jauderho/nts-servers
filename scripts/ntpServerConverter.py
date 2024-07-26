import yaml
import argparse

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def generate_markdown(data):
    markdown = "|Hostname|Stratum|Location|Owner|Notes|\n|---|:---:|---|---|---|\n"
    current_location = None
    for server in data['servers']:
        if server['location'] != current_location:
            if current_location is not None:
                markdown += "|||\n"
            current_location = server['location']
        
        hostname = server['hostname']
        stratum = server['stratum']
        location = server['location']
        owner = server['owner']
        notes = server.get('notes', '')
        
        markdown += f"|{hostname}|{stratum}|{location}|{owner}|{notes}|\n"
    
    return markdown

def generate_chrony_conf(data):
    chrony_conf = "#\n# NTS servers in chrony format\n#\n"
    current_location = None
    for server in data['servers']:
        if server['location'] != current_location:
            if current_location is not None:
                chrony_conf += "\n"
            chrony_conf += f"# {server['location']}\n"
            current_location = server['location']
        
        hostname = server['hostname']
        chrony_conf += f"server {hostname} nts iburst\n"
    
    return chrony_conf

def main():
    parser = argparse.ArgumentParser(description="Convert NTP server data to Markdown or chrony.conf format")
    parser.add_argument("input_file", help="Path to the input YAML file")
    parser.add_argument("output_format", choices=["markdown", "chrony"], help="Output format (markdown or chrony)")
    parser.add_argument("output_file", help="Path to the output file")
    
    args = parser.parse_args()
    
    data = load_yaml(args.input_file)
    
    if args.output_format == "markdown":
        output = generate_markdown(data)
    else:
        output = generate_chrony_conf(data)
    
    with open(args.output_file, 'w') as file:
        file.write(output)
    
    print(f"Output written to {args.output_file}")

if __name__ == "__main__":
    main()
