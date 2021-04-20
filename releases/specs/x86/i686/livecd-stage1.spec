subarch: i686
version_stamp: installer-@TIMESTAMP@
target: livecd-stage1
rel_type: default
profile: default/linux/x86/17.0/desktop
snapshot: @TIMESTAMP@
source_subpath: default/stage3-i686-desktop-@TIMESTAMP@
livecd/use:
	branding
	livecd
	socks5

livecd/packages:
	app-accessibility/brltty
	app-admin/hddtemp
	app-admin/ide-smart
	app-admin/logrotate
	app-admin/pwgen
	app-admin/sudo
	app-admin/syslog-ng
	app-arch/mt-st
	app-benchmarks/cpuburn
#	app-cdr/cdrkit
	app-crypt/gnupg
#	app-editors/emacs
	app-editors/vim
	app-misc/livecd-tools
	app-misc/mc
	app-misc/screen
### Removed for space reasons
#	app-office/openoffice-bin
	app-portage/gentoolkit
	app-portage/mirrorselect
	app-portage/ufed
	app-text/wgetpaste
	dev-util/ccache
	dev-vcs/cvs
	dev-vcs/git
	dev-vcs/subversion
	gnome-base/gdm
### Removed for space reasons
#	mail-client/thunderbird
	media-gfx/fbgrab
#	media-sound/audacious
	net-analyzer/netcat
	net-analyzer/nmap
	net-analyzer/tcpdump
#	net-analyzer/tcptraceroute
	net-analyzer/traceroute
	net-dialup/mingetty
	net-dialup/minicom
### Masked (for removal)
#	net-dialup/penggy
	net-dialup/pptpclient
	net-dialup/rp-pppoe
	net-firewall/iptables
	net-fs/cifs-utils
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
	net-misc/vconfig
	net-misc/vpnc
	net-misc/whois
	net-p2p/bittorrent
	net-proxy/dante
	net-proxy/tsocks
	net-wireless/b43-fwcutter
	net-wireless/wireless-tools
	net-wireless/wpa_supplicant
	sys-apps/ethtool
	sys-apps/fxload
	sys-apps/hdparm
#	sys-apps/ibm-powerpc-utils
#	sys-apps/ibm-powerpc-utils-papr
	sys-apps/iproute2
	sys-apps/memtester
	sys-apps/netplug
	sys-block/parted
#	sys-apps/powerpc-utils
	sys-apps/sdparm
	sys-apps/sg3_utils
	sys-apps/slocate
	sys-apps/smartmontools
	sys-block/aoetools
	sys-block/disktype
	sys-block/gpart
	sys-block/partimage
	sys-block/qla-fc-firmware
#	sys-boot/aboot
#	sys-boot/elilo
	sys-boot/grub
#	sys-boot/lilo
	sys-boot/syslinux
#	sys-boot/yaboot
#	sys-devel/binutils-hppa64
	sys-devel/distcc
#	sys-devel/gcc-hppa64
	sys-firmware/ipw2100-firmware
	sys-firmware/ipw2200-firmware
	sys-firmware/zd1201-firmware
	sys-firmware/zd1211-firmware
	sys-fs/dmraid
	sys-fs/dosfstools
	sys-fs/e2fsprogs
	sys-fs/hfsplusutils
	sys-fs/hfsutils
#	sys-fs/iprutils
	sys-fs/jfsutils
	sys-fs/lsscsi
	sys-fs/lvm2
#	sys-fs/lvm-user
	sys-fs/mac-fdisk
	sys-fs/mdadm
	sys-fs/ntfs3g
	sys-fs/reiserfsprogs
	sys-fs/xfsprogs
	sys-kernel/genkernel
	sys-libs/gpm
	sys-power/acpid
	sys-process/htop
	sys-process/vixie-cron
	www-client/links
	www-client/firefox
	x11-base/xorg-server
	x11-base/xorg-x11
	x11-drivers/synaptics
	x11-themes/gdm-themes-livecd
	x11-themes/gentoo-artwork-livecd
	xfce-base/xfce4
