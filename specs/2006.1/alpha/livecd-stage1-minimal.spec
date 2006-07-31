subarch: alpha
version_stamp: 2006.1
target: livecd-stage1
rel_type: default
profile: default-linux/alpha/no-nptl
snapshot: 2006.1
source_subpath: default/stage3-alpha-2006.1-no-nptl
livecd/use:
	-*
	atm
	fbcon
	ipv6
	livecd
	ncurses
	nls
	pam
	readline
	socks5
	ssl
	unicode
	userlocales

livecd/packages:
	=sys-devel/gcc-3.3*
#	app-admin/passook
	app-admin/pwgen
	app-admin/syslog-ng
	app-arch/unzip
	app-editors/vim
	app-misc/livecd-tools
	app-misc/screen
	app-misc/vlock
	app-portage/mirrorselect
	dev-lang/python
#	media-gfx/fbgrab
#	net-analyzer/tcptraceroute
	net-analyzer/traceroute
#	net-dialup/bpalogin
	net-dialup/mingetty
#	net-dialup/penggy
	net-dialup/pptpclient
	net-dialup/rp-pppoe
	net-fs/nfs-utils
	net-irc/irssi
	net-misc/dhcpcd
	net-misc/iputils
	net-misc/rdate
#	net-misc/vconfig
#	net-wireless/ipw2100-firmware
#	net-wireless/ipw2200-firmware
#	net-wireless/prism54-firmware
#	net-wireless/wireless-tools
#	net-wireless/wpa_supplicant
#	net-wireless/zd1201-firmware
#	sys-apps/apmd
	sys-apps/coldplug
	sys-apps/eject
	sys-apps/ethtool
#	sys-apps/fxload
	sys-apps/hdparm
	sys-apps/hwsetup
	sys-apps/iproute2
#	sys-apps/memtester
	sys-apps/parted
#	sys-apps/powerpc-utils
#	sys-apps/ibm-powerpc-utils
#	sys-apps/ibm-powerpc-utils-papr
#	sys-block/partimage
#	sys-boot/yaboot
#	sys-devel/binutils-hppa64
#	sys-devel/gcc-hppa64
#	sys-fs/dmraid
	sys-fs/dosfstools
	sys-fs/e2fsprogs
#	sys-fs/evms
#	sys-fs/hfsplusutils
#	sys-fs/hfsutils
#	sys-fs/iprutils
#	sys-fs/jfsutils
	sys-fs/lsscsi
	sys-fs/lvm2
#	sys-fs/lvm-user
#	sys-fs/mac-fdisk
	sys-fs/mdadm
#	sys-fs/multipath-tools
#	sys-fs/ntfsprogs
	sys-fs/raidtools
	sys-fs/reiserfsprogs
	sys-fs/xfsprogs
	sys-libs/gpm
	sys-power/acpid
#	sys-power/apmd
	www-client/links
