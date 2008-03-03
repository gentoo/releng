subarch: ppc64
target: livecd-stage1
version_stamp: 32ul-2008.0
rel_type: default
profile: default/linux/powerpc/ppc64/2008.0/32bit-userland
snapshot: 2008.0
source_subpath: default/stage3-ppc64-32ul-2008.0

livecd/use:
	-*
	deprecated
	fbcon
	ipv6
	livecd
	loop-aes
	lvm1
	ncurses
	nls
	nocxx
	nptl
	nptlonly
	pam
	readline
	socks5
	ssl
	unicode
	
livecd/packages:
	app-accessibility/brltty
	app-admin/hddtemp
#	app-admin/passook
	app-admin/pwgen
	app-admin/syslog-ng
	app-arch/unzip
	app-editors/vim
	app-misc/screen
	app-misc/vlock
	app-portage/mirrorselect
	app-text/wgetpaste
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
	net-misc/ntp
	net-misc/rdate
	net-proxy/ntlmaps
	net-wireless/b43-fwcutter
	net-wireless/bcm43xx-fwcutter
	net-wireless/wireless-tools
	net-wireless/wpa_supplicant
	sys-apps/apmd
	sys-apps/eject
	sys-apps/ethtool
	sys-apps/fxload
	sys-apps/hdparm
	sys-apps/iproute2
#	sys-apps/lssbus
	sys-apps/memtester
	sys-apps/parted
	sys-apps/ibm-powerpc-utils
	sys-apps/ibm-powerpc-utils-papr
	sys-apps/sdparm
	sys-block/partimage
#	sys-block/qla-fc-firmware
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
	sys-fs/reiserfsprogs
	sys-fs/xfsprogs
	sys-libs/gpm
	www-client/links
