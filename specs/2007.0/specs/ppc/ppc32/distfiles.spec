subarch: ppc
version_stamp: 2007.0
target: grp
rel_type: default
profile: default-linux/ppc/ppc32/2007.0
snapshot: 2007.0
source_subpath: default/stage3-ppc-2007.0
grp: src

grp/use:
	branding

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
	fxload
	syslog-ng
	logrotate
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
	pcmciautils
	pbbuttonsd
	pciutils
	powerpc-utils
	powerprefs
	cryptsetup-luks
	alsa-driver
	alsa-lib
	alsa-oss
	alsa-utils
	sys-apps/eject
