subarch: alpha
version_stamp: @TIMESTAMP@
target: livecd-stage1
rel_type: default
profile: default/linux/alpha/17.0
snapshot_treeish: @TIMESTAMP@
source_subpath: default/stage3-alpha-openrc-@TIMESTAMP@
portage_confdir: @REPO_DIR@/releases/portage/isos-qemu
interpreter: /usr/bin/qemu-alpha
compression_mode: pixz
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
	app-editors/emacs
	app-editors/vim
	app-misc/livecd-tools
	app-misc/screen
	app-portage/mirrorselect
	app-text/wgetpaste
	net-analyzer/traceroute
	net-dialup/mingetty
	net-dialup/pptpclient
	net-dialup/rp-pppoe
	net-fs/nfs-utils
	net-irc/irssi
	net-misc/chrony
	net-misc/dhcpcd
	net-misc/iputils
	net-misc/rdate
	net-proxy/dante
	net-proxy/tsocks
	sys-apps/busybox
	sys-apps/ethtool
	sys-apps/hdparm
	sys-apps/iproute2
	sys-apps/sdparm
	sys-apps/usbutils
	sys-block/parted
	sys-devel/bc
	sys-fs/btrfs-progs
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
