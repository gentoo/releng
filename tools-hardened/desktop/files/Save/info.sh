#!/bin/bash

[ $(uname -m) == "x86_64" ] && ARCH=amd64
[ $(uname -m) == "i686"   ] && ARCH=i686

cat /etc/make.conf > make-conf.${ARCH}.txt
emerge --info      > emerge-info.${ARCH}.txt
epm -qa | sort     > epm-qa.${ARCH}.txt
emerge -vep world  > emerge-world.${ARCH}.txt
zcat /proc/config.gz > kernel-config.${ARCH}.txt

