subarch: alpha
version_stamp: 2008.0
target: livecd-stage2
rel_type: default
profile: default/linux/alpha/13.0
snapshot: 2008.0
source_subpath: default/livecd-stage1-alpha-2008.0

livecd/bootargs: dokeymap
livecd/cdtar: /space/armin76/tmp/aboot-1.0_pre20040408-r2-cdtar-weekly.tar.bz2
livecd/fsscript: /space/armin76/releng/releases/weekly/scripts/livecd.sh
livecd/fstype: squashfs
livecd/gk_mainargs: --lvm --dmraid --mdadm
livecd/iso: /space/catalyst/builds/default/install-alpha-minimal-2008.0.iso
livecd/type: gentoo-release-minimal
livecd/volid: Gentoo Linux alpha 2008.0

boot/kernel: gentoo gentoo_nolsa

boot/kernel/gentoo/sources: gentoo-sources
boot/kernel/gentoo/config: ../../kconfig/alpha/installcd-3.8.13.config
boot/kernel/gentoo/use:
	-*
	atm
	deprecated
	fbcon
	fbcondecor
	ipv6
	livecd
	loop-aes
	lvm1
	mng
	ncurses
	nls
	nptl
	nptlonly
	pam
	png
	readline
	socks5
	ssl
	truetype
	unicode
	usb

boot/kernel/gentoo_nolsa/sources: gentoo-sources
boot/kernel/gentoo_nolsa/config: ../../kconfig/alpha/installcd-3.8.13.nolsa.config
boot/kernel/gentoo_nolsa/use:
	-*
	atm
	deprecated
	fbcon
	fbcondecor
	ipv6
	livecd
	loop-aes
	lvm1
	mng
	ncurses
	nls
	nptl
	nptlonly
	pam
	png
	readline
	socks5
	ssl
	truetype
	unicode
	usb

# Not keyworded on alpha
#boot/kernel/gentoo/packages:
#	sys-fs/ntfs3g

livecd/unmerge:
	app-admin/eselect
	app-admin/eselect-ctags
	app-admin/eselect-vi
	app-admin/perl-cleaner
	app-admin/python-updater
	app-arch/cpio
	dev-libs/gmp
	dev-libs/libxml2
	dev-libs/mpfr
#	dev-libs/popt
	dev-python/pycrypto
	dev-util/pkgconfig
#	net-misc/rsync
	perl-core/PodParser
	perl-core/Test-Harness
	sys-apps/debianutils
	sys-apps/diffutils
	sys-apps/file
	sys-apps/groff
	sys-apps/man
	sys-apps/man-pages
	sys-apps/miscfiles
#	sys-apps/portage
#	sys-apps/sandbox
	sys-apps/texinfo
	sys-devel/autoconf
	sys-devel/autoconf-wrapper
	sys-devel/automake
	sys-devel/automake-wrapper
	sys-devel/binutils
	sys-devel/binutils-config
	sys-devel/bison
	sys-devel/flex
	sys-devel/gcc
	sys-devel/gcc-config
	sys-devel/gettext
	sys-devel/gnuconfig
	sys-devel/libtool
	sys-devel/m4
	sys-devel/make
	sys-devel/patch
	sys-libs/db
	sys-libs/gdbm
	sys-libs/libkudzu
	sys-kernel/genkernel
	sys-kernel/linux-headers

livecd/empty:
	/etc/cron.daily
	/etc/cron.hourly
	/etc/cron.monthly
	/etc/cron.weekly
	/etc/logrotate.d
	/etc/modules.autoload.d
#	/etc/rsync
	/etc/runlevels/single
	/etc/skel
	/lib/dev-state
	/lib/udev-state
	/lib64/dev-state
	/lib64/udev-state
	/root/.ccache
	/tmp
	/usr/diet/include
	/usr/diet/man
	/usr/i386-gentoo-linux-uclibc
	/usr/i386-pc-linux-gnu
	/usr/i386-pc-linux-uclibc
	/usr/lib/X11/config
	/usr/lib/X11/doc
	/usr/lib/X11/etc
	/usr/lib/awk
	/usr/lib/ccache
	/usr/lib/gcc-config
	/usr/lib/gconv
	/usr/lib/nfs
	/usr/lib/perl5/site_perl
	/usr/lib/portage
	/usr/lib/python2.2
	/usr/lib/python2.3
	/usr/lib/python2.4/test
	/usr/lib64/X11/config
	/usr/lib64/X11/doc
	/usr/lib64/X11/etc
	/usr/lib64/awk
	/usr/lib64/ccache
	/usr/lib64/gcc-config
	/usr/lib64/gconv
	/usr/lib64/nfs
	/usr/lib64/perl5/site_perl
	/usr/lib64/portage
	/usr/lib64/python2.2
	/usr/lib64/python2.3
	/usr/lib64/python2.4/test
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
	/etc/make.conf*
	/etc/make.globals
	/etc/make.profile
	/etc/man.conf
	/etc/resolv.conf
	/lib*/*.a
	/lib*/*.la
	/lib*/cpp
	/root/.bash_history
	/root/.viminfo
	/sbin/*.static
	/sbin/fsck.cramfs
	/sbin/fsck.minix
	/sbin/mkfs.bfs
	/sbin/mkfs.cramfs
	/sbin/mkfs.minix
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
	/usr/bin/emerge
	/usr/bin/elftoaout
	/usr/bin/f77
	/usr/bin/g++*
	/usr/bin/g77
	/usr/bin/gcc*
	/usr/bin/genkernel
	/usr/bin/gprof
	/usr/bin/i386-gentoo-linux-uclibc-*
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
	/usr/bin/repoman
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
	/usr/sbin/archive-conf
	/usr/sbin/dispatch-conf
	/usr/sbin/emaint
	/usr/sbin/emerge-webrsync
	/usr/sbin/env-update
	/usr/sbin/fb*
	/usr/sbin/fixpackages
	/usr/sbin/quickpkg
	/usr/sbin/regenworld
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
