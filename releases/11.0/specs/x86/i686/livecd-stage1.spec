subarch: i686
version_stamp: installer-10.0
target: livecd-stage1
rel_type: default
profile: default/linux/x86/10.0/desktop
snapshot: 20090806
source_subpath: default/stage3-i686-10.0
livecd/use:
	branding
	livecd
	loop-aes
	socks5

livecd/packages:
# Start new packages
	app-admin/eselect-esd
	app-admin/localepurge
	app-admin/paxtest
	app-admin/sysstat
	app-admin/testdisk
	app-admin/usbview
	#app-antivirus/bitdefender-console
	app-antivirus/clamav
	app-arch/afio
	app-arch/arc
	app-arch/arj
	app-arch/deb2targz
	app-arch/dump
	app-arch/file-roller
	app-arch/lha
	app-arch/lrzip
	app-arch/lzop
	app-arch/mscompress
	app-arch/ncompress
	app-arch/par2cmdline
	app-arch/rar
	app-arch/rzip
	app-arch/sharutils
	app-arch/unace
	app-arch/unarj
	app-arch/unrar
	app-arch/upx
	app-arch/zoo
	app-backup/dar
	app-backup/duplicity
	app-backup/rdiff-backup
	app-backup/rsnapshot
	app-cdr/bin2iso
	app-cdr/ccd2iso
	app-cdr/cdrdao
	app-cdr/mdf2iso
	app-cdr/nrg2iso 
	app-crypt/johntheripper
	app-editors/gedit
	app-editors/gvim
	app-editors/hexedit
	app-forensics/cmospwd
	app-forensics/foremost
	app-forensics/magicrescue
	app-forensics/sleuthkit
	app-misc/ckermit
	app-misc/wipe
	app-text/a2ps
	app-text/evince
	dev-util/strace
	dev-util/yacc
	media-gfx/gimp
	media-gfx/sane-frontends
	media-gfx/xsane
	media-plugins/gst-plugins-esd
	media-sound/alsa-utils
	media-sound/aumix
	media-video/mplayer
	media-video/rovclock
	net-firewall/guarddog
	net-ftp/gftp
	net-ftp/ncftp
	net-im/licq
	net-im/ysm
	net-misc/networkmanager
	net-misc/putty		
	net-wireless/ipw3945-ucode
	net-wireless/ipw3945d
	sys-apps/chpax
	sys-apps/hwdata-gentoo
	sys-apps/lshw
	sys-apps/paxctl
	sys-apps/readahead-list
	sys-block/gparted
	sys-block/tw_cli
	sys-fs/dd-rescue
	sys-fs/ddrescue
	sys-power/powernowd
	sys-power/powertop
	www-client/httrack
# end new packages
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
	app-cdr/cdrkit
	app-crypt/gnupg
	app-editors/emacs
	app-editors/vim
	app-misc/mc
	app-misc/screen
	app-misc/vlock
### Removed for space reasons
#	app-office/openoffice-bin
	app-portage/gentoolkit
	app-portage/mirrorselect
	app-portage/ufed
	app-text/wgetpaste
	dev-util/ccache
	dev-util/cvs
	dev-util/git
	dev-util/subversion
	gnome-base/gdm
### Removed for space reasons
#	mail-client/mozilla-thunderbird
	media-gfx/fbgrab
	media-sound/audacious
	net-analyzer/netcat
	net-analyzer/nmap
	net-analyzer/tcpdump
	net-analyzer/tcptraceroute
	net-analyzer/traceroute
	net-dialup/mingetty
	net-dialup/minicom
	net-dialup/penggy
	net-dialup/pptpclient
	net-dialup/rp-pppoe
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
	net-misc/vconfig
	net-misc/vpnc
	net-misc/whois
	net-p2p/bittorrent
	net-proxy/dante
	net-proxy/ntlmaps
	net-proxy/tsocks
### Masked by ~x86
#	net-wireless/b43-fwcutter
#	net-wireless/bcm43xx-fwcutter
	net-wireless/ipw2100-firmware
	net-wireless/ipw2200-firmware
	net-wireless/iwl3945-ucode
	net-wireless/iwl4965-ucode
# Failed to fetch.
#	net-wireless/prism54-firmware
	net-wireless/wireless-tools
	net-wireless/wpa_supplicant
	net-wireless/zd1201-firmware
	net-wireless/zd1211-firmware
	sys-apps/apmd
	sys-apps/eject
	sys-apps/ethtool
	sys-apps/fxload
	#sys-apps/gli
	sys-apps/hdparm
	sys-apps/hwsetup
#	sys-apps/ibm-powerpc-utils
#	sys-apps/ibm-powerpc-utils-papr
	sys-apps/iproute2
	sys-apps/memtester
	sys-apps/netplug
	sys-apps/parted
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
	sys-fs/dmraid
	sys-fs/dosfstools
	sys-fs/e2fsprogs
	sys-fs/evms
	sys-fs/hfsplusutils
	sys-fs/hfsutils
#	sys-fs/iprutils
	sys-fs/jfsutils
	sys-fs/lsscsi
	sys-fs/lvm2
#	sys-fs/lvm-user
	sys-fs/mac-fdisk
	sys-fs/mdadm
	sys-fs/ntfsprogs
	sys-fs/reiserfsprogs
	sys-fs/xfsprogs
	sys-kernel/genkernel
	sys-libs/gpm
	sys-power/acpid
	sys-process/htop
	sys-process/vixie-cron
	www-client/links
	www-client/mozilla-firefox
	x11-base/xorg-server
	x11-base/xorg-x11
	x11-themes/gdm-themes-livecd
	x11-themes/gentoo-artwork-livecd
	xfce-base/xfce4
