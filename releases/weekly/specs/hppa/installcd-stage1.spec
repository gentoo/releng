subarch: hppa1.1
version_stamp: 20130920
target: livecd-stage1
rel_type:  default
profile: default/linux/hppa/13.0
snapshot: 20130920
source_subpath: default/stage3-hppa1.1-20130920
livecd/use:
	deprecated
	fbcon
	ipv6
	livecd
	loop-aes
	lvm1
	modules
	ncurses
	nls
	nptl
	nptlonly
	pam
	readline
	socks5
	ssl
	static-libs
	unicode
	xml

livecd/packages:
	app-accessibility/brltty
	app-admin/hddtemp
	app-admin/passook
	app-admin/pwgen
	app-admin/syslog-ng
	app-arch/unzip
	app-crypt/gnupg
	app-misc/screen
	app-misc/vlock
	app-portage/mirrorselect
	app-text/wgetpaste
	net-analyzer/traceroute
	net-dialup/mingetty
	net-dialup/rp-pppoe
	net-fs/cifs-utils
	net-fs/nfs-utils
	net-irc/irssi
	net-misc/dhcpcd
	net-misc/iputils
	net-misc/ntp
	net-misc/rdate
	net-misc/vconfig
	net-proxy/dante
	net-proxy/ntlmaps
	sys-apps/ethtool
	sys-apps/hdparm
	sys-apps/hwsetup
	sys-apps/iproute2
	sys-apps/pciutils
	sys-apps/sdparm
	sys-apps/usbutils
	sys-devel/binutils-hppa64
	sys-devel/kgcc64
	sys-fs/dosfstools
	sys-fs/e2fsprogs
#	sys-fs/jfsutils
	sys-fs/lsscsi
	sys-fs/cryptsetup
	sys-fs/lvm2
	sys-fs/lsscsi
	sys-fs/mdadm
	sys-fs/reiserfsprogs
	sys-fs/xfsprogs
	sys-libs/gpm
	www-client/links
	sys-devel/bc
