subarch: sparc64
version_stamp: 2005.0
target: livecd-stage1
rel_type: default
profile: default-linux/sparc/sparc64/2005.0
snapshot: 20050303
source_subpath: default/stage3-sparc64-2005.0

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
	>=baselayout-1.9.4-r6
	livecd-tools
	module-init-tools
	hotplug
	coldplug
	irssi
	rdate
	syslog-ng
	pciutils
	mt-st
	links
	star
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
