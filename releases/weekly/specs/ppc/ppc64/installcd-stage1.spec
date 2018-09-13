subarch: ppc64
target: livecd-stage1
version_stamp: 32ul-2008.0
rel_type: default
profile: default/linux/powerpc/ppc64/17.0/32bit-userland
snapshot: 2008.0
source_subpath: default/stage3-ppc64-32ul-2008.0
compression_mode: pixz_x
decompressor_search_order: tar pixz xz lbzip2 bzip2 gzip

livecd/use:
	fbcon
	ipv6
	livecd
	lvm1
	modules
	ncurses
	nls
	nocxx
	nptl
	pam
	readline
	socks5
	ssl
	static-libs
	unicode
	xml
	
livecd/packages:
	app-accessibility/brltty
	app-admin/pwgen
	app-admin/syslog-ng
	app-arch/unzip
	app-crypt/gnupg
	app-misc/screen
	app-portage/mirrorselect
	app-text/wgetpaste
	net-analyzer/tcptraceroute
	net-analyzer/traceroute
	net-dialup/mingetty
	net-dialup/pptpclient
	net-dialup/rp-pppoe
	net-fs/cifs-utils
	net-fs/nfs-utils
	net-irc/irssi
	net-misc/dhcpcd
	net-misc/iputils
	net-misc/ntp
	net-misc/openssh
	net-misc/rdate
	net-misc/rsync
	net-wireless/wireless-tools
	net-wireless/wpa_supplicant
	sys-apps/busybox
	sys-apps/ethtool
	sys-apps/fxload
	sys-apps/hdparm
	sys-apps/ibm-powerpc-utils
	sys-apps/iproute2
	sys-apps/memtester
	sys-apps/sdparm
	sys-block/parted
	sys-boot/yaboot
	sys-fs/btrfs-progs
	sys-fs/dosfstools
	sys-fs/e2fsprogs
	sys-fs/hfsplusutils
	sys-fs/hfsutils
	sys-fs/iprutils
	sys-fs/jfsutils
	sys-fs/lvm2
	sys-fs/mac-fdisk
	sys-fs/mdadm
	sys-fs/ntfs3g
	sys-fs/reiserfsprogs
	sys-fs/xfsprogs
	sys-libs/gpm
	www-client/links
