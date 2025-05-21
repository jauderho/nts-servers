#!/usr/bin/python3

import yaml
import argparse
import re
import os


def load_yaml(file_path):
    with open(file_path, "r") as file:
        return yaml.safe_load(file)


def extract_hostname(hostname_field):
    match = re.search(r"\[([^\]]+)\]", hostname_field)
    if match:
        return match.group(1)
    return hostname_field


def generate_markdown(data):
    markdown = "## The List\n"
    markdown += "|Hostname|Stratum|Location|Owner|Notes|\n|---|:---:|---|---|---|\n"
    current_location = None
    vm_servers = []

    for server in data["servers"]:
        if server["vm"]:
            vm_servers.append(server)
            continue
        if server["location"] != current_location:
            if current_location is not None:
                markdown += "||\n"
            current_location = server["location"]

        hostname = server["hostname"]
        stratum = server["stratum"]
        location = server["location"]
        owner = server["owner"]
        notes = server.get("notes", "")

        markdown += f"|{hostname}|{stratum}|{location}|{owner}|{notes}|\n"

    if vm_servers:
        markdown += "\nThe following servers are known to be virtualized and may be less accurate. YMMV.\n\n"
        markdown += "|Hostname|Stratum|Location|Owner|Notes|\n|---|:---:|---|---|---|\n"
        for server in vm_servers:
            hostname = server["hostname"]
            stratum = server["stratum"]
            location = server["location"]
            owner = server["owner"]
            notes = server.get("notes", "")

            markdown += f"|{hostname}|{stratum}|{location}|{owner}|{notes}|\n"

    return markdown


def generate_chrony_conf(data):
    chrony_conf = "#\n# NTS servers in chrony format\n#\n\n"
    current_location = None
    vm_servers = []

    for server in data["servers"]:
        if server["vm"]:
            vm_servers.append(server)
            continue
        if server["location"] != current_location:
            if current_location is not None:
                chrony_conf += "\n"
            chrony_conf += f"# {server['location']}\n"
            current_location = server["location"]

        hostname = extract_hostname(server["hostname"])
        chrony_conf += f"server {hostname} nts iburst\n"

    if vm_servers:
        chrony_conf += "\n# Known VM servers (may be less accurate)\n"
        for server in vm_servers:
            hostname = extract_hostname(server["hostname"])
            chrony_conf += f"server {hostname} nts iburst\n"

    return chrony_conf


def generate_ntp_toml(data):
    ntp_toml = "#\n# NTS servers in ntpd-rs format\n#\n\n"
    current_location = None
    vm_servers = []

    for server in data["servers"]:
        if server["vm"]:
            vm_servers.append(server)
            continue

        if server["location"] != current_location:
            if current_location is not None:
                ntp_toml += "\n"
            ntp_toml += f"# {server['location']}\n"
            current_location = server["location"]

        hostname = extract_hostname(server["hostname"])
        ntp_toml += f'[[source]]\nmode = "nts"\naddress = "{hostname}"\n\n'

    if vm_servers:
        ntp_toml += "\n# Known VM servers (may be less accurate)\n"
        for server in vm_servers:
            hostname = extract_hostname(server["hostname"])
            ntp_toml += (
                f'[[source]]\nmode = "nts"\naddress = "{hostname}"\n\n'
            )

    return ntp_toml


def update_readme(readme_path, new_content):
    with open(readme_path, "r") as file:
        content = file.read()

    start = content.index("## The List")
    end = content.index("## Star History", start)

    # Keep the original content before "## The List" and after "## Star History"
    updated_content = content[:start] + new_content + "\n" + content[end:]

    with open(readme_path, "w") as file:
        file.write(updated_content)


def main():
    parser = argparse.ArgumentParser(
        description="Convert NTP server data to Markdown, chrony.conf, or ntp.toml format"
    )
    parser.add_argument("input_file", help="Path to the input YAML file")
    parser.add_argument(
        "output_format",
        nargs="?",
        choices=["markdown", "chrony", "toml"],
        help="Output format (markdown, chrony, or toml)",
    )
    parser.add_argument("output_file", nargs="?", help="Path to the output file")

    args = parser.parse_args()

    data = load_yaml(args.input_file)

    if args.output_format is None:
        # Behavior 1: Update README.md, write new chrony.conf and ntp.toml if they exist
        readme_path = "README.md"
        chrony_path = "chrony.conf"
        toml_path = "ntp.toml"

        if os.path.exists(readme_path):
            markdown_content = generate_markdown(data)
            update_readme(readme_path, markdown_content)
            print(f"Updated {readme_path}")

        chrony_content = generate_chrony_conf(data)
        with open(chrony_path, "w") as file:
            file.write(chrony_content)
        print(f"Written {chrony_path}")

        toml_content = generate_ntp_toml(data)
        with open(toml_path, "w") as file:
            file.write(toml_content)
        print(f"Written {toml_path}")

    elif args.output_format == "markdown":
        # Behavior 2: Write markdown to specified file
        if args.output_file is None:
            parser.error("output_file is required when output_format is specified")

        markdown_content = generate_markdown(data)
        with open(args.output_file, "w") as file:
            file.write(markdown_content)
        print(f"Markdown written to {args.output_file}")

    elif args.output_format == "chrony":
        # Behavior 3: Write chrony format to specified file
        if args.output_file is None:
            parser.error("output_file is required when output_format is specified")

        chrony_content = generate_chrony_conf(data)
        with open(args.output_file, "w") as file:
            file.write(chrony_content)
        print(f"Chrony configuration written to {args.output_file}")

    elif args.output_format == "toml":
        # Behavior 4: Write toml format to specified file
        if args.output_file is None:
            parser.error("output_file is required when output_format is specified")

        toml_content = generate_ntp_toml(data)
        with open(args.output_file, "w") as file:
            file.write(toml_content)
        print(f"TOML configuration written to {args.output_file}")


if __name__ == "__main__":
    main()
