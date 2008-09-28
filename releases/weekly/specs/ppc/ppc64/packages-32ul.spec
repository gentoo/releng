# $Header: /var/cvsroot/gentoo/src/releng/specs/2008.0/powerpc/ppc64/packages-32ul.spec,v 1.3 2008.00-30 18:41:30 agaffney Exp $
subarch: ppc64
version_stamp: 32ul-2008.0
target: grp
rel_type: default 
profile:  default/linux/powerpc/ppc64/2008.0/32bit-userland
snapshot: 2008.0
source_subpath: default/stage3-ppc64-32ul-2008.0
grp: cd2

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
	pidgin
	xchat
	tetex
	kile
	nmap
	ettercap
	mplayer

