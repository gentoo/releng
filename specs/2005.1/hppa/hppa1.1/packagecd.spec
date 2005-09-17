subarch: hppa1.1
version_stamp: 2005.1
target: grp
rel_type: default
profile: default-linux/hppa/2005.0
snapshot: 20050709
source_subpath: default/stage3-hppa1.1-2005.1
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
	gif
	xv
	opengl

grp/src/type: srcset
grp/src/packages:
	dhcpcd
	slocate
	udev
	dcron
	fcron
	vixie-cron
	hppa-sources
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
	mdadm
	ethtool
	genkernel
	palo
	dante
	cryptsetup

grp/cd2/type: pkgset
grp/cd2/packages:
	xorg-x11
	hppa-sources
	irssi
	gpm
	parted
	links
	screen
	mirrorselect
	vim
	xscreensaver
	netcat
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
	kde
	mozilla-firefox
	xfce4
	openbox
	sylpheed
	xmms
	abiword
	gaim
	xchat
	pan
	tetex
	samba
	nmap
	ettercap
	mplayer
