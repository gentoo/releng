version_stamp: 20040926
rel_version: 2004.3
snapshot: 20040926 
profile: default-linux/ppc/2004.3
source_subpath: default/stage3-ppc-20040926
subarch: g3
target: grp
rel_type: default

grp: src cd2

grp/use: 
	accessibility 
	alsa 
	apache2 
	apm 
	arts 
	cdr 
	crypt 
	-doc
	dvdr 
	gimpprint 
	gps
	gtk2
	icq 
	ipv6 
	java 
	kerberos 
	ldap 
	mysql 
	ncurses
	nntp 
	oldworld 
	oscar 
	pdflib 
	pic
	postgres 
	quicktime 
	radeon
	regexp 
	samba 
	sasl 
	sdk 
	snmp 
	socks5 
	spell 
	sqlite 
	tetex 
	tiff 
	unicode 
	xmms
	yahoo 
	zlib

grp/cd2/type: pkgset
grp/cd2/packages:
	unzip
	apache
	cdrtools
	cups
	curl
	cvs
	dhcpcd
	emacs
	enlightenment
	evolution
	fluxbox
	ftp
	gentoolkit
	gentoolkit-dev
	gimp
	gnome
	gpm
	hdparm
	host
	iptables
	iputils
	irssi
	kde
	keychain
	koffice
	links
	logrotate
	lynx
	mac-fdisk
	metalog
	mirrorselect
	mozilla
	mysql
	nano
	netcat
	nfs-utils
	nmap
	ntp
	openbox
	openoffice-ximian
	openssh
	parted
	passook
	pbbuttonsd
	pciutils
	pmud
	postgresql
	powerprefs
	ppp
	pppconfig
	pppoed
	raidtools
	rdate
	reiserfsprogs
	rpm2targz
	samba
	sash
	screen
	superadduser
	sysklogd
	syslog-ng
	tcpdump
	tetex
	ufed	
	unzip
	vim
	vixie-cron
	whois
	windowmaker
	xcdroast
	xchat
	xeasyconf
	xfce4
	xfsprogs
	yaboot

grp/src/type: srcset
grp/src/packages:
	gentoo-dev-sources
	metalog
	pcmcia-cs
	sysklogd
	syslog-ng
	vixie-cron
	wireless-tools
	yaboot
