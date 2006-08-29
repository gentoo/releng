subarch: ppc64
version_stamp: 2006.1-distfiles
target: grp
rel_type: default
profile: default-linux/ppc/ppc64/2006.1/32bit-userland
snapshot: 2006.1
source_subpath: default/stage3-ppc64-32ul-2006.1
grp: src

grp/use: 
	cdr
	dvd
	dvdr
	ruby
	-X
	-gtk

grp/src/type: srcset
grp/src/packages:
	hfsutils
	hfsplusutils
	dhcpcd
	slocate
	udev
	dcron
	fcron
	vixie-cron
	gentoo-sources
	vanilla-sources
	coldplug
	syslog-ng
	logrotate
	raidtools
	nfs-utils
	jfsutils
	xfsprogs
	e2fsprogs
	reiserfsprogs
	iputils
	lvm2
	evms
	mdadm
	ethtool
	genkernel
	yaboot
	pcmcia-cs
	yaboot
	usbutils
	pciutils
	iprutils
	ssmtp
	ibm-powerpc-utils-papr
	rp-pppoe




