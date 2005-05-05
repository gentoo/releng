subarch: alpha
version_stamp: 2005.0
target: livecd-stage1
rel_type: default
rel_version: 2005.0
profile: default-linux/alpha/2005.0
snapshot: 20050303
source_subpath: default/stage3-alpha-2005.0
distcc_hosts: gendcc01 gendcc02 gendcc03 gendcc04 gendcc05 gendcc06 gendcc07
livecd/use:
	-X
	-gtk
	-gtk2
	-qt
	-opengl
	-svga
	-fbcon
	livecd
livecd/packages:
	>=sys-apps/baselayout-1.8.6.12-r4
	devfsd
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
# auto* brokenness
#	xfsprogs
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
	lvm-user
#	wireless-tools
#	gpart
