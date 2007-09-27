subarch: alpha
version_stamp: 2007.1
target: grp
rel_type: default
profile: default-linux/alpha/2007.1
snapshot: 2007.1
source_subpath: default/stage3-alpha-2007.1
grp: src

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
	devfsd
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
