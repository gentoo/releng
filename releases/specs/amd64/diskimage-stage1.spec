subarch: amd64
version_stamp: @TIMESTAMP@
target: diskimage-stage1
rel_type: 23.0-default
profile: default/linux/amd64/23.0/no-multilib/systemd
snapshot_treeish: @TREEISH@
source_subpath: 23.0-default/stage3-amd64-nomultilib-systemd-@TIMESTAMP@
compression_mode: pixz
portage_confdir: @REPO_DIR@/releases/portage/isos

diskimage/use:
	compile-locales
	lvm

diskimage/packages:
	app-admin/pwgen
	app-arch/unzip
	app-crypt/gnupg
	app-editors/nano
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
	sys-apps/kexec-tools
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
