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
		echo "kernel.uac.noprint = 1" >> /etc/sysctl.conf
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

echo "#####################################################" > /etc/fstab
echo "## ATTENTION: THIS IS THE FSTAB ON THE LIVECD      ##" >> /etc/fstab
echo "## PLEASE EDIT THE FSTAB at /mnt/gentoo/etc/fstab  ##" >> /etc/fstab
echo "#####################################################" >> /etc/fstab

# fstab tweaks
echo "tmpfs	/		tmpfs	defaults	0 0" >> /etc/fstab
echo "tmpfs	/usr/portage	tmpfs	defaults	0 0" >> /etc/fstab
#echo "tmpfs	/boot		tmpfs	defaults	0 0" >> /etc/fstab

# pull /boot from the CD
cd /boot && ls -1 | grep -v boot > /usr/livecd/bootfiles.txt
mv -f System.map* /usr/livecd
rm -rf /boot/*
cat << 'EOF' >> /etc/conf.d/local.start
if [ -n "$(ls /mnt/cdrom)" ]
then
	rm /boot
	mkdir /boot
	mount -t tmpfs tmpfs /boot
	INITRAMFS=`ls -1 /mnt/cdrom/{boot,isolinux}/*.igz 2>/dev/null | head -n 1`
	KERNEL=${INITRAMFS/.igz/}
	initramfs=`grep initr /usr/livecd/bootfiles.txt | head -n 1`
	kernel=`grep '^kernel-' /usr/livecd/bootfiles.txt | head -n 1`
	cp -f ${INITRAMFS} /boot/${initramfs}
	cp -f ${KERNEL} /boot/${kernel}
	cp -f /usr/livecd/System.map* /boot
fi
EOF

#[ -x /usr/bin/ktelnet ] && ln -sf /usr/bin/ktelnet /usr/bin/telnet
#[ -x /usr/bin/kftp ] && ln -sf /usr/bin/kftp /usr/bin/ftp

# Remove DefaultColorDepth
[ -e /etc/X11/xorg.conf.in ] && sed -i -e '/DefaultColorDepth/d' /etc/X11/xorg.conf.in

# This is here so that the retval of the line above (which may be non-0
# even if everything is ok) is not the retval of the script which would
# make catalyst unhappy.
exit 0                                                                          
