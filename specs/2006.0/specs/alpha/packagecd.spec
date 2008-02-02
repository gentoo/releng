subarch: alpha
version_stamp: 2006.0
target: grp
rel_type: default
profile: default-linux/alpha/2006.0
snapshot: 20060123
source_subpath: default/stage3-alpha-2006.0
distcc_hosts: localhost gendcc01 gendcc02 gendcc03  gendcc05
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
	cups
	ldap
	ssl
	tcpd
	-svga
	-tiff
	-directfb

grp/src/type: srcset
grp/src/packages:
	ucl
	udev
	=vanilla-sources-2.4*
	=vanilla-sources-2.6*
	rp-pppoe
	speedtouch
	pptpclient
	lvm-user
	iputils
	vixie-cron
	dcron
	sysklogd
	metalog
	syslog-ng
	raidtools
	xfsprogs
	reiserfsprogs
	dosfstools
	aboot
	gentoolkit
	chkrootkit
	isdn4k-utils
	iproute2
#	wireless-tools
	genkernel
	
grp/cd2/type: pkgset
grp/cd2/packages:
	pciutils
	hotplug
	dante
	tsocks
	sys-apps/eject
	xorg-x11
	minicom
	links
	lynx
	acpid
	parted
	whois
	tcpdump
	cvs
	unzip
	zip
	netcat
#	DirectFB
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
	fluxbox
	sylpheed
	vim
	xemacs
	xmms
	mozilla-firefox
	mozilla-thunderbird
	abiword
	gaim
	xchat
	tetex
	samba
	nmap
	ettercap
	logrotate
