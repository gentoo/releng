subarch: x86
version_stamp: 2004.2
target: livecd-stage1
rel_type: default
profile: default-x86-2004.0
snapshot: 20040710
distcc_hosts: localhost/3 gravity/3 orion/3
source_subpath: default/stage3-x86-2004.2
livecd/use:
	-X
	-gtk
	-svga
	ipv6
	socks5
	livecd
	fbcon
	ssl
	
livecd/packages:
	baselayout
	livecd-tools
	gentoo-dev-sources
	genkernel
	bootsplash-themes-livecd
	ucl
	kudzu-knoppix
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
	popt
	dialog
	rp-pppoe
	gpm
	screen
	mirrorselect
	penggy
	iputils
	hwdata-knoppix
	hwsetup
	bootsplash
	device-mapper
	lvm2
	evms
	vim
	gpart
	pwgen
	pptpclient
	mdadm
	tcptraceroute
	netcat
	ethtool
	wireless-tools
