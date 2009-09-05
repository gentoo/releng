subarch: i686
version_stamp: 10.0
target: livecd-stage1
rel_type: default
profile: default/linux/x86/10.0/desktop
snapshot: 20090903
source_subpath: default/stage3-i686-desktop-10.0
portage_confdir: /var/svnroot/releng/trunk/releases/10.0/portage

livecd/use:
	branding
	livecd
	loop-aes
	socks5
	gnome
	qt4
livecd/packages:
	x11-terms/terminal
	app-editors/mousepad
	x11-themes/xfce4-icon-theme
	x11-themes/tango-icon-theme
	media-fonts/dejavu
	xfce-extra/xfce4-places-plugin
	xfce-extra/thunar-thumbnailers
	xfce-extra/thunar-volman
	xfce-extra/xfce4-screenshooter
	xfce-extra/xfce4-xkb-plugin
	xfce-extra/xfce4-clipman-plugin
	xfce-extra/xfce4-notes-plugin
	xfce-extra/xfce4-mixer
	sys-block/partitionmanager
	sys-block/tw_cli
	kde-base/kdebase-meta
	gnome-base/gnome
	x11-proto/dri2proto
	net-misc/wicd
	app-admin/eselect-esd
	app-admin/localepurge
	app-admin/sysstat
	app-admin/usbview
	app-antivirus/clamav
	app-arch/afio
	app-arch/arc
	app-arch/arj
	app-arch/deb2targz
	app-arch/dump
	app-arch/file-roller
	app-arch/lha
# keywords.
#	app-arch/lrzip
	app-arch/lzop
	app-arch/mscompress
	app-arch/ncompress
	app-arch/par2cmdline
	app-arch/rar
	app-arch/rzip
	app-arch/sharutils
	app-arch/unace
	app-arch/unarj
	app-arch/upx
	app-arch/zoo
	app-backup/dar
	app-backup/duplicity
	app-backup/rdiff-backup
	app-backup/rsnapshot
	app-cdr/ccd2iso
	app-cdr/mdf2iso
	app-crypt/johntheripper
	app-editors/gedit
	app-editors/hexedit
# keywords.
#	app-forensics/cmospwd
#	app-forensics/foremost
#	app-forensics/magicrescue
	app-misc/ckermit
	app-misc/wipe
	app-text/a2ps
	app-text/evince
	dev-util/yacc
	media-gfx/sane-frontends
	media-plugins/gst-plugins-esd
	media-sound/alsa-utils
	media-sound/aumix
	media-video/rovclock
	net-ftp/gftp
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
	sys-fs/dd-rescue
	sys-fs/ddrescue
	sys-power/powernowd
	sys-power/powertop
	www-client/httrack
	x11-apps/mesa-progs
	x11-apps/xclock
	x11-apps/xhost
	x11-drivers/xf86-video-cirrus
	x11-libs/gksu
	x11-libs/vte
# keywords.
#	x11-misc/cairo-clock
#	x11-misc/grsync
	x11-plugins/pidgin-encryption
	x11-plugins/pidgin-extprefs
	x11-terms/xterm
	app-benchmarks/bonnie++
	app-benchmarks/dbench
	app-benchmarks/httperf
	app-benchmarks/iozone
	app-benchmarks/stress
	app-benchmarks/tiobench
	app-crypt/aespipe
	app-crypt/aesutil
# keywords.
#	app-crypt/gnupg-pkcs11-scd
	app-crypt/gpgme
	app-crypt/hashalot
# keywords.
#	app-crypt/luks-tools
	app-crypt/mcrypt
	app-crypt/md5deep
	app-editors/scite
	app-forensics/autopsy
	app-forensics/memdump
	app-forensics/sleuthkit
	app-text/agrep
	app-admin/hwreport
	app-arch/cabextract
	app-arch/cfv
# keywords.
#	app-arch/lzip
	app-arch/lzma-utils
	app-arch/p7zip
	app-arch/pbzip2
# keywords.
#	app-arch/pigz
	app-arch/xarchiver	
	app-arch/zip	
# keywords.
#	app-backup/tob
#	app-cdr/cdw
	app-cdr/xfburn
# keywords.
	app-crypt/pinentry
	app-editors/hexcurse
	app-editors/joe
	app-editors/qemacs
	app-editors/zile
	app-misc/beep
	app-misc/colordiff
	app-misc/emelfm2
	app-misc/symlinks
	app-shells/ksh
	app-text/dos2unix
	app-text/epdfview
	app-text/hunspell
	app-text/unix2dos
	dev-python/pexpect
	dev-python/py-gnupg
	dev-python/pylibacl
	dev-python/pyparted
	dev-python/pyxattr
	net-analyzer/arping
	net-analyzer/dnstracer
	net-analyzer/httping
	net-analyzer/ifstat
	net-analyzer/iftop
	net-analyzer/iptraf
	net-analyzer/macchanger
	net-analyzer/ngrep
	net-analyzer/vnstat
	net-dns/bind-tools
	net-dns/libidn
	net-ftp/ftp
	net-misc/curl
	net-misc/openvpn
	net-misc/rsync
	net-misc/telnet-bsd
	net-misc/udpcast
	net-misc/wput
	sys-apps/cciss_vol_status
	sys-apps/dcfldd
	sys-apps/diffutils	
	sys-apps/dmapi
	sys-apps/ed
	sys-apps/fbset
