#!/bin/bash -l

echo root:thuser | chpasswd

useradd -m thuser
gpasswd -a thuser disk
gpasswd -a thuser wheel
gpasswd -a thuser audio
gpasswd -a thuser video
gpasswd -a thuser floppy
gpasswd -a thuser tape
gpasswd -a thuser cdrom
gpasswd -a thuser cdrw
gpasswd -a thuser usb
gpasswd -a thuser games

gpasswd -a portage wheel

echo thuser:thuser | chpasswd

groupadd -g 9995 graudit
groupadd -g 9996 grslink
groupadd -g 9997 grasock
groupadd -g 9998 grcsock
groupadd -g 9999 grssock
