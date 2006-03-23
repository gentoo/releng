version_stamp: 2006.0

subarch: ia64
target: livecd-stage1
rel_type: default
profile: default-linux/ia64/2006.0
snapshot: 20060123
source_subpath: default/stage3-ia64-2006.0

livecd/use:
	-*
	ipv6
	socks5
	livecd
	minimal
	ncurses
	readline
	ssl
	pam

livecd/packages:
	baselayout
	livecd-tools
	module-init-tools
	dhcpcd
	udev
	gentoo-sources
	hotplug
	coldplug
	fxload
	irssi
	gpm
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
	pwgen
	popt
	dialog
	screen
	mirrorselect
	iputils
	hwsetup
	hwdata-knoppix
	vim
	mdadm
	ethtool
	dosfstools
	genkernel
	lvm2
