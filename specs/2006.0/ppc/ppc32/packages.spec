# $Header: /var/cvsroot/gentoo/src/releng/specs/2006.0/ppc/ppc32/packages.spec,v 1.1 2006-09-02 00:00:46 wolf31o2 Exp $
subarch: ppc
version_stamp: 2006.0
target: grp
rel_type: official
profile: default-linux/ppc/ppc32/2006.0
snapshot: official
source_subpath: official/stage3-ppc-2006.0
grp: cd2

grp/use: 
	-java
	dvdr

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
	koffice-meta
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

