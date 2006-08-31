subarch: sparc64
version_stamp: 2006.1
target: livecd-stage1
rel_type: default
profile: default-linux/sparc/sparc64/2006.1
snapshot: 2006.1
source_subpath: default/stage3-sparc64-2006.1

livecd/use:
	-*
	fbcon
	gpm
	ipv6
	jpeg
	livecd
	ncurses
	nocxx
	pam
	png
	readline
	socks5
	ssl

livecd/packages:
	~baselayout-1.11.15
	livecd-tools
	module-init-tools
	hotplug
	coldplug
	irssi
	rdate
	syslog-ng
	pciutils
	mt-st
	tar
	links
	raidtools
	mdadm
	lvm2
	evms
	nfs-utils
	usbutils
	e2fsprogs
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
	tcptraceroute
	ethtool
	netcat
	parted
	hwsetup
	lsscsi
	wipe
