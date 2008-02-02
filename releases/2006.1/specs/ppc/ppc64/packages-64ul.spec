subarch: ppc64
version_stamp: 64ul-2006.1
target: grp
rel_type: default 
profile:  default-linux/ppc/ppc64/2006.1/64bit-userland
snapshot: 2006.1
source_subpath: default/stage3-ppc64-64ul-2006.1
grp: cd2

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


