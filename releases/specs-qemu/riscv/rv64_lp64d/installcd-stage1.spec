subarch: rv64_lp64d
target: livecd-stage1
version_stamp: @TIMESTAMP@
rel_type: 23.0-default
profile: default/linux/riscv/23.0/rv64/lp64d
snapshot_treeish: @TREEISH@
source_subpath: 23.0-default/stage3-rv64_lp64d-openrc-@TIMESTAMP@
compression_mode: pixz
portage_confdir: @REPO_DIR@/releases/portage/isos-qemu
interpreter: /usr/bin/qemu-riscv64
decompressor_search_order: xz bzip2

livecd/use:
	alsa
	compile-locales
	fbcon
	livecd
	portaudio
	socks5
	unicode
	xml

livecd/packages:
	app-accessibility/brltty
	app-accessibility/espeakup
	app-admin/hddtemp
	app-admin/pwgen
	app-admin/syslog-ng
	app-arch/unzip
	app-crypt/gnupg
	app-editors/mg
	app-editors/nano
	app-misc/livecd-tools
	app-misc/screen
	app-misc/tmux
	app-portage/gentoolkit
	app-portage/mirrorselect
	app-shells/bash-completion
	app-shells/gentoo-bashcomp
	app-text/wgetpaste
	dev-embedded/u-boot-tools
	media-gfx/fbgrab
	media-sound/alsa-utils
	net-analyzer/traceroute
	net-dialup/mingetty
	net-dialup/pptpclient
	net-dialup/rp-pppoe
	net-fs/cifs-utils
	net-fs/nfs-utils
	net-irc/irssi
	net-misc/chrony
	net-misc/dhcpcd
	net-misc/iputils
	net-misc/ndisc6
	net-misc/openssh
	net-misc/rdate
	net-misc/rsync
	net-misc/vconfig
	net-proxy/dante
	net-wireless/iw
	net-wireless/wireless-tools
	net-wireless/wpa_supplicant
	sys-apps/arch-chroot
	sys-apps/busybox
	sys-apps/dmidecode
	sys-apps/ethtool
	sys-apps/fxload
	sys-apps/gptfdisk
	sys-apps/hdparm
	sys-apps/iproute2
	sys-apps/memtester
	sys-apps/merge-usr
	sys-apps/netplug
	sys-apps/nvme-cli
	sys-apps/pciutils
	sys-apps/pv
	sys-apps/pcmciautils
	sys-apps/sdparm
	sys-apps/usbutils
	sys-auth/ssh-import-id
	sys-block/parted
	sys-block/partimage
	sys-firmware/ipw2100-firmware
	sys-firmware/ipw2200-firmware
	sys-fs/bcache-tools
	sys-fs/btrfs-progs
	sys-fs/cryptsetup
	sys-fs/dmraid
	sys-fs/dosfstools
	sys-fs/e2fsprogs
	sys-fs/f2fs-tools
	sys-fs/genfstab
	sys-fs/lsscsi
	sys-fs/lvm2
	sys-fs/mdadm
	sys-fs/multipath-tools
	sys-fs/ntfs3g
	sys-fs/xfsdump
	sys-fs/xfsprogs
	sys-kernel/linux-firmware
	sys-libs/gpm
	sys-power/acpid
	www-client/links
