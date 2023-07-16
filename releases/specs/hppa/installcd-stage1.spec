subarch: hppa1.1
version_stamp: @TIMESTAMP@
target: livecd-stage1
rel_type:  default
profile: default/linux/hppa/17.0
snapshot_treeish: @TIMESTAMP@
source_subpath: default/stage3-hppa1.1-openrc-@TIMESTAMP@
pkgcache_path: /var/tmp/catalyst/packages/default/installcd-stage1
portage_confdir: @REPO_DIR@/releases/portage/isos
livecd/use:
	compile-locales
	fbcon
	livecd
	socks5
	unicode
	xml

livecd/packages:
	app-admin/hddtemp
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
	dev-util/debootstrap
	net-analyzer/traceroute
	net-fs/nfs-utils
	net-irc/irssi
	net-misc/chrony
	net-misc/dhcpcd
	net-misc/iputils
	net-misc/rdate
	net-misc/vconfig
	net-proxy/dante
	sys-apps/ethtool
	sys-apps/hdparm
	sys-apps/iproute2
	sys-apps/pciutils
	sys-apps/sdparm
	sys-apps/usbutils
	sys-devel/bc
	sys-devel/binutils-hppa64
	sys-devel/kgcc64
	sys-fs/cryptsetup
	sys-fs/dosfstools
	sys-fs/e2fsprogs
	sys-fs/lsscsi
	sys-fs/lvm2
	sys-fs/mdadm
	sys-fs/reiserfsprogs
	sys-fs/xfsprogs
	sys-libs/gpm
	www-client/links
