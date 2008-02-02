# $Header: /var/cvsroot/gentoo/src/releng/specs/2005.1/ppc/ppc32/livecd-stage1.spec,v 1.1 2005-08-07 21:34:05 pylon Exp $
subarch: ppc
version_stamp: 2005.1
target: livecd-stage1
rel_type: default
profile: default-linux/ppc/2005.1/ppc
snapshot: 20050709
source_subpath: default/stage3-ppc-2005.1
#distcc_hosts: localhost/2

livecd/use: 
	-* 
	atm
	fbcon
	ipv6 
	livecd
	ncurses
	readline
	socks5
	ssl

livecd/packages:
	coldplug
	device-mapper
	dhcpcd
	dialog
	dosfstools
	e2fsprogs
	eject
	ethtool
	evms
	fbgrab
	fxload
	gentoo-sources
	gpm
	hfsplusutils
	hfsutils
	hwsetup
	iputils
	irssi
	jfsutils
	links
	livecd-tools
	lvm2
	mac-fdisk
	memtester
	mdadm
	mirrorselect
	nfs-utils
	parted
	pbbuttonsd
	popt
	pptpclient
	pwgen
	raidtools
	reiserfsprogs
	rp-pppoe
	screen
	syslog-ng
	vim
	wireless-tools
	wpa_supplicant
	xfsprogs
	yaboot
