subarch: sparc64
version_stamp: 2006.0
target: livecd-stage1
rel_type: default
profile: default-linux/sparc/sparc64/2006.0/2.4
snapshot: 20060123
source_subpath: default/stage3-sparc64-2006.0

livecd/use:
	-*
	ipv6
	livecd
	ncurses
	nocxx
	pam
	readline
	socks5
	ssl

livecd/packages:
	>=baselayout-1.11.14
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
	lvm-user
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
	python
	mirrorselect
	iputils
	traceroute
	tcptraceroute
	ethtool
	netcat
	parted
	hwsetup
