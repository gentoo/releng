# $Header: /var/cvsroot/gentoo/src/releng/specs/2006.0/ppc/ppc32/livecd-stage1.spec,v 1.1 2006-02-22 23:09:32 pylon Exp $
subarch: ppc
version_stamp: 2006.0
target: livecd-stage1
rel_type: official
profile: default-linux/ppc/ppc32
snapshot: official
source_subpath: official/stage3-ppc-2006.0

livecd/use: 
	-* 
	dhcp
	fbcon
	fortran
	gpm
	jpeg
	ipv6 
	livecd
	minimal
	ncurses
	nocxx
	nls
	nptl
	pam
	png
	readline
	ssl
	unicode

livecd/packages:
	coldplug
	device-mapper
	dhcpcd
	dialog
	dosfstools
	e2fsprogs
	eject
	ethtool
	evms
	fbgrab
	fxload
	gpm
	hfsplusutils
	hfsutils
	hwsetup
	iproute2
	iputils
	irssi
	jfsutils
	links
	livecd-tools
	lvm2
	mac-fdisk
	memtester
	mdadm
	mirrorselect
	nfs-utils
	parted
	popt
	powerpc-utils
	pptpclient
	pwgen
	python
	raidtools
	reiserfsprogs
	rp-pppoe
	screen
	syslog-ng
	vim
	vlock
	wireless-tools
	wpa_supplicant
	xfsprogs
	yaboot
