subarch: ppc64
version_stamp: 2006.0-distfiles-64ul
target: grp
rel_type: default
profile: default-linux/ppc/ppc64/2006.0/64bit-userland/
snapshot: 20060123
source_subpath: default/stage3-ppc64-2006.0-64ul
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
	mdadm
	ethtool
	genkernel
	yaboot-static
	usbutils
	pciutils
	powerpc-utils
	iprutils
	ssmtp



