# $Header: /var/cvsroot/gentoo/src/releng/specs/2006.1/ppc/ppc64/packages-32ul.spec,v 1.1 2006-08-31 18:12:56 wolf31o2 Exp $
subarch: ppc64
version_stamp: 32ul-2006.1
target: grp
rel_type: default 
profile:  default-linux/ppc/ppc64/2006.1/32bit-userland
snapshot: 2006.1
source_subpath: default/stage3-ppc64-32ul-2006.1
grp: cd2

chost: powerpc-unknownlinux-gnu
cflags: -O2 -pipe
cxxflags: -O2 -pipe

grp/use: 
	-java
	dvdr
	imap
	ldap

grp/cd2/type: pkgset
grp/cd2/packages:
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
	xfce4
	fluxbox
	sylpheed
	gnome
	xmms
	gaim
	xchat
	tetex
	kile
	nmap
	ettercap
	mplayer

