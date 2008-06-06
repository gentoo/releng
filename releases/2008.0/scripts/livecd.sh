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
echo "tmpfs	/lib/firmware	tmpfs	defaults	0 0" >> /etc/fstab
echo "tmpfs	/usr/portage	tmpfs	defaults	0 0" >> /etc/fstab
echo "tmpfs	/boot		tmpfs	defaults	0 0" >> /etc/fstab

# pull /boot from the CD
cd /boot && ls -1 | grep -v boot > /usr/livecd/bootfiles.txt
mv -f System.map* /usr/livecd
cat << EOF >> /etc/conf.d/local.start
if [ -n "$(ls /mnt/cdrom)" ]
then
	INITR_TMP=`ls -1 /mnt/cdrom/*/*.gz | head -n 1`
	INITRAMFS=`basename ${INITR_TMP}`
	KERNEL=${INITRAMFS/.gz/}
	initramfs=`grep initr /usr/livecd/bootfiles.txt | head -n 1`
	kernel=`grep kernel /usr/livecd/bootfiles.txt | head -n 1`
	cp -f /mnt/cdrom/*/${INITRAMFS} /boot/${initramfs}
	cp -f /mnt/cdrom/*/${KERNEL} /boot/${kernel}
	mv -f /usr/livecd/System.map* /boot
fi
EOF

