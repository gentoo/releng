subarch: alpha
version_stamp: 2008.0
target: livecd-stage1
rel_type: default
profile: default/linux/alpha/17.0
snapshot: 2008.0
source_subpath: default/stage3-alpha-2008.0
portage_confdir: @REPO_DIR@/releases/weekly/portage/isos
livecd/use:
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
	static-libs
	-static
	unicode
	xml

livecd/packages:
	app-admin/pwgen
	app-admin/syslog-ng
	app-arch/unzip
	app-crypt/gnupg
	app-editors/mg
	app-misc/livecd-tools
	app-misc/screen
	app-portage/mirrorselect
	app-text/wgetpaste
	net-analyzer/traceroute
	net-dialup/mingetty
	net-dialup/pptpclient
	net-dialup/rp-pppoe
	sys-fs/btrfs-progs
	net-fs/nfs-utils
	net-irc/irssi
	net-misc/dhcpcd
	net-misc/iputils
	net-misc/ntp
	net-misc/rdate
	net-proxy/dante
	net-proxy/tsocks
	sys-apps/busybox
	sys-apps/ethtool
	sys-apps/hdparm
	sys-apps/hwsetup
	sys-apps/iproute2
	sys-apps/sdparm
	sys-block/parted
	sys-fs/cryptsetup
	sys-fs/dmraid
	sys-fs/dosfstools
	sys-fs/e2fsprogs
	sys-fs/jfsutils
	sys-fs/lsscsi
	sys-fs/lvm2
	sys-fs/mdadm
	sys-fs/reiserfsprogs
	sys-fs/xfsprogs
	sys-kernel/linux-firmware
	sys-libs/gpm
	www-client/links
