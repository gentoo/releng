subarch: i686
version_stamp: installer-latest
target: livecd-stage1
rel_type: default
profile: default/linux/x86/13.0/desktop
snapshot: latest
source_subpath: default/stage3-i686-desktop-latest
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
	app-admin/testdisk
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
### Can't emerge with profile USE
#	app-misc/beagle
	app-misc/mc
	app-misc/pax-utils
	app-misc/screen
	app-misc/splitvt
	app-misc/vlock
	app-office/dia
	app-office/gnucash
	app-office/gnumeric
	app-office/koffice
	app-office/openoffice-bin
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
	gnome-base/gdm
	gnome-base/gnome
	gnome-extra/evolution-exchange
	gnome-extra/gsynaptics
	gnome-extra/sensors-applet
	kde-base/kde-meta
	kde-base/kooka
	mail-client/evolution
	mail-client/thunderbird
	mail-client/sylpheed
	mail-client/claws-mail
	media-gfx/blender
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
	media-video/gxine
	media-video/lsdvd
	media-video/mplayer
	media-video/ogle-gui
	media-video/vlc
	media-video/xine-ui
	media-video/kmplayer
	net-analyzer/ettercap
	net-analyzer/netcat
	net-analyzer/nmap
	net-analyzer/snort
	net-analyzer/tcpdump
	net-analyzer/tcptraceroute
	net-analyzer/traceroute
	net-analyzer/wireshark
	net-dialup/mingetty
	net-dialup/minicom
### Masked (for removal)
#	net-dialup/penggy
	net-dialup/pptpclient
	net-dialup/rp-pppoe
	net-firewall/iptables
	net-firewall/kmyfirewall
### Compile failure (bug #146214)
#	net-ftp/ncftp
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
	net-wireless/aircrack-ng
	net-wireless/airsnort
### Masked by ~x86
#	net-wireless/b43-fwcutter
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
	sys-apps/apmd
	sys-apps/dmidecode
	sys-apps/ethtool
	sys-apps/fxload
	sys-apps/gradm
	sys-apps/hdparm
	sys-apps/hwsetup
#	sys-apps/ibm-powerpc-utils
#	sys-apps/ibm-powerpc-utils-papr
	sys-apps/iproute2
	sys-apps/ivman
#	sys-apps/lssbus
	sys-apps/memtester
	sys-apps/netplug
	sys-block/parted
	sys-apps/pcsc-lite
	sys-apps/pmount
#	sys-apps/powerpc-utils
	sys-apps/qtparted
	sys-apps/rsbac-admin
	sys-apps/sdparm
	sys-apps/sg3_utils
	sys-apps/slocate
	sys-apps/smartmontools
	sys-block/aoetools
	sys-block/disktype
	sys-block/gpart
	sys-block/gparted
	sys-block/mpt-status
	sys-block/partimage
	sys-block/qla-fc-firmware
#	sys-boot/aboot
#	sys-boot/elilo
	sys-boot/grub
	sys-boot/lilo
	sys-boot/syslinux
#	sys-boot/yaboot
#	sys-devel/binutils-hppa64
	sys-devel/distcc
#	sys-devel/gcc-hppa64
	sys-devel/gdb
	sys-firmware/iwl3945-ucode
	sys-firmware/iwl4965-ucode
	sys-firmware/iwl5000-ucode
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
	sys-fs/quota
	sys-fs/reiserfsprogs
	sys-fs/xfsdump
	sys-fs/xfsprogs
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
	www-client/opera
	www-client/seamonkey
	x11-base/xorg-x11
	x11-drivers/synaptics
	x11-misc/xscreensaver
### Masked (no stable keywords)
#	x11-plugins/gkrellm-plugins
	x11-themes/gdm-themes-livecd
	x11-themes/gentoo-artwork-livecd
	x11-wm/afterstep
	x11-wm/enlightenment
	x11-wm/fluxbox
	x11-wm/windowmaker
	xfce-base/xfce4
