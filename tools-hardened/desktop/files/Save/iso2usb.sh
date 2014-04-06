#!/bin/bash

WORKING=$(pwd)

welcome ()
{
	echo
	echo "================================================================================"
	echo "= This script will transfer the contents of a bootable iso to a usb stick.     ="
	echo "=                                                                              ="
	echo "=        WARNING: IT WILL DESTROY THE CONTENTS OF THE USB STICK!!!             ="
	echo "=                                                                              ="
	echo "================================================================================"
	echo  
}


check ()
{
	echo
	echo "Enter the device name of the USB drive, eg sda                                 "
	echo "Don't worry, I'll show you the device's partition table before we wipe it      "
	echo
	echo -n "Device: "

	read DEVICE

	echo

	parted /dev/${DEVICE} print 

	echo -n "Are you sure? (Type uppercase yes): "

	read ANSWER

	if [[ $ANSWER != "YES" ]] ; then
		echo
		echo "ABORT! ABORT! ABORT!"
		echo
		exit
	fi
}


partition ()
{
	dd if=/dev/zero of=/dev/${DEVICE} bs=1 count=1024 >/dev/null 2>&1
	dd if=/usr/lib/syslinux/mbr.bin of=/dev/${DEVICE} >/dev/null 2>&1
	parted -s /dev/${DEVICE} mklabel msdos mkpartfs primary fat32 0 100% >/dev/null 2>&1
	parted -s /dev/${DEVICE} set 1 boot >/dev/null 2>&1
}


copyiso()
{
	echo
	echo "Enter the name of the iso image relative to ${WORKING} "
	echo
	echo -n "Name: "

	read IMAGE

	if [[ ! -f ${WORKING}/${IMAGE} ]] ; then
		echo
		echo "Cannot find iso image, exiting."
		echo
		exit
	fi

	cd ${WORKING}
	mkdir -p iso usb
	mount -o loop ${IMAGE} iso
	mount /dev/${DEVICE}1 usb

	cp iso/tinroot usb
	cp iso/boot/tinhat usb
	cp iso/boot/tinhat.igz usb
	cp configs/syslinux.cfg usb

	umount iso && rmdir iso
	umount usb && rmdir usb
}


finishup()
{
	syslinux /dev/${DEVICE}1
}


welcome
check
partition
copyiso
finishup