# keywords.
#	sys-apps/flashrom
	sys-apps/groff
	sys-apps/ipmitool
	sys-apps/kbd
	sys-apps/lshw
	sys-apps/pciutils
	sys-apps/pv
	sys-apps/ren
	sys-apps/rename
	sys-apps/rescan-scsi-bus
	sys-apps/setserial
# keywords AND license restricted. Must not be included in public media.
#	sys-block/lsiutil	
	sys-block/mbuffer
	sys-block/ms-sys
	sys-block/mtx
	sys-block/nbd
# keywords.
#	sys-fs/btrfs-progs
	sys-process/atop
	sys-process/iotop
	www-client/elinks
# keywords.
#	net-p2p/frostwire
	www-client/lynx
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
	#app-cdr/k3b
	app-cdr/nrg2iso
	app-crypt/gnupg
	app-editors/bluefish
	app-editors/emacs
	app-editors/gvim
	app-editors/vim
	app-editors/xemacs
	app-forensics/chkrootkit
	app-laptop/i8kutils
	app-misc/mc
	app-misc/pax-utils
	app-misc/screen
	app-misc/splitvt
	app-misc/vlock
	app-office/dia
	app-office/gnucash
	app-office/gnumeric
	app-office/openoffice-bin
	app-office/scribus
	app-pda/gtkpod
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
	app-text/wgetpaste
	dev-util/anjuta
	dev-util/ccache
	dev-util/cvs
	dev-util/git
	dev-util/indent
	dev-util/ltrace
	dev-util/strace
	dev-util/subversion
	dev-util/valgrind
	gnome-base/gdm
	gnome-extra/evolution-exchange
	gnome-extra/gsynaptics
	gnome-extra/sensors-applet
	mail-client/evolution
	mail-client/mozilla-thunderbird
	mail-client/sylpheed
	mail-client/claws-mail
	media-gfx/blender
	#media-gfx/digikam
	media-gfx/fbgrab
	media-gfx/gimp
	media-gfx/gtkam
	media-gfx/inkscape
	media-gfx/xsane
	media-sound/amarok
	media-sound/audacious
# fails because of expat libs
#	media-sound/audacity
	media-sound/easytag
	media-sound/gnomeradio
	media-sound/grip
	media-sound/hydrogen
	media-sound/rhythmbox
	media-video/gxine
	media-video/lsdvd
	media-video/mplayer
	media-video/ogle-gui
	media-video/vlc
	media-video/xine-ui
	media-video/smplayer
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
	net-dialup/pptpclient
	net-dialup/rp-pppoe
	net-firewall/iptables
	net-ftp/ncftp
	net-fs/mount-cifs
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
	net-print/cups
	net-proxy/dante
	net-proxy/ntlmaps
	net-proxy/tsocks
	net-wireless/aircrack-ng
	net-wireless/airsnort
### Masked by ~x86
#	net-wireless/b43-fwcutter
#	net-wireless/bcm43xx-fwcutter
	net-wireless/gnome-bluetooth
	net-wireless/ipw2100-firmware
	net-wireless/ipw2200-firmware
	net-wireless/iwl3945-ucode
	net-wireless/iwl4965-ucode
# failed to fetch
#	net-wireless/prism54-firmware
	net-wireless/wepattack
	net-wireless/wireless-tools
	net-wireless/wpa_supplicant
	net-wireless/zd1201-firmware
	net-wireless/zd1211-firmware
	rox-base/rox
	sys-apps/dmidecode
	sys-apps/eject
	sys-apps/ethtool
	sys-apps/fxload
	sys-apps/gradm
	sys-apps/hdparm
	sys-apps/hwsetup
	sys-apps/iproute2
	sys-apps/ivman
	sys-apps/memtester
	sys-apps/netplug
	sys-apps/parted
	sys-apps/pcsc-lite
	sys-apps/pmount
	sys-apps/qtparted
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
	sys-boot/grub
	sys-boot/lilo
	sys-boot/syslinux
	sys-devel/distcc
	sys-devel/gdb
	sys-fs/dmraid
	sys-fs/dosfstools
	sys-fs/e2fsprogs
	sys-fs/evms
	sys-fs/hfsplusutils
	sys-fs/hfsutils
	sys-fs/jfsutils
	sys-fs/lsscsi
	sys-fs/lvm2
	sys-fs/mac-fdisk
	sys-fs/mdadm
	sys-fs/ntfsprogs
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
	www-client/mozilla-firefox
	www-client/opera
	www-client/seamonkey
	x11-base/xorg-x11
	x11-drivers/xf86-input-synaptics
	x11-misc/xscreensaver
### Masked (no stable keywords)
#	x11-plugins/gkrellm-plugins
	x11-themes/gdm-themes-livecd
	x11-themes/gentoo-artwork-livecd
	x11-wm/afterstep
	x11-wm/enlightenment
	x11-wm/fluxbox
	x11-wm/windowmaker
	x11-wm/openbox
	xfce-base/xfce4-meta
