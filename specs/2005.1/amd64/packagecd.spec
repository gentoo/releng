subarch: amd64
version_stamp: 2005.1
target: grp
rel_type: default
profile: default-linux/amd64/2005.1
snapshot: official
source_subpath: default/stage3-amd64-2005.1

distcc_hosts: pitr-int pitr-int localhost pitr-int pitr-int localhost

grp: src cd2

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

grp/cd2/type: pkgset
grp/cd2/packages:
	xorg-x11
	irssi
	gpm
	parted
	links
	dosfstools
	ntfsprogs
	screen
	mirrorselect
	vim
	xscreensaver
	ide-smart
	netcat
	gpart
	gnupg
	sys-apps/eject
	minicom
	whois
	tcpdump
	cvs
	zip
	unzip
	app-admin/sudo
	app-cdr/cdrtools
	gnome
	emacs
	dev-lang/ruby
	enlightenment
	kde-meta
	mozilla-firefox
	mozilla-thunderbird
	xfce4
	openbox
	fluxbox
	sylpheed
	openoffice-bin
	xemacs
	xmms
	abiword
	gaim
	xchat
	pan
	tetex
	k3b
	koffice
	samba
	nmap
	mplayer
