subarch: ppc64
target: livecd-stage1
version_stamp: 32ul-2006.1
rel_type: default
profile: default-linux/ppc/ppc64/2006.1/32bit-userland
snapshot: 2006.1
source_subpath: default/stage3-ppc64-32ul-2006.1
chost: powerpc-unknown-linux-gnu
livecd/use:
	-*
	atm
	fbcon
	ipv6
	livecd
	ncurses
	-nls
	-nocxx
	nptl
	nptlonly
	pam
	readline
	socks5
	ssl
	unicode
	userlocales
	
livecd/packages:
	app-admin/passook
	app-admin/pwgen
	app-admin/syslog-ng
	app-arch/unzip
	app-editors/vim
	app-misc/livecd-tools
	app-misc/screen
	app-misc/vlock
	app-portage/mirrorselect
	dev-lang/python
	media-gfx/fbgrab
	net-analyzer/tcptraceroute
	net-analyzer/traceroute
	net-dialup/mingetty
	net-dialup/pptpclient
	net-dialup/rp-pppoe
	net-fs/nfs-utils
	net-irc/irssi
	net-misc/dhcpcd
	net-misc/iputils
	net-misc/rdate
	net-wireless/wireless-tools
	net-wireless/wpa_supplicant
	sys-apps/apmd
	sys-apps/coldplug
	sys-apps/eject
	sys-apps/ethtool
	sys-apps/fxload
	sys-apps/hdparm
	sys-apps/iproute2
	sys-apps/memtester
	sys-apps/parted
	sys-apps/ibm-powerpc-utils
	sys-apps/ibm-powerpc-utils-papr
	sys-block/partimage
	sys-boot/yaboot
	sys-fs/dosfstools
	sys-fs/e2fsprogs
	sys-fs/evms
	sys-fs/hfsplusutils
	sys-fs/hfsutils
	sys-fs/iprutils
	sys-fs/jfsutils
	sys-fs/lvm2
	sys-fs/mac-fdisk
	sys-fs/mdadm
	sys-fs/ntfsprogs
	sys-fs/raidtools
	sys-fs/reiserfsprogs
	sys-fs/xfsprogs
	sys-libs/gpm
	www-client/links
