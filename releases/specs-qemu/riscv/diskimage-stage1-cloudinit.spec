subarch: rv64_lp64d
version_stamp: cloudinit-@TIMESTAMP@
target: diskimage-stage1
interpreter: /usr/bin/qemu-riscv64
rel_type: 23.0-default
profile: default/linux/riscv/23.0/rv64/lp64d/systemd
snapshot_treeish: @TREEISH@
source_subpath: 23.0-default/stage3-rv64_lp64d-systemd-@TIMESTAMP@
compression_mode: pixz
portage_confdir: @REPO_DIR@/releases/portage/diskimage-qemu

diskimage/use:
	compile-locales
	lvm

diskimage/packages:
	app-admin/pwgen
	app-admin/sudo
	app-arch/unzip
	app-crypt/gnupg
	app-editors/nano
	app-emulation/cloud-init
	app-misc/screen
	app-portage/cpuid2cpuflags
	app-portage/gentoolkit
	app-portage/mirrorselect
	app-text/wgetpaste
	net-analyzer/traceroute
	net-irc/irssi
	net-misc/iputils
	net-misc/openssh
	net-misc/rsync
	sys-apps/busybox
	sys-apps/gptfdisk
	sys-apps/iproute2
	sys-apps/kbd
	sys-apps/nvme-cli
	sys-apps/pciutils
	sys-apps/pv
	sys-apps/usbutils
	sys-auth/ssh-import-id
	sys-block/parted
	sys-boot/grub
	sys-fs/cryptsetup
	sys-fs/dmraid
	sys-fs/dosfstools
	sys-fs/e2fsprogs
	sys-fs/lvm2
	sys-fs/mdadm
	sys-fs/multipath-tools
	sys-fs/xfsdump
	sys-fs/xfsprogs
	sys-kernel/linux-firmware
	#force rebuild for USE="(-multilib*)"
	sys-libs/glibc
