subarch: sparc64
version_stamp: @TIMESTAMP@
target: livecd-stage1
rel_type: 23.0-default
profile: default/linux/sparc/23.0/64ul
snapshot_treeish: @TREEISH@
source_subpath: 23.0-default/stage3-sparc64-openrc-@TIMESTAMP@
interpreter: /usr/bin/qemu-sparc64
compression_mode: pixz
portage_confdir: @REPO_DIR@/releases/portage/isos-qemu

livecd/use:
	compile-locales
	fbcon
	livecd
# needs broken dante
#	socks5
	unicode
	xml

livecd/packages:
# Masked (not keyworded, use.masked as well)
#	app-accessibility/brltty
	app-admin/hddtemp
	app-admin/pwgen
	app-admin/syslog-ng
	app-arch/unzip
	app-crypt/gnupg
	app-editors/mg
	app-editors/nano
	app-misc/livecd-tools
	app-misc/screen
	app-portage/mirrorselect
	app-text/wgetpaste
#	media-gfx/fbgrab
	net-analyzer/tcptraceroute
	net-analyzer/traceroute
	net-dialup/mingetty
#	net-dialup/pptpclient
#	net-dialup/rp-pppoe
#	net-fs/cifs-utils
	net-fs/nfs-utils
	net-irc/irssi
	net-misc/chrony
	net-misc/dhcpcd
	net-misc/iputils
#	net-misc/ndisc6
	net-misc/openssh
	net-misc/rdate
	net-misc/rsync
	net-misc/vconfig
#broken bug 639216
#	net-proxy/dante
# Not keyworded
#	net-proxy/ntlmaps
#	net-proxy/tsocks
#	net-wireless/iw
#	net-wireless/wireless-tools
#	net-wireless/wpa_supplicant
	sys-apps/arch-chroot
	sys-apps/busybox
#	sys-apps/dmidecode
	sys-apps/ethtool
	sys-apps/fxload
	sys-apps/gptfdisk
	sys-apps/hdparm
	sys-apps/iproute2
	sys-apps/lssbus
	sys-apps/memtester
	sys-apps/netplug
	sys-apps/sdparm
	sys-apps/usbutils
	sys-block/parted
#	sys-block/partimage
	sys-fs/btrfs-progs
	sys-fs/cryptsetup
#	sys-fs/dmraid
	sys-fs/dosfstools
	sys-fs/e2fsprogs
	sys-fs/genfstab
#	sys-fs/f2fs-tools
#	sys-fs/jfsutils
	sys-fs/lsscsi
	sys-fs/lvm2
#	sys-fs/mac-fdisk
	sys-fs/mdadm
#	sys-fs/multipath-tools
	sys-fs/ntfs3g
#	sys-fs/reiserfsprogs
	sys-fs/xfsprogs
	sys-kernel/linux-firmware
	sys-libs/gpm
	www-client/links
