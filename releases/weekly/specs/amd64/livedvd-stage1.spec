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
	app-admin/gkrellm
	app-admin/hddtemp
	app-admin/ide-smart
	app-admin/logrotate
	app-admin/passook
	app-admin/pwgen
	app-admin/quickswitch
	app-admin/sudo
	app-admin/superadduser
	app-admin/syslog-ng
### Masked (~amd64)
#	app-admin/testdisk
	app-arch/alien
	app-arch/mt-st
	app-arch/unrar
	app-arch/unzip
	app-benchmarks/cpuburn
	app-cdr/bin2iso
	app-cdr/cdrdao
	app-cdr/cdrkit
	app-cdr/dvd+rw-tools
	app-cdr/gnomebaker
	app-cdr/k3b
	app-cdr/nrg2iso
	app-crypt/gnupg
	app-editors/bluefish
	app-editors/emacs
	app-editors/gvim
	app-editors/vim
	app-editors/xemacs
	app-forensics/chkrootkit
	app-laptop/i8kutils
### Compile fails
#	app-misc/beagle
	app-misc/mc
	app-misc/pax-utils
	app-misc/screen
### Masked (~amd64)
#	app-misc/splitvt
	app-misc/vlock
	app-office/dia
	app-office/gnucash
	app-office/gnumeric
	app-office/koffice
	app-office/openoffice
#	app-office/openoffice-bin
	app-office/scribus
	app-pda/gtkpod
	app-pda/ipodslave
	app-portage/herdstat
	app-portage/genlop
	app-portage/gentoolkit
	app-portage/gentoolkit-dev
	app-portage/layman
	app-portage/mirrorselect
	app-portage/portage-utils
	app-portage/ufed
	app-shells/bash-completion
	app-shells/gentoo-bashcomp
	app-shells/tcsh
	app-shells/zsh
	app-shells/zsh-completion
	app-text/tetex
	app-text/wgetpaste
	dev-util/anjuta
	dev-util/ccache
	dev-vcs/cvs
	dev-vcs/git
	dev-util/indent
	dev-util/kdbg
	dev-vcs/kdesvn
	dev-util/kdevelop
	dev-util/ltrace
	dev-util/strace
	dev-vcs/subversion
	dev-util/valgrind
	gnome-base/gnome
	gnome-extra/evolution-exchange
	gnome-base/gdm
### Masked (~amd64)
#	gnome-extra/gsynaptics
	gnome-extra/sensors-applet
	kde-base/kde-meta
	kde-base/kooka
	mail-client/evolution
	mail-client/thunderbird
	mail-client/thunderbird-bin
	mail-client/sylpheed
	mail-client/claws-mail
### Masked (~amd64)
#	media-gfx/blender
	media-gfx/digikam
	media-gfx/fbgrab
	media-gfx/gimp
	media-gfx/gimp-print
	media-gfx/gtkam
	media-gfx/inkscape
	media-gfx/xsane
	media-sound/amarok
	media-sound/audacious
	media-sound/audacity
	media-sound/easytag
	media-sound/gnomeradio
	media-sound/grip
	media-sound/hydrogen
	media-sound/rhythmbox
	media-video/dvdrip
	media-video/gqcam
#	media-video/gxine
	media-video/lsdvd
	media-video/mplayer
### Masked (~amd64)
#	media-video/mplayer-bin
	media-video/ogle-gui
	media-video/vlc
	media-video/xine-ui
	media-video/kmplayer
	net-analyzer/ettercap
	net-analyzer/netcat
	net-analyzer/nmap
	net-analyzer/snort
	net-analyzer/tcpdump
	net-analyzer/traceroute
	net-analyzer/wireshark
	net-dialup/mingetty
	net-dialup/minicom
### Masked (no keyword)
#	net-dialup/penggy
	net-dialup/pptpclient
	net-dialup/rp-pppoe
	net-firewall/iptables
	net-firewall/kmyfirewall
	net-ftp/ncftp
	net-fs/cifs-utils
	net-fs/nfs-utils
	net-fs/samba
	net-im/pidgin
	net-irc/irssi
	net-irc/xchat
	net-misc/bridge-utils
	net-misc/dhcpcd
	net-misc/iputils
	net-misc/ntp
	net-misc/rdate
	net-misc/rdesktop
	net-misc/tightvnc
	net-misc/vconfig
	net-misc/vpnc
	net-misc/whois
	net-nntp/pan
	net-p2p/bittorrent
	net-p2p/limewire
	net-print/cups
	net-proxy/dante
