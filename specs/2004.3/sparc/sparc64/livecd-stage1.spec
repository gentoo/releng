subarch: sparc64
version_stamp: 2004.3
target: livecd-stage1
rel_type: default
profile: default-linux/sparc/sparc64/2004.3
snapshot: 20041022
source_subpath: default/stage3-sparc64-2004.3

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
	>=baselayout-1.9.4-r5
	livecd-tools
	module-init-tools
	hotplug
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
	reiserfsprogs
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
	tcptraceroute
	ethtool
	netcat
