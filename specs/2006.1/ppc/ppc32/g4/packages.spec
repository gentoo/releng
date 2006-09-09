subarch: g4
version_stamp: 2006.1
target: grp
rel_type: default
profile: default-linux/ppc/ppc32/2006.1/G4
snapshot: 2006.1
source_subpath: default/stage3-g4-2006.1
grp: cd2

grp/use: 
	-java
	nptl
	nptlonly
	dvdr
	samba
	xorg
	dri
	dbus
	hal
	bzip2
	qt3

grp/cd2/type: pkgset
grp/cd2/packages:
	xorg-x11
	Xorgautoconfig
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
	samba
	cups
	app-admin/sudo
	app-cdr/cdrtools
	cdrdao
	emacs
	xemacs
	dev-lang/ruby
	enlightenment
	mozilla-firefox
	mozilla-thunderbird
	xfce4
	openbox
	fluxbox
	sylpheed
	openoffice
	gnome
	kde-meta
	kde-i18n
	koffice-meta
	koffice-i18n
	xmms
	abiword
	gaim
	xchat
	tetex
	kile
	k3b
	nmap
	ettercap
	mplayer

