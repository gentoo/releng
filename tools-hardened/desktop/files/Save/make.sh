#!/bin/bash

WORKING=$(pwd)
SKIP=$(echo $WORKING | sed -e 's/^\///')

welcome()
{
	echo
	echo "================================================================================"
	echo "= Building iso image from template ...                                         ="
	echo "= Hit Control-C at any continuation prompt to stop at that point               ="
	echo "================================================================================"
	echo  
}


cleanup()
{
	echo
	echo "================================================================================"
	echo "= Cleaning up any remaining tmp files from previous builds                     ="
	echo "= Removing ramdisk.iso tinhat.igz init/ iso/                                   ="
	echo "================================================================================"
	echo -n "Continue? " 
	read ANSWER

	cd ${WORKING}
	rm -f ramdisk.iso
	rm -f tinhat.igz
	rm -rf init
	rm -rf iso
}


mkinitramfs()
{
	echo
	echo "================================================================================"
	echo "= Building initramfs image which will be named tinhat.igz                      ="
	echo "================================================================================"
	echo -n "Continue? " 
	read ANSWER

	cd ${WORKING}

	mkdir init
	cd init

	mkdir -p bin dev etc mnt/cdrom mnt/squashfs mnt/tmpfs proc sbin sys tmp usr/bin usr/sbin var

	cp ../configs/busybox bin
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
	echo
	echo "================================================================================"
	echo "= Building the iso image which will be named ramdisk.iso                       ="
	echo "================================================================================"
	echo -n "Continue? " 
	read ANSWER

	cd ${WORKING}

	mkdir -p iso/boot/grub

	mv tinhat.igz iso/boot

	cp -L /boot/kernel iso/boot/tinhat

	cp /lib/grub/i386-pc/stage2_eltorito iso/boot/grub

	cp configs/menu.lst  iso/boot/grub/menu.lst


	mkdir -p root
	mount -o ro --bind / root
	mksquashfs root iso/tinroot -e usr/portage $SKIP usr/src var/cache/edb
	umount root
	rmdir root


	cp configs/ABOUT.html  iso/ABOUT.html

	mkisofs -R -b boot/grub/stage2_eltorito -no-emul-boot -boot-load-size 4 -boot-info-table -o ramdisk.iso iso

	rm -rf iso

	cd ${WORKING}
}


nameit()
{
	echo
	echo "================================================================================"
	echo "= Renaming the iso image as th-ARCH-DATE.iso                                   ="
	echo "================================================================================"
	echo -n "Continue? " 
	read ANSWER

	echo
	echo -n "Enter the RC suffix, empty for none: "
	read RC

	[ $(uname -m) == "x86_64" ] && ARCH="amd64"
	[ $(uname -m) == "i686"   ] && ARCH="i686"

	DATE=$(date +%Y%m%d)

	[ -z $RC ] && NAME="th-${ARCH}-${DATE}.iso" ||  NAME="th-${ARCH}-${DATE}-${RC}.iso"

	[ -f ramdisk.iso ] && mv ramdisk.iso $NAME || echo "Can't name ramdisk.iso, I didn't find it."
}


welcome
cleanup
mkinitramfs
mkiso
nameit

