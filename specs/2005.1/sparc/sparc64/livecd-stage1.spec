subarch: sparc64
version_stamp: 2005.1
target: livecd-stage1
rel_type: default
profile: default-linux/sparc/sparc64/2005.1
snapshot: 20050709
source_subpath: default/stage3-sparc64-2005.1

livecd/use:
	-*
	ipv6
	livecd
	minimal
	ncurses
	readline
	socks5
	ssl

livecd/packages:
	>=baselayout-1.11.12-r4
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
	lvm-user
	traceroute
	tcptraceroute
	ethtool
	netcat
	hwsetup
	hwdata-knoppix
	parted
