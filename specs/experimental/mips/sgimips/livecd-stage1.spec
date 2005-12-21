subarch: mips3
version_stamp: 2005.1
target: livecd-stage1
rel_type: default
profile: default-linux/mips/2005.0
snapshot: 20051016
source_subpath: default/stage3-mips3-2005.1-pre2

livecd/use:
	-*
	livecd
	minimal
	ncurses
	readline
	ssl
	userlocales

livecd/packages:
	baselayout
	livecd-tools
	hotplug
	coldplug
	irssi
	syslog-ng
	pciutils
	mt-st
	tar
	elinks
	nfs-utils
	usbutils
	e2fsprogs
	com_err
	ss
	nano
	vim
	less
	openssh
	dhcpcd
	mingetty
	pwgen
	popt
	dialog
	rp-pppoe
	screen
	mirrorselect
	iputils
	traceroute
	sdparm
	dvhtool
	ttcp
	gcc-mips64
	mdadm
	pork
