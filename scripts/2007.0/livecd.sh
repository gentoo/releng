#!/bin/bash
 
if [[ -e /etc/X11/gdm/custom.conf ]]
then
	sed -e '/^[^#]\+=.\+$/d' /etc/X11/gdm/custom.conf > \
 	/etc/X11/gdm/custom.conf.old
	sed -i -e 's/gentoo-emergence/gentoo-livecd-2007.0/' \
	/etc/X11/gdm/custom.conf
fi

if [[ -e /etc/X11/gdm/gdm.conf ]]
then
	sed -i -e 's/gentoo-emergence/gentoo-livecd-2007.0/' \
	/etc/X11/gdm/gdm.conf
fi

if [[ -e /etc/conf.d/splash ]]
then
	sed -i -e "/^# SPLASH_TTYS=/ s/^#//" /etc/conf.d/splash
fi

if [[ -e /sbin/splash-functions.sh ]]
then
	sed -i -e 's/type" cachedir "${spl_/type" tmpfs "${spl_/' \
	/sbin/splash-functions.sh
fi

if [[ -e /etc/conf.d/clock ]]
then
	sed -i -e 's/#TIMEZONE="Factory"/TIMEZONE="UTC"/' /etc/conf.d/clock
fi

gconftool-2 --direct \
	--config-source xml:readwrite:/usr/livecd/gconf/gconf.xml.defaults \
	--type string --set /desktop/gnome/background/picture_filename \
	/usr/share/pixmaps/gentoo-livecd-2007.0/gentoo-livecd-2007.0-1024x768.png

case `uname -m` in
	i?86|x86_64)
		sed -i 's/DRIVER fbdev/DRIVER vesa/' /usr/share/hwdata/Cards
		sed -e 's/CONSOLEFONT="default8x16"/CONSOLEFONT="lat1-16"/' \
			-e '/^#CONSOLETRANSLATION="8859-1_to_uni"/ s/^#//' \
			-i /etc/conf.d/consolefont
	;;
esac

