subarch: amd64
target: stage4
version_stamp: cloud-nomultilib-latest
rel_type: default
profile: default/linux/amd64/13.0/no-multilib
snapshot: latest
source_subpath: default/stage3-amd64-nomultilib-latest
portage_confdir: /release/releng/releases/weekly/portage/cloud-stages

stage4/use:
	bash-completion
	bzip2
	idm
	ipv6
	mmx
	sse
	sse2
	urandom

stage4/packages:
	app-admin/logrotate
	app-admin/sudo
	app-admin/syslog-ng
	app-editors/vim
	app-emulation/cloud-init
	app-portage/eix
	app-portage/gentoolkit
	net-misc/dhcpcd
	sys-boot/grub
	sys-apps/dmidecode
	sys-apps/gptfdisk
	sys-apps/iproute2
	sys-apps/lsb-release
	sys-apps/pciutils
	sys-block/parted
	sys-devel/bc
	sys-power/acpid
	sys-process/cronie
stage4/fsscript: /release/releng/releases/weekly/scripts/cloud-prep.sh
stage4/root_overlay: /release/releng/releases/weekly/overlays/cloud-overlay
stage4/rcadd:
	acpid|default
	cloud-config|default
	cloud-final|default
	cloud-init-local|default
	cloud-init|default
	cronie|default
	dhcpcd|default
	net.lo|default
	netmount|default
	sshd|default
	syslog-ng|default

boot/kernel: gentoo
boot/kernel/gentoo/sources: gentoo-sources
boot/kernel/gentoo/config: /release/releng/releases/weekly/kconfig/amd64/installcd-3.18.12.config
boot/kernel/gentoo/extraversion: openstack
boot/kernel/gentoo/gk_kernargs: --all-ramdisk-modules
