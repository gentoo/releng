# $Header: /var/cvsroot/gentoo/src/releng/specs/2006.1/ppc/ppc64/grp/ppc64-livecd-grp-src-64ul.spec,v 1.1 2006-08-31 17:57:10 dostrow Exp $
subarch: ppc64
version_stamp: src-64ul-2006.1
target: grp
rel_type: default 
profile:  default-linux/ppc/ppc64/2006.1/64bit-userland
snapshot: 2006.1
source_subpath: default/stage3-ppc64-64ul-2006.1
grp: src

grp/use: 
	-java
	dvdr

grp/src/type: srcset
grp/src/packages:
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


