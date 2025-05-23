# NTP servers with NTS support

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/jauderho/nts-servers)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/jauderho/nts-servers/badge)](https://securityscorecards.dev/viewer/?uri=github.com/jauderho/nts-servers) 

WARNING: There is no endorsement of any server included in this list. Please carefully vet before usage.

This is intended to bootstrap a list of NTP servers with NTS support given that NTS support is not currently widespread.

## Contribute
- Pull requests are welcome to add new sources ([signed commits](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits) are preferred)
- PR will not be merged until connectivity to server can be verified
- Please specify if server is virtualized
- You can now update `nts-sources.yml` to modify the `README.md`, `chrony.conf`, and `ntp.toml`
  - Run `./scripts/ntpServerConverter.py nts-sources.yml`
  - Use `git diff origin README.md chrony.conf ntp.toml` to verify that you have a clean update before submitting a PR
- AI generated documentation: https://deepwiki.com/jauderho/nts-servers

## Usage
- This repository provides NTS server lists in multiple formats:
  - For use with chrony - [chrony.conf](chrony.conf)
  - For use with ntpd-rs - [ntp.toml](ntp.toml)
- Before using anycast NTP servers, make sure that you understand the [limitations](https://www.rfc-editor.org/rfc/rfc8633.html#page-17)
- Use [at least 4 time sources](https://support.ntp.org/Support/SelectingOffsiteNTPServers#Upstream_Time_Server_Quantity) as a best practice. No more than 10 should be used
- It is not possible to mix and match NTP and NTS at this time. Only NTS servers should be specified as the NTP entries will not be used
- Generally, virtualized systems do not make for good time sources as there is too much jitter. Submissions should strive to ensure that high quality time is available
- Verify NTS server connectivity using the following command before submitting a pull request
  - `./scripts/ntsCheck.sh <NTS_SERVER_NAME>` 

## The List
|Hostname|Stratum|Location|Owner|Notes|
|---|:---:|---|---|---|
|[time.cloudflare.com](https://time.cloudflare.com)|3|All|Cloudflare|Anycast|
||
|1.ntp.ubuntu.com|2|Distro|Ubuntu|Distro use only|
|2.ntp.ubuntu.com|2|Distro|Ubuntu|Distro use only|
|3.ntp.ubuntu.com|2|Distro|Ubuntu|Distro use only|
|4.ntp.ubuntu.com|2|Distro|Ubuntu|Distro use only|
||
|[nts.teambelgium.net](https://ntp.teambelgium.net)|1|Belgium|Team Belgium||
||
|a.st1.ntp.br|1|Brazil|[ntp.br](https://ntp.br)||
|b.st1.ntp.br|1|Brazil|[ntp.br](https://ntp.br)||
|c.st1.ntp.br|1|Brazil|[ntp.br](https://ntp.br)||
|d.st1.ntp.br|1|Brazil|[ntp.br](https://ntp.br)||
|gps.ntp.br|1|Brazil|[ntp.br](https://ntp.br)||
|brazil.time.system76.com|2|Brazil|System76||
|[time.bolha.one](https://time.bolha.one)|1|Brazil|Cadu Silva||
||
|[time.web-clock.ca](https://time.web-clock.ca)|1|Canada|Community||
||
|[ntp.miuku.net](https://ntp.miuku.net)|3|Finland|miuku.net||
||
|paris.time.system76.com|2|France|System76||
||
|ntp3.fau.de|1|Germany|FAU||
|ntp3.ipv6.fau.de|1|Germany|FAU|IPv6 only|
|ptbtime1.ptb.de|1|Germany|PTB||
|ptbtime2.ptb.de|1|Germany|PTB||
|ptbtime3.ptb.de|1|Germany|PTB||
|ptbtime4.ptb.de|1|Germany|PTB||
|www.jabber-germany.de|2|Germany|Jörg Morbitzer||
|www.masters-of-cloud.de|2|Germany|Jörg Morbitzer||
|ntp.nanosrvr.cloud|1|Germany|Michael Byczkowski|IPv4 and IPv6|
||
|ntppool1.time.nl|1|Netherlands|TimeNL||
|ntppool2.time.nl|1|Netherlands|TimeNL||
||
|ntpmon.dcs1.biz|1|Singapore|Sanjeev Gupta||
||
|[nts.netnod.se](https://nts.netnod.se)|1|Sweden|Netnod|Anycast|
|gbg1.nts.netnod.se|1|Sweden|Netnod|For users near Göteborg|
|gbg2.nts.netnod.se|1|Sweden|Netnod|For users near Göteborg|
|lul1.nts.netnod.se|1|Sweden|Netnod|For users near Luleå|
|lul2.nts.netnod.se|1|Sweden|Netnod|For users near Luleå|
|mmo1.nts.netnod.se|1|Sweden|Netnod|For users near Malmö|
|mmo2.nts.netnod.se|1|Sweden|Netnod|For users near Malmö|
|sth1.nts.netnod.se|1|Sweden|Netnod|For users near Stockholm|
|sth2.nts.netnod.se|1|Sweden|Netnod|For users near Stockholm|
|svl1.nts.netnod.se|1|Sweden|Netnod|For users near Sundsvall|
|svl2.nts.netnod.se|1|Sweden|Netnod|For users near Sundsvall|
||
|[ntp.3eck.net](https://ntp.3eck.net)|2|Switzerland|Adrian Zaugg||
|[ntp.trifence.ch](https://ntp.trifence.ch)|2|Switzerland|Marcel Waldvogel||
|[ntp.zeitgitter.net](https://ntp.zeitgitter.net)|2|Switzerland|Marcel Waldvogel||
|[ntp01.maillink.ch](https://ntp01.maillink.ch)|2|Switzerland|Ueli Heuer||
|[ntp02.maillink.ch](https://ntp02.maillink.ch)|2|Switzerland|Ueli Heuer||
|[ntp03.maillink.ch](https://ntp03.maillink.ch)|2|Switzerland|Ueli Heuer||
|time.signorini.ch|1|Switzerland|Attilio Signorini||
||
|ntp2.glypnod.com|2|UK|Hal Murray|London|
|ntp1.dmz.terryburton.co.uk|1|UK|Terry Burton|IPv4 and IPv6|
|ntp2.dmz.terryburton.co.uk|1|UK|Terry Burton|IPv4 and IPv6|
||
|ntp1.glypnod.com|2|US|Hal Murray|San Francisco|
|ohio.time.system76.com|2|US|System76||
|oregon.time.system76.com|2|US|System76||
|virginia.time.system76.com|2|US|System76||
|[stratum1.time.cifelli.xyz](https://stratum1.time.cifelli.xyz)|1|US|Mike Cifelli||
|[time.cifelli.xyz](https://time.cifelli.xyz)|2|US|Mike Cifelli||
|[time.txryan.com](https://time.txryan.com)|2|US|Tanner Ryan||

The following servers are known to be virtualized and may be less accurate. YMMV.

|Hostname|Stratum|Location|Owner|Notes|
|---|:---:|---|---|---|
|[ntp.viarouge.net](http://ntp.viarouge.net)|2|France|Hubert Viarouge||
|time.xargs.org|2|US|Michael Driscoll|IPv4 and IPv6|

## Star History
<a href="https://star-history.com/#jauderho/nts-servers&Timeline">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=jauderho/nts-servers&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=jauderho/nts-servers&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=jauderho/nts-servers&type=Date" />
  </picture>
</a>
