subarch: amd64
target: stage4
version_stamp: musl-hardened-MY_DATE
rel_type: musl/hardened/amd64
profile: hardened/linux/musl/amd64
snapshot: current
source_subpath: musl/hardened/amd64/stage3-amd64-musl-hardened
portage_confdir: @REPO_DIR@/portage.amd64.hardened-stage4
portage_overlay: /opt/overlays/musl

stage4/use:
	bash-completion
	bindist
	bzip2
	idm
	ipv6
	mmx
	sse
	sse2
	urandom

stage4/packages:
	app-admin/syslog-ng
	dev-util/pkgconf
	net-misc/dhcpcd
	sys-apps/iproute2
	sys-devel/bc
	sys-power/acpid
	sys-process/cronie
stage4/fsscript: @REPO_DIR@/stage4-fsscript.sh
stage4/rcadd:
	acpid|default
	cronie|default
	dhcpcd|default
	net.lo|default
	netmount|default
	sshd|default
	syslog-ng|default

boot/kernel: gentoo
boot/kernel/gentoo/sources: gentoo-sources
boot/kernel/gentoo/config: @REPO_DIR@/../releases/weekly/kconfig/amd64/cloud-amd64-gentoo.config
boot/kernel/gentoo/extraversion: openstack
boot/kernel/gentoo/gk_kernargs: --all-ramdisk-modules --no-nfs --makeopts=-j4

stage4/empty:
	/root/.ccache
	/tmp
	/usr/portage/distfiles
	/usr/src
	/var/cache
	/var/empty
	/var/run
	/var/state
	/var/tmp

stage4/rm:
	/boot/System.map-genkernel*
	/etc/*-
	/etc/*.old
	/etc/ssh/ssh_host_*
	/root/.*history
	/root/.lesshst
	/root/.ssh/known_hosts
	/root/.viminfo
	# Remove any generated stuff by genkernel
	/usr/share/genkernel
	# This is 3MB of crap for each copy
	/usr/lib64/python*/site-packages/gentoolkit/test/eclean/testdistfiles.tar.gz
