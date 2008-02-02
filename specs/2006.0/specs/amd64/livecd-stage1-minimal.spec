subarch: amd64
version_stamp: 2006.0
target: livecd-stage1
rel_type: default
profile: default-linux/amd64/2006.0
snapshot: official
source_subpath: default/stage3-amd64-2006.0
livecd/use:
	-*
	ipv6
	socks5
	livecd
	fbcon
	ncurses
	readline
	ssl
	atm
	pam
	nocxx

livecd/packages:
	livecd-tools
	gentoo-sources
	dhcpcd
	acpid
	apmd
	coldplug
	fxload
	irssi
	gpm
	syslog-ng
	parted
	links
	raidtools
	dosfstools
	nfs-utils
	jfsutils
	xfsprogs
	e2fsprogs
	reiserfsprogs
	ntfsprogs
	pwgen
	popt
	dialog
	rp-pppoe
	screen
	python
	mirrorselect
#	penggy
	iputils
	hwsetup
	lvm2
	evms
	vim
	pptpclient
	mdadm
	ethtool
	wireless-tools
	prism54-firmware
#	zd1201-firmware
#	ipw2100-firmware
#	ipw2200-firmware
#	wpa_supplicant
	unzip
	vlock
	lsscsi
	vconfig
#	dmraid
