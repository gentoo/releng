subarch: ppc64
target: livecd-stage1

rel_type: default
snapshot: 20060123
version_stamp: 2006.0
profile: default-linux/ppc/ppc64/2006.0/32bit-userland
source_subpath: default/stage3-ppc64-2006.0-32ul

chost: powerpc-unknown-linux-gnu
cflags: -O2 -pipe
cxxflags: -O2 -pipe

portage_overlay: /usr/local/portage

livecd/use:
	-*
	nptl
	nptlonly
	nocxx
	pam
	ipv6
	socks5
	ncurses
	readline
	atm
	livecd
	tcpd
	ssl
	unicode

livecd/packages:
	python
	livecd-tools
	dhcpcd
	e2fsprogs
	ethtool
	hdparm
	hfsplusutils
	hfsutils
	hotplug
	hwsetup
	iprutils
	iputils
	irssi
	jfsutils
	kbd
	less
	links 
	lvm2
	lzo 
	mac-fdisk
	mdadm
	mirrorselect
	mingetty
	netcat
	nfs-utils
	partimage
	parted
	passook
	pciutils
	popt
	pwgen
	raidtools
	reiserfsprogs
	screen
	strace
	syslog-ng
	coldplug
	ucl
	udev
	ufed
	unzip
	usbutils
	vim
	xfsprogs
	yaboot
