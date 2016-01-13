subarch: amd64
version_stamp: installer-latest
target: livecd-stage1
rel_type: default
profile: default/linux/amd64/13.0/desktop
snapshot: latest
source_subpath: default/stage3-amd64-desktop-latest
livecd/use:
	branding
	livecd
	loop-aes
	socks5

livecd/packages:
	app-accessibility/brltty
	app-admin/hddtemp
	app-admin/ide-smart
	app-admin/logrotate
	app-admin/passook
	app-admin/pwgen
	app-admin/sudo
	app-admin/syslog-ng
	app-arch/mt-st
	app-benchmarks/cpuburn
#	app-cdr/cdrkit
	app-crypt/gnupg
#	app-editors/emacs
	app-editors/vim
	app-misc/mc
	app-misc/screen
	app-misc/vlock
#	app-office/openoffice-bin
#	app-office/openoffice
	app-portage/gentoolkit
	app-portage/mirrorselect
	app-portage/ufed
	app-text/wgetpaste
	dev-util/ccache
	dev-vcs/cvs
	dev-vcs/git
	dev-vcs/subversion
	gnome-base/gdm
#	gnome-base/gnome
	xfce-base/xfce4
	mail-client/thunderbird
#	mail-client/thunderbird-bin
	media-gfx/fbgrab
#	media-sound/audacious
	net-analyzer/netcat
	net-analyzer/nmap
	net-analyzer/tcpdump
	net-analyzer/traceroute
	net-dialup/mingetty
	net-dialup/minicom
### Masked (no keywords)
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
#	net-proxy/ntlmaps
	net-proxy/tsocks
	net-wireless/b43-fwcutter
### Masked (~amd64)
#	net-wireless/bcm43xx-fwcutter
	net-wireless/ipw2100-firmware
	net-wireless/ipw2200-firmware
	net-wireless/prism54-firmware
	net-wireless/wireless-tools
	net-wireless/wpa_supplicant
	net-wireless/zd1201-firmware
	net-wireless/zd1211-firmware
### Masked (no keywords)
#	sys-apps/apmd
	sys-apps/ethtool
	sys-apps/fxload
	sys-apps/hdparm
	sys-apps/hwsetup
### Masked (no keywords)
#	sys-apps/ibm-powerpc-utils
### Masked (no keywords)
#	sys-apps/ibm-powerpc-utils-papr
	sys-apps/iproute2
### Masked (no keywords)
#	sys-apps/lssbus
	sys-apps/memtester
	sys-apps/netplug
	sys-block/parted
### Masked (no keywords)
#	sys-apps/powerpc-utils
	sys-apps/sdparm
	sys-apps/sg3_utils
	sys-apps/slocate
	sys-apps/smartmontools
	sys-block/aoetools
	sys-block/disktype
### Masked (-amd64)
#	sys-block/gpart
	sys-block/partimage
	sys-block/qla-fc-firmware
### Masked (no keywords)
#	sys-boot/aboot
### Masked (no keywords)
#	sys-boot/elilo
	sys-boot/grub
#	sys-boot/lilo
	sys-boot/syslinux
### Masked (no keywords)
#	sys-boot/yaboot
### Masked (no keywords)
#	sys-devel/binutils-hppa64
	sys-devel/distcc
### Masked (no keywords)
#	sys-devel/gcc-hppa64
	sys-firmware/iwl3945-ucode
	sys-firmware/iwl4965-ucode
	sys-firmware/iwl5000-ucode
	sys-fs/cryptsetup
	sys-fs/dmraid
	sys-fs/dosfstools
	sys-fs/e2fsprogs
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
#	www-client/firefox-bin
	x11-base/xorg-server
	x11-base/xorg-x11
	x11-drivers/synaptics
	x11-themes/gdm-themes-livecd
	x11-themes/gentoo-artwork-livecd
