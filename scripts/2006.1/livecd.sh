#!/bin/bash
 
sed -e '/^[^#]\+=.\+$/d' /etc/X11/gdm/custom.conf > \
 	/etc/X11/gdm/custom.conf.old
sed -i -e 's/gentoo-emergence/gentoo-livecd-2006.1/' \
	/etc/X11/gdm/custom.conf
