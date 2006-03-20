## livecd-stage1 template for Gentoo Linux release bootable LiveCDs
## John Davis <zhen@gentoo.org>

subarch: hppa1.1
version_stamp: 2006.0
target: livecd-stage1
rel_type:  default
profile: default-linux/hppa/2005.0
snapshot: 20060123
source_subpath: default/stage3-hppa1.1-2006.0
livecd/use:
	-X
	-gtk
	-svga
	-perl
	-gpm
	ipv6
	socks5
	livecd
	fbcon
	ssl
	
	
livecd/packages:
	devfsd
	binutils-hppa64
	gcc-hppa64
	baselayout
	livecd-tools
	module-init-tools
	hotplug
	irssi
	metalog
	pciutils
	parted
	mt-st
	links
	star
	strace
	raidtools
	nfs-utils
	jfsutils
	usbutils
	speedtouch
	xfsprogs
	e2fsprogs
	reiserfsprogs
	hdparm
	nano
	less
	openssh
	dhcpcd
	mingetty
	pwgen
	dialog
	rp-pppoe
	screen
	mirrorselect
	iputils
	device-mapper
	vim
	pwgen
	mdadm
	netcat
	ethtool

