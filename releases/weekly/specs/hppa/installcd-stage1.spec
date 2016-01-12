subarch: hppa1.1
version_stamp: 20140201
target: livecd-stage1
rel_type:  default
profile: default/linux/hppa/13.0
snapshot: 20140201
source_subpath: default/stage3-hppa1.1-20140201
livecd/use:
	-*
	python_targets_python2_7
	bindist
	fbcon
	ipv6
	livecd
	lvm1
	ncurses
	nls
	pam
	readline
	socks5
	ssl
	openssl
	curl_ssl_openssl
	unicode

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
	dev-util/debootstrap
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
