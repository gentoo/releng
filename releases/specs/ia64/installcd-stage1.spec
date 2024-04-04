subarch: ia64
version_stamp: @TIMESTAMP@
target: livecd-stage1
rel_type: 23.0-default
profile: default/linux/ia64/23.0
snapshot_treeish: @TREEISH@
source_subpath: 23.0-default/stage3-ia64-openrc-@TIMESTAMP@
compression_mode: pixz
portage_confdir: @REPO_DIR@/releases/portage/isos

livecd/use:
	compile-locales
	fbcon
	livecd
	socks5
	unicode
	xml

livecd/packages:
	app-admin/pwgen
	app-admin/syslog-ng
	app-arch/unzip
	app-crypt/gnupg
	app-misc/livecd-tools
	app-misc/screen
	app-portage/mirrorselect
	app-text/wgetpaste
	net-analyzer/traceroute
	net-dialup/mingetty
	net-fs/cifs-utils
	net-fs/nfs-utils
	net-irc/irssi
	net-misc/chrony
	net-misc/dhcpcd
	net-misc/iputils
	net-misc/rdate
	net-proxy/dante
	sys-apps/busybox
	sys-apps/ethtool
	sys-apps/fxload
	sys-apps/hdparm
	sys-apps/iproute2
	sys-apps/sdparm
	sys-block/parted
	sys-fs/cryptsetup
	sys-fs/dosfstools
	sys-fs/e2fsprogs
	sys-fs/jfsutils
	sys-fs/mdadm
	sys-fs/reiserfsprogs
	sys-fs/xfsprogs
	sys-libs/gpm
	sys-power/acpid
	www-client/links
