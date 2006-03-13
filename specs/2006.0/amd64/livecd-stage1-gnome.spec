subarch: amd64
version_stamp: installer-2006.0
target: livecd-stage1
rel_type: default
profile: default-linux/amd64/2006.0
snapshot: official
source_subpath: default/stage3-amd64-2006.0
livecd/use:
	livecd
	socks5
	atm

livecd/packages:
	app-portage/gentoolkit
	sys-apps/baselayout
	x11-base/xorg-x11
	x11-misc/mkxf86config
	app-misc/livecd-tools
	sys-kernel/gentoo-sources
	net-misc/dhcpcd
	sys-apps/slocate
	sys-power/acpid
	sys-apps/apmd
	sys-apps/coldplug
	sys-apps/fxload
	net-irc/irssi
	sys-libs/gpm
	app-admin/syslog-ng
	app-admin/logrotate
	sys-apps/parted
	www-client/links
	sys-fs/raidtools
	sys-fs/dosfstools
	net-fs/nfs-utils
	sys-fs/jfsutils
	sys-fs/xfsprogs
	sys-fs/e2fsprogs
	sys-fs/reiserfsprogs
	sys-fs/ntfsprogs
	app-admin/pwgen
	dev-libs/popt
	dev-util/dialog
	net-dialup/rp-pppoe
	app-misc/screen
	app-portage/mirrorselect
#	net-dialup/penggy
	net-misc/iputils
	sys-apps/hwsetup
	sys-fs/lvm2
	sys-fs/evms
	app-editors/vim
	net-dialup/pptpclient
	sys-fs/mdadm
	sys-apps/ethtool
	net-wireless/wireless-tools
	net-wireless/prism54-firmware
#	net-wireless/zd1201-firmware
#	net-wireless/wpa_supplicant
	app-arch/unzip
	sys-fs/lsscsi
#	new stuff below here
	app-misc/vlock
	sys-kernel/genkernel
	dev-libs/libgpg-error
	media-libs/imlib
	x11-misc/xscreensaver
	app-admin/ide-smart
	net-analyzer/netcat
	sys-block/gpart
	app-crypt/gnupg
#	sys-boot/lilo
	sys-boot/grub
	net-proxy/dante
	net-proxy/tsocks
	sys-apps/eject
	net-dialup/minicom
	net-misc/whois
	net-analyzer/tcpdump
#	sys-block/partimage
	app-admin/sudo
	app-cdr/cdrtools
	gnome-base/gnome
	app-editors/emacs
#	x11-wm/enlightenment
#	kde-base/kde-meta
	www-client/mozilla-firefox
	mail-client/mozilla-thunderbird
#	xfce-base/xfce4
#	x11-wm/fluxbox
#	mail-client/sylpheed
	app-office/openoffice-bin
#	app-editors/xemacs
	media-sound/beep-media-player
	media-sound/rhythmbox
	net-im/gaim
	net-irc/xchat
	net-nntp/pan
#	app-text/tetex
#	app-cdr/k3b
#	app-office/koffice
	net-fs/samba
	app-portage/ufed
	net-analyzer/nmap
#	sys-apps/gradm
#	net-analyzer/ettercap
	net-analyzer/ethereal
	media-video/mplayer
	net-misc/rsync
	net-misc/bridge-utils
#	net-misc/vconfig
	sys-process/vixie-cron
#	net-wireless/airsnort
	sys-boot/syslinux
	sys-apps/smartmontools
	sys-devel/distcc
	dev-util/ccache
#	media-gfx/gimp
#	sys-fs/dmraid
#	x11-misc/synaptics
	net-p2p/bittorrent
	app-arch/unrar
	app-arch/mt-st
#	sys-fs/multipath-tools
	sys-apps/gli
