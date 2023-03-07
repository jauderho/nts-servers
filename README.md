# NTP servers with NTS support

This is intended to bootstrap a list of NTP servers with NTS support given that NTS support is not currently widespread. Pull requests are welcome to add new sources. Please adhere to the format.

|Hostname|Stratum|Location|Owner|Notes|
|---|:---:|---|---|---|
|time.cloudflare.com|3|All|Cloudflare|Anycast|
||
|ohio.time.system76.com|2|US|System76||
|oregon.time.system76.com|2|US|System76||
|virginia.time.system76.com|2|US|System76||
||
|nts.ntp.se|1|Sweden|Netnod|
|nts.netnod.se|1|Sweden|Netnod|Anycast|
|sth1.nts.netnod.se|1|Sweden|Netnod||
|sth1.nts.netnod.se|1|Sweden|Netnod||

## Use this to verify connectivity (h/t [@cadusilva](https://github.com/cadusilva))
`chronyd -Q -t 3 'server NTP_SERVER_HERE iburst nts maxsamples 1'`
