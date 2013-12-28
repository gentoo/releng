#!/bin/bash -l

echo root:root | chpasswd

useradd -m gentoo
gpasswd -a gentoo disk
gpasswd -a gentoo wheel
gpasswd -a gentoo audio
gpasswd -a gentoo video
gpasswd -a gentoo floppy
gpasswd -a gentoo tape
gpasswd -a gentoo cdrom
gpasswd -a gentoo cdrw
gpasswd -a gentoo usb
gpasswd -a gentoo games

gpasswd -a portage wheel

echo gentoo:gentoo | chpasswd

groupadd -g 9995 graudit
groupadd -g 9996 grslink
groupadd -g 9997 grasock
groupadd -g 9998 grcsock
groupadd -g 9999 grssock
