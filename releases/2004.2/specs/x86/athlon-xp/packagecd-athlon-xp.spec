subarch: athlon-xp
version_stamp: 2004.2
target: grp
rel_type: default
profile: default-x86-2004.2
snapshot: 20040710
distcc_hosts: localhost/3 gravity/3 orion/3
source_subpath: default/stage3-athlon-xp-2004.2
grp: src cd2

grp/use: 
	gtk2 
	gnome 
	kde 
	qt 
	bonobo 
	cdr 
	esd 
	gtkhtml 
	mozilla
	mysql
	perl
	ruby
	tcltk
	acl
	cups
	ldap
	ssl
	tcpd
	-svga

grp/src/type: srcset
grp/src/packages:
	gentoo-sources
	gentoo-dev-sources
	vanilla-sources
	development-sources
	iptables
	gpm
	rp-pppoe
	ppp
	speedtouch
	pciutils
	hdparm
	hotplug
	aumix
	xorg-x11
	iputils
	vixie-cron
	sysklogd
	metalog
	syslog-ng
	raidtools
	jfsutils
	xfsprogs
	reiserfsprogs
	lvm-user
	dosfstools
	lilo
	grub
	superadduser
	gentoolkit
	chkrootkit
	minicom
	lynx
	rpm2targz
	parted
	rdate
	whois
	tcpdump
	cvs
	unzip
	zip
	netcat
	isdn4k-utils
	nforce-net
	nforce-audio
	iproute
	nvidia-kernel
	nvidia-glx
	ati-drivers
	e100
	e1000
	wireless-tools
	pcmcia-cs
	emu10k1
	evms
	linux-wlan-ng
	sys-apps/eject
	genkernel
	
grp/cd2/type: pkgset
grp/cd2/packages:
	pciutils
	hdparm
	hotplug
	aumix
	dante
	tsocks
	chkrootkit
	minicom
	lynx
	rpm2targz
	parted
	rdate
	whois
	tcpdump
	cvs
	unzip
	zip
	netcat
	partimage
	DirectFB
	apache
	app-cdr/cdrtools
	gnome
	evolution
	cups
	dev-db/mysql
	dev-lang/ruby
	emacs
	enlightenment
	fluxbox
	kde
	libsdl
	mozilla
	xfce4
	openbox
	openoffice-bin
	sylpheed
	vim
	xemacs
	xmms
	mozilla-firefox
	abiword
	gaim
	tetex
	xcdroast
	samba
	nmap
	gradm
	ettercap
	xchat
	dante
	tsocks
	logrotate
