subarch: alpha
version_stamp: 2004.3
target: livecd-stage1
rel_type: default
rel_version: 2004.3
profile: default-linux/alpha/2004.3
snapshot: 20041023
source_subpath: default/stage3-alpha-2004.3
livecd/use:
	-X
	-gtk
	-svga
	-fbcon
	livecd
livecd/packages:
	>=sys-apps/baselayout-1.8.6.12-r4
#	kudzu
#	module-init-tools
	hotplug
	>=glib-2
	irssi
	aumix
	metalog
	pciutils
	parted
	mt-st
	links
	star
	strace
	raidtools
	nfs-utils
	usbutils
	speedtouch
	xfsprogs
	e2fsprogs
	reiserfsprogs
	hdparm
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
	gpm
	screen
	mirrorselect
	iputils
	hwdata-knoppix
	hwsetup
	livecd-tools
	ucl
#	wireless-tools
#	gpart