#	net-proxy/ntlmaps
	net-proxy/tsocks
### Masked (~amd64)
#	net-wireless/aircrack-ng
### Masked (~amd64)
#	net-wireless/airsnort
	net-wireless/b43-fwcutter
### Masked (~amd64)
#	net-wireless/bcm43xx-fwcutter
	net-wireless/gnome-bluetooth
	net-wireless/ipw2100-firmware
	net-wireless/ipw2200-firmware
	net-wireless/kdebluetooth
	net-wireless/prism54-firmware
	net-wireless/wepattack
	net-wireless/wireless-tools
	net-wireless/wpa_supplicant
	net-wireless/zd1201-firmware
	net-wireless/zd1211-firmware
	rox-base/rox
### Masked
#	sys-apps/apmd
	sys-apps/dmidecode
	sys-apps/ethtool
	sys-apps/fxload
	sys-apps/gradm
	sys-apps/hdparm
	sys-apps/hwsetup
### Masked (no keyword)
#	sys-apps/ibm-powerpc-utils
### Masked (no keyword)
#	sys-apps/ibm-powerpc-utils-papr
	sys-apps/iproute2
	sys-apps/ivman
### Masked (no keyword)
#	sys-apps/lssbus
	sys-apps/memtester
	sys-apps/netplug
	sys-block/parted
	sys-apps/pcsc-lite
	sys-apps/pmount
### Masked (no keyword)
#	sys-apps/powerpc-utils
### Masked (~amd64)
#	sys-apps/qtparted
### Compile fails
#	sys-apps/rsbac-admin
	sys-apps/sdparm
	sys-apps/sg3_utils
	sys-apps/slocate
	sys-apps/smartmontools
### Masked (~amd64)
#	sys-apps/tuxonice-userui
	sys-block/aoetools
	sys-block/disktype
### Masked (-amd64)
#	sys-block/gpart
	sys-block/gparted
	sys-block/mpt-status
	sys-block/partimage
	sys-block/qla-fc-firmware
### Masked (no keyword)
#	sys-boot/aboot
### Masked (no keyword)
#	sys-boot/elilo
	sys-boot/grub
	sys-boot/lilo
	sys-boot/syslinux
### Masked (no keyword)
#	sys-boot/yaboot
### Masked (no keyword)
#	sys-devel/binutils-hppa64
	sys-devel/distcc
### Masked (no keyword)
#	sys-devel/gcc-hppa64
	sys-devel/gdb
	sys-firmware/iwl3945-ucode
	sys-firmware/iwl4965-ucode
	sys-firmware/iwl5000-ucode
	sys-fs/cryptsetup
	sys-fs/dmraid
	sys-fs/dosfstools
	sys-fs/e2fsprogs
### Masked (~amd64)
#	sys-fs/hfsplusutils
	sys-fs/hfsutils
### Masked (no keyword)
#	sys-fs/iprutils
	sys-fs/jfsutils
	sys-fs/lsscsi
	sys-fs/lvm2
	sys-fs/mac-fdisk
	sys-fs/mdadm
	sys-fs/multipath-tools
	sys-fs/ntfs3g
	sys-fs/reiserfsprogs
	sys-fs/quota
	sys-fs/xfsprogs
	sys-fs/xfsdump
	sys-kernel/genkernel
	sys-libs/gpm
	sys-power/acpid
	sys-power/apcupsd
	sys-process/htop
	sys-process/lsof
	sys-process/vixie-cron
	www-client/epiphany-extensions
	www-client/galeon
	www-client/links
	www-client/firefox
	www-client/firefox-bin
	www-client/opera
	www-client/seamonkey
	www-client/seamonkey-bin
	x11-base/xorg-x11
	x11-drivers/synaptics
	x11-misc/xscreensaver
### Masked (no keyword)
#	x11-plugins/gkrellm-plugins
	x11-themes/gdm-themes-livecd
	x11-themes/gentoo-artwork-livecd
	x11-wm/afterstep
	x11-wm/enlightenment
	x11-wm/fluxbox
	x11-wm/windowmaker
	xfce-base/xfce4
