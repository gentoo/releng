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

echo gentoo:gentoo | chpasswd
