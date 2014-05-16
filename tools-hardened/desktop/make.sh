#!/bin/bash

WORKING=$(pwd)
CHROOTS=${CHROOTS:-"${WORKING}"}
MYROOT=${MYROOT:-""}

cleanup()
{
	cd ${WORKING}
	rm -f ramdisk.iso
	rm -f tinhat.igz
	rm -rf init
	rm -rf iso
}


mkinitramfs()
{
	local BUSYBOX="http://dev.gentoo.org/~twitch153/tinhat/busybox"

	cd ${WORKING}
	mkdir init

	cd init
	mkdir -p bin dev etc mnt/cdrom mnt/squashfs mnt/tmpfs proc sbin sys tmp usr/bin usr/sbin var

	wget -O ${WORKING}/init/bin/busybox "${BUSYBOX}"
	cp ../configs/init .
	chmod 755 bin/busybox
	chmod 755 init 

	chroot . /bin/busybox --install -s

	find . | cpio -H newc -o | gzip -9 > ../tinhat.igz

	cd ${WORKING}
	rm -rf init
}


mkiso()
{
	cd ${WORKING}
	mkdir -p iso/boot/grub

	mv tinhat.igz iso/boot
	cp -L ${CHROOTS}/${MYROOT}/boot/kernel iso/boot/tinhat
	cp files/th-boot/grub/stage2_eltorito iso/boot/grub
	cp configs/menu.lst  iso/boot/grub/menu.lst
	cp configs/ABOUT.html  iso/ABOUT.html

	mksquashfs ${CHROOTS}/${MYROOT} iso/tinroot -comp xz -e usr/src var/cache/edb usr/portage/distfiles

	mkisofs -R -b boot/grub/stage2_eltorito -no-emul-boot -boot-load-size 4 -boot-info-table -o ramdisk.iso iso

	rm -rf iso
}


nameit()
{
	DATE=$(date +%Y%m%d)
	NAME="${MYROOT}-${DATE}.iso"

	[ -f ramdisk.iso ] && mv ramdisk.iso $NAME || echo "Can't name ramdisk.iso, I didn't find it."
}


cleanup
mkinitramfs
mkiso
nameit
