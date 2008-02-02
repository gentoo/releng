# $Header: /var/cvsroot/gentoo/src/releng/specs/2005.1/ppc/ppc32/grp-ppc.spec,v 1.1 2005-08-07 21:36:55 pylon Exp $
subarch: ppc
version_stamp: 2005.1
target: grp
rel_type: default
profile: default-linux/ppc/2005.1/ppc
snapshot: current
source_subpath: default/stage3-ppc-2005.1
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
	wpa_supplicant
	genkernel
	yaboot
	bootcreator
	dante
	tsocks
	pcmcia-cs
	pbbuttonsd
	powerprefs
	cryptsetup
        alsa-driver
        alsa-lib
        alsa-oss
        alsa-utils

grp/cd2/type: pkgset
grp/cd2/packages:
	ibm-jdk-bin
	xorg-x11
	gentoo-sources
	irssi
	gpm
	parted
	links
	dosfstools
	hfsutils
	hfsplusutils
	screen
	mirrorselect
	vim
	xscreensaver
	ide-smart
	netcat
	gnupg
	sys-apps/eject
	minicom
	whois
	tcpdump
	cvs
	zip
	unzip
	partimage
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
	ettercap
	mplayer

