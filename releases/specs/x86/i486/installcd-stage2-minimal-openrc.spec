subarch: i486
version_stamp: openrc-@TIMESTAMP@
target: livecd-stage2
rel_type: 23.0-default
profile: default/linux/x86/23.0/i486
snapshot_treeish: @TREEISH@
source_subpath: 23.0-default/livecd-stage1-i486-openrc-@TIMESTAMP@
portage_confdir: @REPO_DIR@/releases/portage/isos-x86

livecd/bootargs: dokeymap nodhcp
#livecd/cdtar: /usr/share/catalyst/livecd/cdtar/isolinux-elilo-memtest86+-cdtar.tar.bz2
livecd/fstype: squashfs
livecd/iso: install-x86-minimal-@TIMESTAMP@.iso
livecd/type: gentoo-release-minimal
livecd/volid: Gentoo-x86-@DATESTAMP@

livecd/rcadd: dbus|default gpm|default NetworkManager|default

boot/kernel: gentoo

boot/kernel/gentoo/distkernel: yes
boot/kernel/gentoo/dracut_args: --xz --no-hostonly -a dmsquash-live -a mdraid -o btrfs -o crypt -o i18n -o usrmount -o lunmask -o qemu -o qemu-net -o nvdimm -o multipath -o modsign -o net-lib -o bcache -o dmraid -o lvm -o resume -o virtiofs -o mdraid -o shutdown -o kernel-modules-extra -o shutdown  -o pcmcia -o hwdb -i /lib/keymaps /lib/keymaps -I busybox
boot/kernel/gentoo/config: @REPO_DIR@/releases/kconfig/x86/dist-x86-livecd.config
boot/kernel/gentoo/packages: --usepkg n broadcom-sta

livecd/unmerge:
	app-admin/eselect-ctags
	app-admin/eselect-vi
	app-admin/perl-cleaner
	app-admin/python-updater
	app-arch/cpio
	app-portage/gentoolkit
	dev-build/cmake
	dev-build/libtool
	dev-lang/rust-bin
	dev-libs/gmp
	dev-libs/libxml2
	dev-libs/mpfr
	dev-python/pycrypto
	perl-core/PodParser
	perl-core/Test-Harness
	sys-apps/debianutils
	sys-apps/diffutils
	sys-apps/groff
	sys-apps/man-db
	sys-apps/man-pages
	sys-apps/memtest86+
	sys-apps/miscfiles
	sys-apps/sandbox
	sys-apps/texinfo
	dev-build/autoconf
	dev-build/autoconf-wrapper
	dev-build/automake
	dev-build/automake-wrapper
	sys-devel/binutils
	sys-devel/binutils-config
	sys-devel/bison
	sys-devel/flex
	sys-devel/gcc
	sys-devel/gcc-config
	sys-devel/gettext
	sys-devel/gnuconfig
	sys-devel/m4
	dev-build/make
	sys-devel/patch
	sys-libs/db
	sys-libs/gdbm
	sys-kernel/dracut
	sys-kernel/gentoo-kernel
	sys-kernel/linux-headers


livecd/empty:
	/boot
	/etc/cron.daily
	/etc/cron.hourly
	/etc/cron.monthly
	/etc/cron.weekly
	/etc/kernel/config.d
	/etc/logrotate.d
	/etc/modules.autoload.d
	/etc/rsync
	/etc/runlevels/single
	/etc/skel
	/root/.ccache
	/tmp
	/usr/include
	/usr/local
	/usr/share/aclocal
	/usr/share/baselayout
	/usr/share/binutils-data
	/usr/share/consolefonts/partialfonts
	/usr/share/consoletrans
	/usr/share/dict
	/usr/share/doc
	/usr/share/emacs
	/usr/share/et
	/usr/share/gcc-data
	/usr/share/gettext
	/usr/share/glib-2.0
	/usr/share/gnuconfig
	/usr/share/gtk-doc
	/usr/share/i18n
	/usr/share/info
	/usr/share/lcms
	/usr/share/libtool
	/usr/share/man
	/usr/share/rfc
	/usr/share/ss
	/usr/share/state
	/usr/share/texinfo
	/usr/share/unimaps
	/usr/share/zoneinfo
	/usr/src
	/var/cache
	/var/empty
	/var/lib/portage
	/var/log
	/var/spool
	/var/state
	/var/tmp

livecd/rm:
	/etc/*-
	/etc/*.old
	/etc/default/audioctl
	/etc/dispatch-conf.conf
	/etc/etc-update.conf
	/etc/hosts.bck
	/etc/issue*
	/etc/man.conf
	/etc/resolv.conf
	/root/.bash_history
	/root/.viminfo
	/usr/bin/*.static
	/usr/bin/fsck.cramfs
	/usr/bin/fsck.minix
	/usr/bin/mkfs.bfs
	/usr/bin/mkfs.cramfs
	/usr/bin/mkfs.minix
	/usr/bin/addr2line
	/usr/share/consolefonts/1*
	/usr/share/consolefonts/7*
	/usr/share/consolefonts/8*
	/usr/share/consolefonts/9*
	/usr/share/consolefonts/A*
	/usr/share/consolefonts/C*
	/usr/share/consolefonts/E*
	/usr/share/consolefonts/G*
	/usr/share/consolefonts/L*
	/usr/share/consolefonts/M*
	/usr/share/consolefonts/R*
	/usr/share/consolefonts/a*
	/usr/share/consolefonts/c*
	/usr/share/consolefonts/dr*
	/usr/share/consolefonts/g*
	/usr/share/consolefonts/i*
	/usr/share/consolefonts/k*
	/usr/share/consolefonts/l*
	/usr/share/consolefonts/r*
	/usr/share/consolefonts/s*
	/usr/share/consolefonts/t*
	/usr/share/consolefonts/v*
	/usr/share/misc/*.old
