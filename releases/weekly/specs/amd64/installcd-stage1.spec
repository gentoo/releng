subarch: amd64
version_stamp: 2008.0
target: livecd-stage1
rel_type: default
profile: default/linux/amd64/2008.0/no-multilib
snapshot: 2008.0
source_subpath: default/stage3-amd64-2008.0
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
	app-admin/passook
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
### Masked (no keywords)
#	net-dialup/penggy
	net-dialup/pptpclient
	net-dialup/rp-pppoe
	net-fs/nfs-utils
	net-irc/irssi
	net-misc/dhcpcd
	net-misc/iputils
	net-misc/ntp
	net-misc/rdate
	net-misc/vconfig
	net-proxy/dante
	net-proxy/ntlmaps
	net-proxy/tsocks
### Masked (~amd64)
#	net-wireless/b43-fwcutter
### Masked (~amd64)
#	net-wireless/bcm43xx-fwcutter
	net-wireless/ipw2100-firmware
	net-wireless/ipw2200-firmware
	net-wireless/iwl3945-ucode
	net-wireless/iwl4965-ucode
	net-wireless/prism54-firmware
	net-wireless/wireless-tools
	net-wireless/wpa_supplicant
	net-wireless/zd1201-firmware
	net-wireless/zd1211-firmware
	sys-apps/apmd
	sys-apps/eject
	sys-apps/ethtool
	sys-apps/fxload
	sys-apps/hdparm
	sys-apps/hwsetup
	sys-apps/iproute2
### Masked (no keywords)
#	sys-apps/lssbus
	sys-apps/memtester
	sys-apps/netplug
	sys-apps/parted
### Masked (no keywords)
#	sys-apps/powerpc-utils
### Masked (no keywords)
#	sys-apps/ibm-powerpc-utils
### Masked (no keywords)
#	sys-apps/ibm-powerpc-utils-papr
	sys-apps/sdparm
### Masked (~amd64)
#	sys-block/partimage
	sys-block/qla-fc-firmware
### Masked (no keywords)
#	sys-boot/yaboot
### Masked (no keywords)
#	sys-devel/binutils-hppa64
### Masked (no keywords)
#	sys-devel/gcc-hppa64
	sys-fs/cryptsetup
	sys-fs/dmraid
	sys-fs/dosfstools
	sys-fs/e2fsprogs
	sys-fs/evms
	sys-fs/hfsplusutils
	sys-fs/hfsutils
### Masked (no keywords)
#	sys-fs/iprutils
	sys-fs/jfsutils
	sys-fs/lsscsi
	sys-fs/lvm2
#	sys-fs/lvm-user
	sys-fs/mac-fdisk
	sys-fs/mdadm
	sys-fs/multipath-tools
	sys-fs/ntfsprogs
	sys-fs/reiserfsprogs
	sys-fs/xfsprogs
	sys-libs/gpm
	sys-power/acpid
### Masked (no keywords)
#	sys-power/apmd
	www-client/links
