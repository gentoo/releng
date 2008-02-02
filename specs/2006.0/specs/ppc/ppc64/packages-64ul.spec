# $Header: /var/cvsroot/gentoo/src/releng/specs/2006.0/ppc/ppc64/packages-64ul.spec,v 1.1 2006-03-15 18:49:34 wolf31o2 Exp $
subarch: ppc64
version_stamp: 2006.0-64ul
target: grp
rel_type: default 
profile:  default-linux/ppc/ppc64/2006.0/64bit-userland
snapshot: 20060123 
source_subpath: default/stage3-ppc64-2006.0-64ul
grp: cd2

chost: powerpc-unknownlinux-gnu
cflags: -O2 -pipe
cxxflags: -O2 -pipe

grp/use: 
	-java
	dvdr

grp/cd2/type: pkgset
grp/cd2/packages:
	xorg-x11
	gentoo-sources
	irssi
	gpm
	parted
	links
	hfsutils
	hfsplusutils
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
	samba
	cups
	app-admin/sudo
	app-cdr/cdrtools
	cdrdao
	emacs
	xemacs
	dev-lang/ruby
	enlightenment
	xfce4
	fluxbox
	sylpheed
	kde
	xmms
	gaim
	xchat
	tetex
	nmap
	mplayer
	cvs
	subversion


