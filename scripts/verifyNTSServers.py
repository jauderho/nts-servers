#!/usr/bin/python3
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "yaml",
# ]
# ///

import yaml
import argparse
import subprocess
import re


def load_yaml(file_path):
    with open(file_path, "r") as file:
        return yaml.safe_load(file)


def extract_hostname(hostname_field):
    # Extract hostname from potential markdown link
    match = re.search(r"\[([^\]]+)\]", hostname_field)
    if match:
        return match.group(1)
    return hostname_field


HOSTNAME_RE = re.compile(r"^(?=.{1,253}$)[A-Za-z0-9]([A-Za-z0-9.-]*[A-Za-z0-9])?$")


def verify_ntp_server(hostname):
    # Hostnames come from untrusted PRs: validate, and never use a shell
    if not HOSTNAME_RE.match(hostname):
        print(f"Skipping invalid hostname: {hostname!r}\n")
        return
    print(f"Verifying {hostname} ...", end="", flush=True)
    command = [
        "chronyd",
        "-Q",
        "-t",
        "5",
        f"server {hostname} iburst nts maxsamples 1",
    ]
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print(" Good")
        print(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        print(" Failed")
        print(f"Error verifying {hostname}: {e}")
        print(e.output.strip())
    print()  # Add a newline for better readability


def main():
    parser = argparse.ArgumentParser(description="Verify NTP server connectivity")
    parser.add_argument("yaml_file", help="Path to the input YAML file")
    parser.add_argument("--hostname", help="Specific hostname to verify (optional)")

    args = parser.parse_args()

    data = load_yaml(args.yaml_file)

    if args.hostname:
        verify_ntp_server(args.hostname)
    else:
        hostnames = [extract_hostname(server["hostname"]) for server in data["servers"]]
        for hostname in hostnames:
            verify_ntp_server(hostname)


if __name__ == "__main__":
    main()
