#!/bin/bash
# This is where we will put any release-specific fsscript code

if [[ -e /etc/conf.d/clock ]]
then
	sed -i -e 's/#TIMEZONE="Factory"/TIMEZONE="UTC"/' /etc/conf.d/clock
fi

case `uname -m` in
	alpha)
		echo >> /etc/sysctl.conf
		echo "# Disable UAC on Alpha" >> /etc/sysctl.conf
		echo "uac.noprint = 1" >> /etc/sysctl.conf
	;;
	i?86|x86_64)
		sed -i 's/DRIVER fbdev/DRIVER vesa/' /usr/share/hwdata/Cards
	;;
esac

# Enforce a unicode font by default
sed -e 's/CONSOLEFONT="default8x16"/CONSOLEFONT="lat1-16"/' \
	-e '/^#CONSOLETRANSLATION="8859-1_to_uni"/ s/^#//' \
	-i /etc/conf.d/consolefont

# This is necessary because /home/gentoo in the squashfs ends up getting owned
# by whoever the owner of the overlay files were on the build box. This causes
# weird stuff to happen like X failing to start because it doesn't have the
# ability to write the .Xauthority file
if [[ -d /home/gentoo ]]
then
	chown -R gentoo:users /home/gentoo
fi
