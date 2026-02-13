# AGENTS.md

- Scan the URL provided or GitHub Issue for any relevant information
- Extract hostname and verify that the NTS server is reachable via NTS and NTP
- Place new entry in the proper location in nts-sources.yml by alphabetical country
- Do not make direct changes to README.md, chrony.conf and ntp.toml. Run scripts/ntpServerConvertor.py to update after changes to nts-sources.yml are completed
