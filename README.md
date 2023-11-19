# NTP servers with NTS support

This is intended to bootstrap a list of NTP servers with NTS support given that NTS support is not currently widespread. 

Pull requests are welcome to add new sources (signed commits are preferred). Each PR should include any proposed changes to README.md and chrony.conf. Please adhere to the format.

- Before using anycast NTP servers, make sure that you understand the [limitations](https://www.rfc-editor.org/rfc/rfc8633.html#page-17)
- Generally, virtualized systems do not make for good time sources as there is too much jitter. Submissions should strive to ensure that high quality time is available. 

|Hostname|Stratum|Location|Owner|Notes|
|---|:---:|---|---|---|
|time.cloudflare.com|3|All|Cloudflare|Anycast|
||
|a.st1.ntp.br|1|Brazil|ntp.br||
|b.st1.ntp.br|1|Brazil|ntp.br||
|c.st1.ntp.br|1|Brazil|ntp.br||
|d.st1.ntp.br|1|Brazil|ntp.br||
|gps.ntp.br|1|Brazil|ntp.br||
|brazil.time.system76.com|2|Brazil|System76||
|time.bolha.one|1|Brazil|Cadu Silva||
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
|ntp-by.dynu.net|1|Germany|Michael Byczkowski||
|[nts.ntstime.de](https://ntstime.de)|2|Germany|Patrick Jansen||
||
|ntppool1.time.nl|1|Netherlands|TimeNL||
|ntppool2.time.nl|1|Netherlands|TimeNL||
||
|ntpmon.dcs1.biz|1|Singapore|Sanjeev Gupta||
||
|nts.netnod.se|1|Sweden|Netnod|Anycast|
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
|ntp.3eck.net|2|Switzerland|Adrian Zaugg||
|ntp.trifence.ch|2|Switzerland|Marcel Waldvogel||
|ntp.zeitgitter.net|2|Switzerland|Marcel Waldvogel||
|time.signorini.ch|1|Switzerland|Attilio Signorini||
||
|ohio.time.system76.com|2|US|System76||
|oregon.time.system76.com|2|US|System76||
|virginia.time.system76.com|2|US|System76||
|stratum1.time.cifelli.xyz|1|US|Mike Cifelli||
|time.cifelli.xyz|2|US|Mike Cifelli||
|time.txryan.com|2|US|Tanner Ryan||

The following servers are known to be virtualized and may be less accurate. YMMV.

|Hostname|Stratum|Location|Owner|Notes|
|---|:---:|---|---|---|
|[ntp.viarouge.net](http://ntp.viarouge.net)|2|France|Hubert Viarouge||

## Use this to verify connectivity (h/t [@cadusilva](https://github.com/cadusilva))
`chronyd -Q -t 3 'server <NTP_SERVER_HERE> iburst nts maxsamples 1'`

## Star History
<a href="https://star-history.com/#jauderho/nts-servers&Timeline">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=jauderho/nts-servers&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=jauderho/nts-servers&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=jauderho/nts-servers&type=Date" />
  </picture>
</a>
