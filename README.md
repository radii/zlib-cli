This trivial program replaces `openssl zlib` because Debian
now builds OpenSSL with `no-zlib` due to [CVE-2012-4929](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=728055)

It is useful for dealing with Android `.ab` files if you choose
not to use Java apps.

Usage:

```
dd if=backup.ab bs=24 skip=1 | ./zlib.py -d | tar -xvf -
```
