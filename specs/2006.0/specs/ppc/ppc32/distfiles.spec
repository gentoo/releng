# $Header: /var/cvsroot/gentoo/src/releng/specs/2006.0/ppc/ppc32/distfiles.spec,v 1.1 2006-02-22 23:09:32 pylon Exp $
subarch: ppc
version_stamp: 2006.0
target: grp
rel_type: official
profile: default-linux/ppc/ppc32/2006.0
snapshot: official
source_subpath: official/stage3-ppc-2006.0
grp: src

grp/use:
	-java
	dvdr

grp/src/type: srcset
grp/src/packages:
	dhcpcd
	slocate
	udev
	dcron
	fcron
	vixie-cron
	gentoo-sources
	vanilla-sources
	coldplug
	hotplug
	fxload
	syslog-ng
	logrotate
	raidtools
	nfs-utils
	jfsutils
	xfsprogs
	e2fsprogs
	reiserfsprogs
	rp-pppoe
	iputils
	lvm2
	evms
	pptpclient
	mdadm
	ethtool
	wireless-tools
	wpa_supplicant
	genkernel
	yaboot
	bootcreator
	dante
	tsocks
	pcmcia-cs
	pbbuttonsd
	pciutils
	powerpc-utils
	powerprefs
	cryptsetup
        alsa-driver
        alsa-lib
        alsa-oss
        alsa-utils
	sys-apps/eject
