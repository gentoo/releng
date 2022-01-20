subarch: ppc64le
version_stamp: @TIMESTAMP@
target: livecd-stage1
rel_type: default
profile: default/linux/ppc64le/17.0
snapshot: @TIMESTAMP@
source_subpath: default/stage3-ppc64le-openrc-@TIMESTAMP@
compression_mode: pixz
portage_confdir: @REPO_DIR@/releases/portage/isos

livecd/use:
	-introspection
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
	symlink
	unicode
	xml

livecd/packages:
	app-accessibility/brltty
	app-admin/pwgen
	app-admin/syslog-ng
	app-arch/lbzip2
	app-arch/pigz
	app-arch/unzip
	app-arch/zstd
	app-crypt/gnupg
	app-misc/livecd-tools
	app-misc/screen
	app-misc/tmux
	app-portage/mirrorselect
	app-text/wgetpaste
	net-analyzer/tcptraceroute
	net-analyzer/traceroute
	net-dialup/mingetty
	net-dialup/pptpclient
	net-dialup/rp-pppoe
	net-fs/cifs-utils
	net-fs/nfs-utils
	net-irc/irssi
	net-irc/weechat
	net-misc/dhcpcd
	net-misc/iputils
	net-misc/ntp
	net-misc/openssh
	net-misc/rdate
	net-misc/rsync
	net-wireless/iw
	net-wireless/iwd
	net-wireless/wireless-tools
	net-wireless/wpa_supplicant
	sys-apps/busybox
	sys-apps/ethtool
	sys-apps/fxload
	sys-apps/gptfdisk
	sys-apps/hdparm
	sys-apps/ibm-powerpc-utils
	sys-apps/iproute2
	sys-apps/lm-sensors
	sys-apps/lsvpd
	sys-apps/memtester
	sys-apps/nvme-cli
	sys-apps/opal-utils
	sys-apps/sdparm
	sys-apps/usbutils
	sys-block/parted
	sys-boot/grub
	sys-fs/bcache-tools
	sys-fs/btrfs-progs
	sys-fs/cryptsetup
	sys-fs/dosfstools
	sys-fs/e2fsprogs
	sys-fs/f2fs-tools
	sys-fs/hfsplusutils
	sys-fs/hfsutils
	sys-fs/iprutils
	sys-fs/jfsutils
	sys-fs/lsscsi
	sys-fs/lvm2
	sys-fs/mdadm
	sys-fs/ntfs3g
	sys-fs/reiserfsprogs
	sys-fs/squashfs-tools
	sys-fs/xfsprogs
	sys-kernel/linux-firmware
	sys-libs/gpm
	www-client/links
