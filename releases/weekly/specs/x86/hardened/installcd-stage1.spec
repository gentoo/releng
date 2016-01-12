subarch: x86
version_stamp: hardened-latest
target: livecd-stage1
rel_type: hardened
profile: hardened/linux/x86
snapshot: latest
source_subpath: hardened/stage3-x86-hardened-latest
livecd/use:
	-*
	deprecated
	fbcon
	ipv6
	livecd
	loop-aes
	lvm1
	modules
	ncurses
#	nls
	pam
	readline
	socks5
	ssl
#	unicode
	xml

livecd/packages:
	app-accessibility/brltty
	app-admin/hddtemp
	app-admin/passook
	app-admin/pwgen
	app-admin/syslog-ng
	app-arch/unzip
	app-crypt/gnupg
	app-editors/mg
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
	net-misc/vconfig
	net-proxy/dante
#	net-proxy/ntlmaps
	net-proxy/tsocks
	net-wireless/ipw2100-firmware
	net-wireless/ipw2200-firmware
	net-wireless/prism54-firmware
	net-wireless/wireless-tools
	net-wireless/wpa_supplicant
	net-wireless/zd1201-firmware
	net-wireless/zd1211-firmware
	sys-apps/apmd
	sys-apps/ethtool
	sys-apps/fxload
	sys-apps/hdparm
	sys-apps/hwsetup
	sys-apps/iproute2
	sys-apps/memtester
	sys-apps/netplug
	sys-block/parted
	sys-apps/sdparm
#	sys-block/partimage
#	sys-block/qla-fc-firmware
	sys-firmware/iwl3945-ucode
	sys-firmware/iwl4965-ucode
	sys-firmware/iwl5000-ucode
	sys-fs/cryptsetup
	sys-fs/dmraid
	sys-fs/dosfstools
	sys-fs/e2fsprogs
#	sys-fs/hfsplusutils
#	sys-fs/hfsutils
	sys-fs/jfsutils
	sys-fs/lsscsi
	sys-fs/lvm2
#	sys-fs/mac-fdisk
	sys-fs/mdadm
#	sys-fs/multipath-tools
	sys-fs/ntfs3g
	sys-fs/reiserfsprogs
	sys-fs/xfsprogs
	sys-libs/gpm
	sys-power/acpid
	www-client/links
