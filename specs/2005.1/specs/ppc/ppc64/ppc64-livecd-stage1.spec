subarch: ppc64-64ul
target: livecd-stage1

rel_type: default
rel_version: 2005.1
snapshot: 20050709
version_stamp: 2005.1
profile: default-linux/ppc/2005.1/ppc64/64bit-userland/
source_subpath: default/stage3-ppc64-64ul-2005.1

livecd/use:
	-X
	-gtk
	-svga
	-unicode
	ipv6
	socks5
	pic
	livecd
	tcpd
	ssl

livecd/packages:
	baselayout
	livecd-tools
	genkernel
	module-init-tools
	ccache
	curl
	cvs
	dhcpcd
	dialog
	e2fsprogs
	ethtool
	ftp
	hdparm
	hfsplusutils
	hfsutils
	host 
	hotplug
	kudzu-knoppix
	hwsetup
	iprutils
	iputils
	irssi
	jfsutils
	keychain
	kbd
	less
	links 
	logrotate
	lynx
	lzo 
	mac-fdisk
	mdadm
	metalog
	mirrorselect
	mingetty
	nano
	nfs-utils
	openssh
	parted
	passook
	pciutils
	popt
 	ppc64-utils
	pwgen
	reiserfsprogs
	screen
	strace
	ucl
	udev
	ufed
	unzip
	usbutils
	vim
	vixie-cron
	wget
	xfsprogs
	yaboot-static
