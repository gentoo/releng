subarch: amd64
version_stamp: 2005.0
target: grp
rel_type: default
profile: default-linux/amd64/2005.0
snapshot: 20050303
source_subpath: default/stage3-amd64-2005.0

grp: src cd2

grp/use: 
	X
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

grp/src/type: srcset
grp/src/packages:
	ucl
	udev
#	gentoo-sources
	gentoo-sources
#	vanilla-sources
#	development-sources
	rp-pppoe
	speedtouch
#	fcpci
#	fcdsl
	pptpclient
#	slmodem
	lvm2
	iputils
	vixie-cron
	fcron
	dcron
	sysklogd
	metalog
	syslog-ng
	raidtools
	jfsutils
	xfsprogs
	reiserfsprogs
	lvm2
	dosfstools
#	lilo
	grub
	gentoolkit
	chkrootkit
	isdn4k-utils
	iproute2
	nvidia-kernel
	nvidia-glx
#	ati-drivers
	wireless-tools
#	madwifi
	pcmcia-cs
	genkernel
	hotplug
	pciutils
	usbutils
	slocate
	
grp/cd2/type: pkgset
grp/cd2/packages:
	gentoo-sources
	pciutils
	hotplug
	dante
	tsocks
	sys-apps/eject
	sys-process/procps
	xorg-x11
	minicom
	links
	lynx
	parted
	whois
	tcpdump
	cvs
	unzip
	zip
	netcat
#	partimage
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
	fluxbox
	openoffice-bin
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
	xcdroast
	k3b
	samba
	nmap
#	gradm
#	ettercap
	logrotate
