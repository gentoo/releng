subarch: alpha
version_stamp: 2008.0
target: livecd-stage1
rel_type: default
profile: default/linux/alpha/13.0
snapshot: 2008.0
source_subpath: default/stage3-alpha-2008.0
livecd/use:
	deprecated
	fbcon
	ipv6
	livecd
	loop-aes
	lvm1
	ncurses
	nls
	pam
	readline
	socks5
	ssl
	static-libs
	unicode
	xml

livecd/packages:
	app-accessibility/brltty
#	app-admin/hddtemp
# No keywords on alpha
#	app-admin/passook
	app-admin/pwgen
	app-admin/syslog-ng
	app-arch/unzip
	app-crypt/gnupg
	app-editors/mg
	app-misc/screen
	app-misc/vlock
	app-portage/mirrorselect
	app-text/wgetpaste
#	media-gfx/fbgrab
	net-analyzer/traceroute
	net-dialup/mingetty
#	net-dialup/penggy
	net-dialup/pptpclient
	net-dialup/rp-pppoe
	net-fs/cifs-utils
	net-fs/nfs-utils
	net-irc/irssi
	net-misc/dhcpcd
	net-misc/iputils
	net-misc/ntp
	net-misc/rdate
#	net-misc/vconfig
	net-proxy/dante
	net-proxy/ntlmaps
	net-proxy/tsocks
#	net-wireless/ipw2100-firmware
#	net-wireless/ipw2200-firmware
#	net-wireless/prism54-firmware
#	net-wireless/wireless-tools
#	net-wireless/wpa_supplicant
#	net-wireless/zd1201-firmware
#	sys-apps/apmd
	sys-apps/busybox
	sys-apps/ethtool
#	sys-apps/fxload
	sys-apps/hdparm
	sys-apps/hwsetup
	sys-apps/iproute2
#	sys-apps/lssbus
#	sys-apps/memtester
# no keywords on alpha
#	sys-apps/netplug
#	sys-apps/powerpc-utils
#	sys-apps/ibm-powerpc-utils
#	sys-apps/ibm-powerpc-utils-papr
	sys-apps/sdparm
	sys-block/parted
#	sys-block/partimage
#	sys-block/qla-fc-firmware
#	sys-boot/yaboot
#	sys-devel/binutils-hppa64
#	sys-devel/gcc-hppa64
	sys-fs/cryptsetup
#	sys-fs/dmraid
	sys-fs/dosfstools
	sys-fs/e2fsprogs
#	sys-fs/hfsplusutils
#	sys-fs/hfsutils
#	sys-fs/iprutils
	sys-fs/jfsutils
	sys-fs/lsscsi
	sys-fs/lvm2
#	sys-fs/lvm-user
#	sys-fs/mac-fdisk
	sys-fs/mdadm
#	sys-fs/multipath-tools
#	sys-fs/ntfsprogs
	sys-fs/reiserfsprogs
	sys-fs/xfsprogs
	sys-libs/gpm
# No ACPI on alphas, not keyworded. 
#	sys-power/acpid
#	sys-power/apmd
	www-client/links
