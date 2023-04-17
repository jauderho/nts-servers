# NTP servers with NTS support

This is intended to bootstrap a list of NTP servers with NTS support given that NTS support is not currently widespread. Pull requests are welcome to add new sources. Please adhere to the format.

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
|www.jabber-germany.de|2|Germany|Jörg Morbitzer||
|www.masters-of-cloud.de|2|Germany|Jörg Morbitzer||
|ntp-by.dynu.net|1|Germany|Michael Byczkowski||
||
|ntppool1.time.nl|1|Netherlands|TimeNL||
|ntppool2.time.nl|1|Netherlands|TimeNL||
||
|ntpmon.dcs1.biz|1|Singapore|Sanjeev Gupta||
||
|nts.netnod.se|1|Sweden|Netnod|Anycast|
|sth1.nts.netnod.se|1|Sweden|Netnod|For users close to Stockholm|
|sth1.nts.netnod.se|1|Sweden|Netnod|For users close to Stockholm|
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


## Use this to verify connectivity (h/t [@cadusilva](https://github.com/cadusilva))
`chronyd -Q -t 3 'server NTP_SERVER_HERE iburst nts maxsamples 1'`
