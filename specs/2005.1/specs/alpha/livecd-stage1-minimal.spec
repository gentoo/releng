subarch: alpha
version_stamp: 2005.1
target: livecd-stage1
rel_type: default
profile: default-linux/alpha/2005.0
snapshot: 20050709
distcc_hosts: localhost/5 alpha10.crl.dec.com/5
source_subpath: default/stage3-alpha-2005.1
livecd/use:
	-*
	ipv6
	socks5
	livecd
	ncurses
	readline
	ssl
	
livecd/packages:
	livecd-tools
	devfsd
	=vanilla-sources-2.4*
	=vanilla-sources-2.6*
	dhcpcd
	coldplug
	irssi
	gpm
	syslog-ng
	parted
	links
#	raidtools
	dosfstools
	nfs-utils
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
#	lvm2
#	evms
	vim
	pptpclient
#	mdadm
	ethtool
#	vlock
