subarch: amd64
version_stamp: @TIMESTAMP@
target: livecd-stage2
rel_type: 23.0-default
profile: default/linux/amd64/23.0/no-multilib
snapshot_treeish: @TREEISH@
source_subpath: 23.0-default/livecd-stage1-amd64-@TIMESTAMP@
portage_confdir: @REPO_DIR@/releases/portage/isos

livecd/bootargs: dokeymap nodhcp
livecd/fstype: squashfs
livecd/iso: install-amd64-minimal-@TIMESTAMP@.iso
livecd/type: gentoo-release-minimal
livecd/volid: Gentoo-amd64-@DATESTAMP@

livecd/rcadd: dbus|default gpm|default NetworkManager|default

boot/kernel: gentoo

boot/kernel/gentoo/distkernel: yes
boot/kernel/gentoo/dracut_args: --xz --no-hostonly -a dmsquash-live -a mdraid -o btrfs -o crypt -o i18n -o usrmount -o lunmask -o qemu -o qemu-net -o nvdimm -o multipath -i /lib/keymaps /lib/keymaps -I busybox
boot/kernel/gentoo/config: @REPO_DIR@/releases/kconfig/amd64/dist-amd64-livecd.config
boot/kernel/gentoo/packages: --usepkg n net-wireless/broadcom-sta sys-fs/zfs

livecd/unmerge:
        app-admin/eselect-ctags
        app-admin/eselect-vi
        app-admin/perl-cleaner
        app-admin/python-updater
        app-arch/cpio
	app-portage/gentoolkit
        dev-build/libtool
        dev-libs/gmp
        dev-libs/libxml2
        dev-libs/mpfr
        dev-python/pycrypto
        dev-util/pkgconf
        perl-core/PodParser
        perl-core/Test-Harness
        sys-apps/debianutils
        sys-apps/diffutils
        sys-apps/file
        sys-apps/groff
        sys-apps/man-db
        sys-apps/man-pages
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
        sys-kernel/linux-headers
	sys-kernel/gentoo-kernel

livecd/empty:
	/boot
	/etc/cron.daily
	/etc/cron.hourly
	/etc/cron.monthly
	/etc/cron.weekly
	/etc/logrotate.d
	/etc/modules.autoload.d
	/etc/runlevels/single
	/etc/skel
	/usr/lib/dev-state
	/usr/lib/udev-state
	/usr/lib64/dev-state
	/usr/lib64/udev-state
	/root/.ccache
	/tmp
	/usr/diet/include
	/usr/diet/man
	/usr/include
	/usr/i386-gentoo-linux-uclibc
	/usr/i386-pc-linux-gnu
	/usr/i386-pc-linux-uclibc
	/usr/lib/X11/config
	/usr/lib/X11/doc
	/usr/lib/X11/etc
	/usr/lib/awk
	/usr/lib/ccache
	/usr/lib/gcc-config
	/usr/lib/nfs
	/usr/lib/perl5/site_perl
	/usr/lib/portage
	/usr/lib64/X11/config
	/usr/lib64/X11/doc
	/usr/lib64/X11/etc
	/usr/lib64/awk
	/usr/lib64/ccache
	/usr/lib64/gcc-config
	/usr/lib64/nfs
	/usr/lib64/perl5/site_perl
	/usr/lib64/portage
	/usr/local
	/usr/portage
	/usr/powerpc-unknown-linux-gnu
	/usr/powerpc64-unknown-linux-gnu
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
	/usr/share/genkernel
	/usr/share/gettext
	/usr/share/glib-2.0
	/usr/share/gnuconfig
	/usr/share/gtk-doc
	/usr/share/i18n
	/usr/share/info
	/usr/share/lcms
	/usr/share/libtool
	/usr/share/locale
	/usr/share/man
	/usr/share/rfc
	/usr/share/ss
	/usr/share/state
	/usr/share/texinfo
	/usr/share/unimaps
	/usr/share/zoneinfo
	/usr/sparc-unknown-linux-gnu
	/usr/src
	/usr/x86_64-pc-linux-gnu
	/var/cache
	/var/empty
	/var/lib/portage
	/var/log
	/var/spool
	/var/state
	/var/tmp

livecd/rm:
	/boot/System*
	/boot/initr*
	/boot/kernel*
	/etc/*-
	/etc/*.old
	/etc/default/audioctl
	/etc/dispatch-conf.conf
	/etc/env.d/05binutils
	/etc/env.d/05gcc
	/etc/etc-update.conf
	/etc/hosts.bck
	/etc/issue*
	/etc/genkernel.conf
	/etc/portage/make.conf*
	/etc//portage/make.globals
	/etc/portage/make.profile
	/etc/man.conf
	/etc/resolv.conf
	/usr/lib*/*.a
	/usr/lib*/*.la
	/usr/lib*/cpp
	/root/.bash_history
	/root/.viminfo
	/usr/bin/*.static
	/usr/bin/fsck.cramfs
	/usr/bin/fsck.minix
	/usr/bin/mkfs.bfs
	/usr/bin/mkfs.cramfs
	/usr/bin/mkfs.minix
	/usr/bin/addr2line
	/usr/bin/ar
	/usr/bin/as
	/usr/bin/audioctl
	/usr/bin/c++*
	/usr/bin/cc
	/usr/bin/cjpeg
	/usr/bin/cpp
	/usr/bin/djpeg
	/usr/bin/ebuild
	/usr/bin/egencache
	/usr/bin/emerge
	/usr/bin/emerge-webrsync
	/usr/bin/emirrordist
	/usr/bin/elftoaout
	/usr/bin/f77
	/usr/bin/g++*
	/usr/bin/g77
	/usr/bin/gcc*
	/usr/bin/genkernel
	/usr/bin/gprof
	/usr/bin/i386-pc-linux-*
	/usr/bin/jpegtran
	/usr/bin/ld
	/usr/bin/libpng*
	/usr/bin/nm
	/usr/bin/objcopy
	/usr/bin/objdump
	/usr/bin/piggyback*
	/usr/bin/portageq
	/usr/bin/ranlib
	/usr/bin/readelf
	/usr/bin/size
	/usr/bin/powerpc-unknown-linux-gnu-*
	/usr/bin/powerpc64-unknown-linux-gnu-*
	/usr/bin/sparc-unknown-linux-gnu-*
	/usr/bin/sparc64-unknown-linux-gnu-*
	/usr/bin/strings
	/usr/bin/strip
	/usr/bin/tbz2tool
	/usr/bin/x86_64-pc-linux-gnu-*
	/usr/bin/xpak
	/usr/bin/yacc
	/usr/lib*/*.a
	/usr/lib*/*.la
	/usr/lib*/perl5/site_perl
	/usr/lib*/gcc-lib/*/*/libgcj*
	/usr/bin/archive-conf
	/usr/bin/dispatch-conf
	/usr/bin/emaint
	/usr/bin/env-update
	/usr/bin/etc-update
	/usr/bin/fb*
	/usr/bin/fixpackages
	/usr/bin/quickpkg
	/usr/bin/regenworld
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
