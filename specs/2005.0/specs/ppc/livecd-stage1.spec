# $Header: /var/cvsroot/gentoo/src/releng/specs/2005.0/ppc/livecd-stage1.spec,v 1.3 2005-03-19 06:15:00 pylon Exp $
subarch: ppc
version_stamp: 2005.0
target: livecd-stage1
rel_type: default
profile: default-linux/ppc/2005.0
snapshot: 20050303
default_subpath: default/stage3-ppc-20050303

livecd/use: 
	-* 
	fbcon
	ipv6 
	livecd
	minimal
	pic 
	ppc 
	readline
	ssl

livecd/packages:
	app-admin/sudo
	baselayout
	bind-tools
	coldplug
	curl
	cvs
	devfsd
	device-mapper
	dhcpcd
	distcc
	e2fsprogs
	eject
	ethtool
	ftp
	gentoolkit
	gentoo-sources
	pegasos-sources
	gpm
	hdparm
	hfsplusutils
	hfsutils
	host
	hotplug
	iptables
	iputils
	irssi
	jfsutils
	keychain
	kpnadsl4linux
	less
	links
	livecd-tools
	lsof
	lvm2
	lynx
	lzo 
	mac-fdisk
	memtester
	mingetty
	mirrorselect
	module-init-tools
	nano
	nfs-utils
	ntp
	openssh
	parted
	pbbuttonsd
	pciutils
	popt
	ppp
	pppconfig
	pppoed
	pptpclient
	pwgen
	raidtools
	reiserfsprogs
	rp-pppoe
	screen
	syslog-ng
	ucl
	udev
	ufed
	unzip
	usbutils
	vim
	vixie-cron
	wget
	wireless-tools
	xfsprogs
	yaboot
	genkernel
