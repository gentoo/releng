subarch: amd64
version_stamp: 2004.2
target: grp
rel_type: default
profile: default-amd64-2004.2
snapshot: 20040716
source_subpath: default/stage3-amd64-2004.2
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
	gentoo-dev-sources
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
	grub-static
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
	iproute2
	nvidia-kernel
	nvidia-glx
	wireless-tools
	pcmcia-cs
	evms
	sys-apps/eject
	genkernel
	
grp/cd2/type: pkgset
grp/cd2/packages:
	pciutils
	hdparm
	hotplug
	aumix
	xorg-x11
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
	xchat
	dante
	tsocks
	logrotate
