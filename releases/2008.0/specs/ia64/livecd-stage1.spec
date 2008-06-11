subarch: ia64
version_stamp: installer-2008.0
target: livecd-stage1
rel_type: default
profile: default/linux/ia64/2008.0/desktop
snapshot: 2008.0
source_subpath: default/stage3-ia64-desktop-2008.0
livecd/use:
	branding
	livecd
	loop-aes
	socks5

livecd/packages:
	app-accessibility/brltty
#	app-admin/hddtemp
#	app-admin/ide-smart
	app-admin/logrotate
#	app-admin/passook
	app-admin/pwgen
	app-admin/sudo
	app-admin/syslog-ng
	app-arch/mt-st
#	app-benchmarks/cpuburn
	app-cdr/cdrkit
	app-crypt/gnupg
	app-editors/emacs
	app-editors/vim
	app-misc/mc
	app-misc/screen
	app-misc/vlock
#	app-office/openoffice
	app-portage/gentoolkit
	app-portage/mirrorselect
	app-portage/ufed
	app-text/wgetpaste
	dev-util/ccache
	dev-util/cvs
	dev-util/git
	dev-util/subversion
	gnome-base/gdm
	xfce-base/xfce4
	mail-client/mozilla-thunderbird
#	media-gfx/fbgrab
#	media-sound/audacious
	net-analyzer/netcat
	net-analyzer/nmap
	net-analyzer/tcpdump
#	net-analyzer/tcptraceroute
	net-analyzer/traceroute
	net-dialup/mingetty
	net-dialup/minicom
#	net-dialup/penggy
#	net-dialup/pptpclient
#	net-dialup/rp-pppoe
	net-firewall/iptables
	net-fs/mount-cifs
	net-fs/nfs-utils
	net-im/pidgin
	net-irc/irssi
	net-irc/xchat
	net-misc/bridge-utils
	net-misc/dhcpcd
	net-misc/iputils
	net-misc/ntp
	net-misc/rdate
	net-misc/rdesktop
#	net-misc/vconfig
#	net-misc/vpnc
	net-misc/whois
#	net-p2p/bittorrent
	net-proxy/dante
	net-proxy/ntlmaps
#	net-proxy/tsocks
#	net-wireless/ipw2100-firmware
#	net-wireless/ipw2200-firmware
#	net-wireless/prism54-firmware
#	net-wireless/wireless-tools
#	net-wireless/wpa_supplicant
#	net-wireless/zd1201-firmware
#	sys-apps/apmd
	sys-apps/eject
	sys-apps/ethtool
	sys-apps/fxload
	sys-apps/gli
	sys-apps/hdparm
	sys-apps/hwsetup
#	sys-apps/ibm-powerpc-utils
#	sys-apps/ibm-powerpc-utils-papr
	sys-apps/iproute2
#	sys-apps/lssbus
#	sys-apps/memtester
#	sys-apps/netplug
	sys-apps/parted
#	sys-apps/powerpc-utils
	sys-apps/sdparm
#	sys-apps/sg3_utils
	sys-apps/slocate
#	sys-apps/smartmontools
#	sys-block/aoetools
#	sys-block/disktype
#	sys-block/gpart
#	sys-block/partimage
#	sys-block/qla-fc-firmware
#	sys-boot/aboot
	sys-boot/elilo
#	sys-boot/grub
#	sys-boot/lilo
#	sys-boot/syslinux
#	sys-boot/yaboot
#	sys-devel/binutils-hppa64
	sys-devel/distcc
#	sys-devel/gcc-hppa64
	sys-fs/cryptsetup
	sys-fs/dosfstools
	sys-fs/e2fsprogs
	sys-fs/evms
#	sys-fs/hfsplusutils
#	sys-fs/hfsutils
#	sys-fs/iprutils
	sys-fs/jfsutils
#	sys-fs/lsscsi
#	sys-fs/lvm2
#	sys-fs/lvm-user
#	sys-fs/mac-fdisk
	sys-fs/mdadm
#	sys-fs/ntfsprogs
	sys-fs/reiserfsprogs
	sys-fs/xfsprogs
	sys-kernel/genkernel
	sys-libs/gpm
	sys-power/acpid
	sys-process/htop
	sys-process/vixie-cron
	www-client/links
	www-client/mozilla-firefox
	x11-base/xorg-x11
#	x11-drivers/synaptics
	x11-misc/xscreensaver
	x11-themes/gdm-themes-livecd
	x11-themes/gentoo-artwork-livecd
