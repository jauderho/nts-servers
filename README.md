# NTP servers with NTS support

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/jauderho/nts-servers)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/jauderho/nts-servers/badge)](https://securityscorecards.dev/viewer/?uri=github.com/jauderho/nts-servers) 

**WARNING:** There is no endorsement of any server included in this list. Please carefully vet before usage.

This is intended to bootstrap a list of NTP servers with NTS support given that NTS support is not currently widespread. Visit the companion repo of [public NTP servers](https://github.com/jauderho/public-ntp-servers).

## Contribute
- Pull requests are welcome to add new sources ([signed commits](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits) are preferred)
- PR will not be merged until connectivity to server can be verified. Scripts are available in the `scripts/` subfolder to assist with this
- New entries should be grouped by location then in alphabetical order
- Please specify if server is virtualized
- Contributions and updates to the list are welcome via pull requests to [nts-sources.yml](https://github.com/jauderho/nts-servers/blob/main/nts-sources.yml) to modify the `README.md`, `chrony.conf`, and `ntp.toml`
  - Run `./scripts/ntsServerConverter.py nts-sources.yml` to update the other files after changing nts-sources.yml
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
|Hostname|Stratum|Location|Owner|Notes|Cert Validity|
|---|:---:|---|---|---|---|
|time.cloudflare.com|3|All|Cloudflare|Anycast|1 year|
||
|1.ntp.ubuntu.com|2|Distro|Ubuntu|Distro use only|2.9 months|
|ntp-bootstrap.ubuntu.com|2|Distro|Ubuntu|Self-signed certificate with long validity|130 years|
|2.ntp.ubuntu.com|2|Distro|Ubuntu|Distro use only|2.9 months|
|3.ntp.ubuntu.com|2|Distro|Ubuntu|Distro use only|2.9 months|
|4.ntp.ubuntu.com|2|Distro|Ubuntu|Distro use only|2.9 months|
||
|[nts.teambelgium.net](https://ntp.teambelgium.net)|1|Belgium|Team Belgium||2.9 months|
||
|a.st1.ntp.br|1|Brazil|[ntp.br](https://ntp.br)||2.9 months|
|b.st1.ntp.br|1|Brazil|[ntp.br](https://ntp.br)|||
|c.st1.ntp.br|1|Brazil|[ntp.br](https://ntp.br)||2.9 months|
|d.st1.ntp.br|2|Brazil|[ntp.br](https://ntp.br)||2.9 months|
|gps.ntp.br|1|Brazil|[ntp.br](https://ntp.br)||2.9 months|
|brazil.time.system76.com|2|Brazil|System76||2.9 months|
|time.bolha.one|2|Brazil|Cadu Silva||2.9 months|
||
|[time1.mbix.ca](https://time1.mbix.ca)|1|Canada|Manitoba Internet Exchange|IPv4 and IPv6|2.9 months|
|[time2.mbix.ca](https://time2.mbix.ca)|1|Canada|Manitoba Internet Exchange|IPv4 and IPv6|2.9 months|
|[time3.mbix.ca](https://time3.mbix.ca)|1|Canada|Manitoba Internet Exchange|IPv4 and IPv6|2.9 months|
|[time.web-clock.ca](https://time.web-clock.ca)|1|Canada|Community||2.9 months|
||
|[nts1.ntp.hr](http://www.ntp.hr)|1|Croatia|UNIZG FER REMLAB|[rem.fer.hr](https://rem.fer.hr)|6.5 months|
|[nts2.ntp.hr](http://www.ntp.hr)|1|Croatia|UNIZG FER REMLAB|[rem.fer.hr](https://rem.fer.hr)|6.5 months|
||
|[time.cincura.net](https://time.cincura.net)|1|Czech Republic|Jiří Činčura|IPv4 and IPv6|2.9 months|
||
|ntp.miuku.net|3|Finland|miuku.net||2.9 months|
||
|paris.time.system76.com|2|France|System76||2.9 months|
||
|ntp3.fau.de|1|Germany|FAU||2.9 months|
|ntp3.ipv6.fau.de|1|Germany|FAU|IPv6 only||
|ptbtime1.ptb.de|1|Germany|PTB||2.9 months|
|ptbtime2.ptb.de|1|Germany|PTB||2.9 months|
|ptbtime3.ptb.de|1|Germany|PTB||2.9 months|
|ptbtime4.ptb.de|1|Germany|PTB||2.9 months|
|[www.jabber-germany.de](https://www.jabber-germany.de)|2|Germany|Jörg Morbitzer||2.9 months|
|[www.masters-of-cloud.de](https://www.masters-of-cloud.de)|2|Germany|Jörg Morbitzer||2.9 months|
|ntp.nanosrvr.cloud|1|Germany|Michael Byczkowski|IPv4 and IPv6|2.9 months|
||
|1.nts.nothingtohide.nl|2|Netherlands|Nothing to hide|IPv4 and IPv6|2.9 months|
|2.nts.nothingtohide.nl|2|Netherlands|Nothing to hide|IPv4 and IPv6|3 months|
|3.nts.nothingtohide.nl|2|Netherlands|Nothing to hide|IPv4 and IPv6|3 months|
|4.nts.nothingtohide.nl|2|Netherlands|Nothing to hide|IPv4 and IPv6|3 months|
|ntppool1.time.nl|1|Netherlands|TimeNL||2.9 months|
|ntppool2.time.nl|1|Netherlands|TimeNL||2.9 months|
|nts.decepticon.space|1|Netherlands|Rick Betting||2.9 months|
||
|[ntpmon.dcs1.biz](https://ntpmon.dcs1.biz)|3|Singapore|Sanjeev Gupta||2.9 months|
||
|nts.netnod.se|1|Sweden|Netnod|Anycast||
|gbg1.nts.netnod.se|1|Sweden|Netnod|For users near Göteborg|2.9 months|
|gbg2.nts.netnod.se|1|Sweden|Netnod|For users near Göteborg|2.9 months|
|lul1.nts.netnod.se|1|Sweden|Netnod|For users near Luleå|2.9 months|
|lul2.nts.netnod.se|1|Sweden|Netnod|For users near Luleå|2.9 months|
|mmo1.nts.netnod.se|1|Sweden|Netnod|For users near Malmö|2.9 months|
|mmo2.nts.netnod.se|1|Sweden|Netnod|For users near Malmö|2.9 months|
|sth1.nts.netnod.se|1|Sweden|Netnod|For users near Stockholm|2.9 months|
|sth2.nts.netnod.se|1|Sweden|Netnod|For users near Stockholm|2.9 months|
|svl1.nts.netnod.se|1|Sweden|Netnod|For users near Sundsvall|2.9 months|
|svl2.nts.netnod.se|1|Sweden|Netnod|For users near Sundsvall|2.9 months|
||
|[ntp.3eck.net](https://ntp.3eck.net)|3|Switzerland|Adrian Zaugg||2.9 months|
|[ntp.trifence.ch](https://ntp.trifence.ch)|2|Switzerland|Marcel Waldvogel|||
|[ntp.zeitgitter.net](https://ntp.zeitgitter.net)|2|Switzerland|Marcel Waldvogel|||
|[ntp01.maillink.ch](https://ntp01.maillink.ch)|1|Switzerland|Ueli Heuer||2.9 months|
|[ntp02.maillink.ch](https://ntp02.maillink.ch)|1|Switzerland|Ueli Heuer||2.9 months|
|[ntp03.maillink.ch](https://ntp03.maillink.ch)|1|Switzerland|Ueli Heuer||2.9 months|
|time.signorini.ch|1|Switzerland|Attilio Signorini|||
||
|ntp2.glypnod.com|2|UK|Hal Murray|London|2.9 months|
|ntp1.dmz.terryburton.co.uk|1|UK|Terry Burton|IPv4 and IPv6|2.9 months|
|ntp2.dmz.terryburton.co.uk|1|UK|Terry Burton|IPv4 and IPv6|2.9 months|
|ntp0.cam.ac.uk|2|UK|University of Cambridge, University Information Services (UIS)|IPv4 and IPv6|12 months|
|ntp1.cam.ac.uk|2|UK|University of Cambridge, University Information Services (UIS)|IPv4 and IPv6|12 months|
|ntp2.cam.ac.uk|2|UK|University of Cambridge, Department of Engineering|IPv4 and IPv6|12 months|
|ntp3.cam.ac.uk|2|UK|University of Cambridge, University Information Services (UIS)|IPv4 and IPv6|12 months|
||
|ntp1.glypnod.com|2|US|Hal Murray|San Francisco|2.9 months|
|ohio.time.system76.com|2|US|System76||2.9 months|
|oregon.time.system76.com|2|US|System76||2.9 months|
|virginia.time.system76.com|2|US|System76||2.9 months|
|[stratum1.time.cifelli.xyz](https://stratum1.time.cifelli.xyz)|1|US|Mike Cifelli||2.9 months|
|[time.cifelli.xyz](https://time.cifelli.xyz)|2|US|Mike Cifelli||2.9 months|
|[time.txryan.com](https://time.txryan.com)|2|US|Tanner Ryan||2.9 months|
|[ntp1.wiktel.com](https://ntp1.wiktel.com)|1|US|Wikstrom Telephone Company|IPv4 and IPv6|2.9 months|
|[ntp2.wiktel.com](https://ntp2.wiktel.com)|1|US|Wikstrom Telephone Company|IPv4 and IPv6|2.9 months|

The following servers are known to be virtualized and may be less accurate. YMMV.

|Hostname|Stratum|Location|Owner|Notes|Cert Validity|
|---|:---:|---|---|---|---|
|ntp.viarouge.net|2|France|Hubert Viarouge||3 months|
|ntp1.rdem-systems.com|2|France|[RDEM Systems](https://www.rdem-systems.com)|Equinix PA4, IPv4 and IPv6|2.9 months|
|ntp10.rdem-systems.com|2|France|[RDEM Systems](https://www.rdem-systems.com)|Equinix PA3, IPv4 and IPv6|2.9 months|
|ntp11.rdem-systems.com|2|France|[RDEM Systems](https://www.rdem-systems.com)|TH2 Paris, IPv4 and IPv6|2.9 months|
|ntp2.rdem-systems.com|2|France|[RDEM Systems](https://www.rdem-systems.com)|Equinix PA4, IPv4 and IPv6|2.9 months|
|ntp3.rdem-systems.com|2|France|[RDEM Systems](https://www.rdem-systems.com)|Equinix PA3, IPv4 and IPv6|2.9 months|
|ntp4.rdem-systems.com|2|France|[RDEM Systems](https://www.rdem-systems.com)|Equinix PA3, IPv4 and IPv6|2.9 months|
|ntp5.rdem-systems.com|2|France|[RDEM Systems](https://www.rdem-systems.com)|Equinix PA5, IPv4 and IPv6|2.9 months|
|ntp6.rdem-systems.com|2|France|[RDEM Systems](https://www.rdem-systems.com)|Equinix PA5, IPv4 and IPv6|2.9 months|
|ntp8.rdem-systems.com|2|France|[RDEM Systems](https://www.rdem-systems.com)|Equinix PA5, IPv4 and IPv6|2.9 months|
|ntp9.rdem-systems.com|2|France|[RDEM Systems](https://www.rdem-systems.com)|Equinix PA4, IPv4 and IPv6|2.9 months|
|ntp7.rdem-systems.com|2|Germany|[RDEM Systems](https://www.rdem-systems.com)|Frankfurt area, IPv4 and IPv6|2.9 months|
|[time.xargs.org](https://time.xargs.org)|3|US|Michael Driscoll|IPv4 and IPv6||

## Star History
<a href="https://star-history.com/#jauderho/nts-servers&Timeline">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=jauderho/nts-servers&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=jauderho/nts-servers&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=jauderho/nts-servers&type=Date" />
  </picture>
</a>
