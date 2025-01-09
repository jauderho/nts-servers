# NTP servers with NTS support

[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/jauderho/nts-servers/badge)](https://securityscorecards.dev/viewer/?uri=github.com/jauderho/nts-servers)

This is intended to bootstrap a list of NTP servers with NTS support given that NTS support is not currently widespread.

## Contribute
- Pull requests are welcome to add new sources ([signed commits](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits) are preferred)
- PR will not be merged until connectivity to server can be verified
- Please specify if server is virtualized
- You can now update `nts-sources.yml` to modify both the `README.md` and `chrony.conf`
  - Run `./scripts/ntpServerConverter.py nts-sources.yml`
  - Use `git diff origin README.md chrony.conf` to verify that you have a clean update before submitting a PR

## Usage
- There is no endorsement of any particular server. Please carefully vet before usage
- Before using anycast NTP servers, make sure that you understand the [limitations](https://www.rfc-editor.org/rfc/rfc8633.html#page-17)
- Use [at least 4 time sources](https://support.ntp.org/Support/SelectingOffsiteNTPServers#Upstream_Time_Server_Quantity) as a best practice. No more than 10 should be used
- It is not possible to mix and match NTP and NTS at this time. Only NTS servers should be specified as the NTP entries will not be used
- Generally, virtualized systems do not make for good time sources as there is too much jitter. Submissions should strive to ensure that high quality time is available
- Verify NTS server connectivity using the following command
  - `./scripts/ntsCheck.sh <NTS_SERVER_NAME>` 

## The List
|Hostname|Stratum|Location|Owner|Notes|
|---|:---:|---|---|---|
|[time.cloudflare.com](https://time.cloudflare.com)|3|All|Cloudflare|Anycast|
||
|[nts.teambelgium.net](https://ntp.teambelgium.net)|1|Belgium|Team Belgium||
||
|a.st1.ntp.br|1|Brazil|ntp.br||
|b.st1.ntp.br|1|Brazil|ntp.br||
|c.st1.ntp.br|1|Brazil|ntp.br||
|d.st1.ntp.br|1|Brazil|ntp.br||
|gps.ntp.br|1|Brazil|ntp.br||
|brazil.time.system76.com|2|Brazil|System76||
|[time.bolha.one](https://time.bolha.one)|1|Brazil|Cadu Silva||
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
|gbg1.nts.netnod.se|1|Sweden|Netnod|For users close to Göteborg|
|gbg2.nts.netnod.se|1|Sweden|Netnod|For users close to Göteborg|
|lul1.nts.netnod.se|1|Sweden|Netnod|For users close to Luleå|
|lul2.nts.netnod.se|1|Sweden|Netnod|For users close to Luleå|
|mmo1.nts.netnod.se|1|Sweden|Netnod|For users close to Malmö|
|mmo2.nts.netnod.se|1|Sweden|Netnod|For users close to Malmö|
|sth1.nts.netnod.se|1|Sweden|Netnod|For users close to Stockholm|
|sth2.nts.netnod.se|1|Sweden|Netnod|For users close to Stockholm|
|svl1.nts.netnod.se|1|Sweden|Netnod|For users close to Sundsvall|
|svl2.nts.netnod.se|1|Sweden|Netnod|For users close to Sundsvall|
||
|[ntp.3eck.net](https://ntp.3eck.net)|2|Switzerland|Adrian Zaugg||
|[ntp.trifence.ch](https://ntp.trifence.ch)|2|Switzerland|Marcel Waldvogel||
|[ntp.zeitgitter.net](https://ntp.zeitgitter.net)|2|Switzerland|Marcel Waldvogel||
|time.signorini.ch|1|Switzerland|Attilio Signorini||
||
|ntp2.glypnod.com|2|UK|Hal Murray|London|
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
|[ntp.viarouge.net](http://ntp.viarouge.net)|2|France|Hubert Viarouge|EXPIRED CERT|
|time.xargs.org|2|US|Michael Driscoll|IPv4 and IPv6|

## Star History
<a href="https://star-history.com/#jauderho/nts-servers&Timeline">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=jauderho/nts-servers&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=jauderho/nts-servers&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=jauderho/nts-servers&type=Date" />
  </picture>
</a>
