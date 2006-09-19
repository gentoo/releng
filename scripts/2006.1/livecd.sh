#!/bin/bash
 
if [ -e /etc/X11/gdm/custom.conf ]
then
	sed -e '/^[^#]\+=.\+$/d' /etc/X11/gdm/custom.conf > \
 	/etc/X11/gdm/custom.conf.old
	sed -i -e 's/gentoo-emergence/gentoo-livecd-2006.1/' \
	/etc/X11/gdm/custom.conf
fi

if [ -e /etc/X11/gdm/gdm.conf ]
then
	sed -i -e 's/gentoo-emergence/gentoo-livecd-2006.1/' \
	/etc/X11/gdm/gdm.conf
fi

gconftool-2 --direct \
	--config-source xml:readwrite:/usr/livecd/gconf/gconf.xml.defaults \
	--type string --set /desktop/gnome/background/picture_filename \
	/usr/share/pixmaps/gentoo-livecd-2006.1/gentoo-livecd-2006.1-1024x768.png

case `uname -m` in
	i?86|x86_64)
		sed -i 's/DRIVER fbdev/DRIVER vesa/' /usr/share/hwdata/Cards
	;;
esac

sed -i -e 's:/psaux/:/input/:' /usr/sbin/mkxf86config.sh
sed -i '/^PORTDIR_OVERLAY/d' /etc/make.conf
rm -rf /root/catalyst
