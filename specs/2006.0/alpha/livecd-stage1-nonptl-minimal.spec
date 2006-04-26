subarch: alpha
version_stamp: 2006.0
target: livecd-stage1
rel_type: default
profile: default-linux/alpha/no-nptl
snapshot: 20060123
distcc_hosts: localhost gendcc01 gendcc02 gendcc03  gendcc05
source_subpath: default/stage3-alpha-2006.0-no-nptl
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
	
livecd/packages:
	livecd-tools
	=vanilla-sources-2.4*
	=vanilla-sources-2.6*
	pciutils
	dhcpcd
	acpid
	coldplug
	irssi
	gpm
	syslog-ng
	parted
	links
	raidtools
	dosfstools
	nfs-utils
	#jfsutils
	xfsprogs
	e2fsprogs
	reiserfsprogs
	pwgen
	popt
	dialog
	rp-pppoe
	screen
	mirrorselect
	iputils
	hwsetup
	lvm2
	#evms
	vim
	pptpclient
	mdadm
	ethtool
	unzip
	vlock
	lsscsi
#	dmraid
