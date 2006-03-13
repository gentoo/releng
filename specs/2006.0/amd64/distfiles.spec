subarch: amd64
version_stamp: 2006.0
target: grp
rel_type: default
profile: default-linux/amd64/2006.0
snapshot: official
source_subpath: default/stage3-amd64-2006.0
grp: src

grp/use: 
	bonobo
	cdr
	dvd
	dvdr
	esd 
	gtkhtml 
	mozilla
	ruby
	tcltk
	ldap
	socks5
	fbcon
	atm

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
	prism54-firmware
	genkernel
	grub
	dante
	tsocks
	splashutils
	splash-themes-livecd
	pcmcia-cs
	acpid
	cryptsetup
	nvidia-kernel
	nvidia-glx
	alsa-lib
	alsa-oss
	alsa-utils
	alsa-driver
