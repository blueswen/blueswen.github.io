---
categories:
- Tip
date: '2020-11-04'
tags:
- Web Development
---

# Chrome ERR_UNSAFE_PORT

問題：以 6666 port 開啟服務，使用 Chrome 瀏覽時出現 ERR_UNSAFE_PORT 錯誤訊息

原因：基於安全理由 Chrome 或其他瀏覽器會直接阻擋特定 port 的服務。Chromium 的[原始碼](https://chromium.googlesource.com/chromium/src.git/+/refs/heads/master/net/base/port_util.cc)有列出會被阻擋的清單，在使用時應特別注意。

```cpp
// The general list of blocked ports. Will be blocked unless a specific
// protocol overrides it. (Ex: ftp can use ports 20 and 21)
const int kRestrictedPorts[] = {
    1,       // tcpmux
    7,       // echo
    9,       // discard
    11,      // systat
    13,      // daytime
    15,      // netstat
    17,      // qotd
    19,      // chargen
    20,      // ftp data
    21,      // ftp access
    22,      // ssh
    23,      // telnet
    25,      // smtp
    37,      // time
    42,      // name
    43,      // nicname
    53,      // domain
    77,      // priv-rjs
    79,      // finger
    87,      // ttylink
    95,      // supdup
    101,     // hostriame
    102,     // iso-tsap
    103,     // gppitnp
    104,     // acr-nema
    109,     // pop2
    110,     // pop3
    111,     // sunrpc
    113,     // auth
    115,     // sftp
    117,     // uucp-path
    119,     // nntp
    123,     // NTP
    135,     // loc-srv /epmap
    139,     // netbios
    143,     // imap2
    179,     // BGP
    389,     // ldap
    427,     // SLP (Also used by Apple Filing Protocol)
    465,     // smtp+ssl
    512,     // print / exec
    513,     // login
    514,     // shell
    515,     // printer
    526,     // tempo
    530,     // courier
    531,     // chat
    532,     // netnews
    540,     // uucp
    548,     // AFP (Apple Filing Protocol)
    556,     // remotefs
    563,     // nntp+ssl
    587,     // smtp (rfc6409)
    601,     // syslog-conn (rfc3195)
    636,     // ldap+ssl
    993,     // ldap+ssl
    995,     // pop3+ssl
    2049,    // nfs
    3659,    // apple-sasl / PasswordServer
    4045,    // lockd
    6000,    // X11
    6665,    // Alternate IRC [Apple addition]
    6666,    // Alternate IRC [Apple addition]
    6667,    // Standard IRC [Apple addition]
    6668,    // Alternate IRC [Apple addition]
    6669,    // Alternate IRC [Apple addition]
    6697,    // IRC + TLS
};
```

6665~6669 是 IRC protocol 預設使用的 Port。IRC 有許多安全漏洞，為了避免 Chrome 變成跳板去影響其他服務，所以會主動進行阻擋。因此這些阻擋是保護 Service 本身，而不是保護 Chrome 的使用者。

Reference:

1. [Chrome错误代码:ERR_UNSAFE_PORT](https://www.applenice.net/2019/06/04/ERR-UNSAFE-PORT-On-Browser/)
2. [Which ports are considered unsafe by Chrome?](https://superuser.com/q/188058)
3. [Why does Chrome consider some ports unsafe?](https://jazzy.id.au/2012/08/23/why_does_chrome_consider_some_ports_unsafe.html)