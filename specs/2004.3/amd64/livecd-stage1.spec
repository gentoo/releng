subarch: amd64
version_stamp: 2004.3
target: livecd-stage1
rel_type: default
profile: default-linux/amd64/2004.3
snapshot: 20041011
source_subpath: default/stage3-amd64-20041011
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
	xfsprogs
	e2fsprogs
	reiserfsprogs
#	cryptsetup
	pwgen
	popt
	dialog
	rp-pppoe
	screen
	mirrorselect
#	penggy
	iputils
	acpid
	hwdata-knoppix
	hwsetup
	device-mapper
	lvm2
	vim
	pptpclient
	mdadm
	ethtool
	wireless-tools
#	madwifi-tools
#	ntlmaps
