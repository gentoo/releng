subarch: x86
version_stamp: 2004.3
target: livecd-stage1
rel_type: default
profile: default-linux/x86/2004.3
snapshot: 20041016
distcc_hosts: localhost/3 gravity/3 orion/3
source_subpath: default/stage3-x86-2004.3
livecd/use:
	-*
	ipv6
	socks5
	livecd
	fbcon
	minimal
	ncurses
	readline
	ssl
	
livecd/packages:
	baselayout
	livecd-tools
	mingetty
	module-init-tools
	dhcpcd
	udev
	gentoo-dev-sources
	kudzu-knoppix
	hotplug
	fxload
	syslog-ng
	parted
	links
	raidtools
	nfs-utils
	jfsutils
	usbutils
	pciutils
	xfsprogs
	e2fsprogs
	reiserfsprogs
	cryptsetup
	pwgen
	popt
	dialog
	rp-pppoe
	screen
	mirrorselect
	penggy
	iputils
	hwdata-knoppix
	hwsetup
	device-mapper
	lvm2
	evms
	vim
	pptpclient
	mdadm
	ethtool
	wireless-tools
#	madwifi-tools
#	ntlmaps
