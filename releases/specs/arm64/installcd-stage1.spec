subarch: arm64
target: livecd-stage1
version_stamp: @TIMESTAMP@
rel_type: default
profile: default/linux/arm64/17.0
snapshot: @TIMESTAMP@
source_subpath: default/stage3-arm64-@TIMESTAMP@
compression_mode: pixz_x
portage_confdir: @REPO_DIR@/releases/portage/isos

livecd/use:
	alsa
	compile-locales
	fbcon
	ipv6
	livecd
	modules
	ncurses
	nls
	nptl
	pam
	portaudio
	readline
	socks5
	ssl
	static-libs
	unicode
	xml

livecd/packages:
	app-accessibility/brltty
	#app-accessibility/espeakup # needs keywording
	#app-admin/hddtemp # needs stable
	#app-admin/pwgen # needs stable
	app-admin/syslog-ng
	app-arch/unzip
	app-crypt/gnupg
	#app-editors/mg # needs keywording
	app-editors/nano
	app-misc/livecd-tools
	app-misc/screen
	app-misc/tmux
	app-portage/mirrorselect
	app-text/wgetpaste
	#media-gfx/fbgrab # needs stable
	media-sound/alsa-utils
	net-analyzer/traceroute
	net-dialup/mingetty
	net-dialup/pptpclient
	#net-dialup/rp-pppoe # needs stable
	net-fs/cifs-utils
	net-fs/nfs-utils
	#net-irc/irssi # needs stable
	net-misc/dhcpcd
	net-misc/iputils
	#net-misc/ndisc6 # needs stable
	net-misc/ntp
	net-misc/openssh
	#net-misc/rdate # needs stable
	net-misc/rsync
	#net-misc/vconfig # needs keywording
	net-proxy/dante
	#net-proxy/tsocks # needs keywording
	#net-wireless/b43-fwcutter # needs stable
	net-wireless/iw
	net-wireless/wireless-tools
	net-wireless/wpa_supplicant
	sys-apps/busybox
	sys-apps/dmidecode
	sys-apps/ethtool
	#sys-apps/fxload # needs keywording
	sys-apps/gptfdisk
	sys-apps/hdparm
	sys-apps/iproute2
	#sys-apps/memtester # needs keywording
	#sys-apps/netplug # needs keywording
	sys-apps/nvme-cli
	sys-apps/pciutils
	#sys-apps/pcmciautils # needs keywording
	#sys-apps/sdparm # needs keywording
	sys-apps/usbutils
	sys-block/parted
	#sys-block/partimage # needs keywording
	#sys-firmware/ipw2100-firmware # needs keywording
	#sys-firmware/ipw2200-firmware # needs keywording
	sys-fs/btrfs-progs
	sys-fs/cryptsetup
	#sys-fs/dmraid # needs stable
	sys-fs/dosfstools
	sys-fs/e2fsprogs
	sys-fs/f2fs-tools
	#sys-fs/jfsutils # needs stable
	sys-fs/lsscsi
	sys-fs/lvm2
	#sys-fs/mac-fdisk # not needed?
	#sys-fs/mdadm # needs stable
	sys-fs/multipath-tools
	#sys-fs/ntfs3g # needs stable
	#sys-fs/reiserfsprogs # needs stable
	sys-fs/xfsprogs
	sys-kernel/linux-firmware
	sys-libs/gpm
	sys-power/acpid
	www-client/links
