subarch: hppa1.1
version_stamp: @TIMESTAMP@
target: livecd-stage2
rel_type: default
profile: default/linux/hppa/17.0
snapshot: @TIMESTAMP@
source_subpath: default/livecd-stage1-hppa1.1-@TIMESTAMP@
pkgcache_path: /var/tmp/catalyst/packages/default/installcd-stage2
portage_confdir: @REPO_DIR@/releases/portage/isos

livecd/volid: Gentoo hppa @TIMESTAMP@
livecd/bootargs: dokeymap
livecd/fstype: squashfs
livecd/iso: /var/tmp/catalyst/builds/default/install-hppa-minimal-@TIMESTAMP@.iso
livecd/type: gentoo-release-minimal

boot/kernel: livecd32 livecd64

# On hppa, kernelopts are common for all kernel and will be applied to both
boot/kernel/livecd32/kernelopts: panic=30

boot/kernel/livecd32/sources: sys-kernel/gentoo-sources
boot/kernel/livecd32/config: /home/gmsoft/specs/installcd-3.10.7-gentoo-livecd32.config
boot/kernel/livecd32/use:
	-*
	atm
	fbcon
	ipv6
	livecd
	ncurses
	nls
	nptl
	pam
	png
	readline
	socks5
	ssl
	truetype
	unicode
	usb

boot/kernel/livecd64/sources: sys-kernel/gentoo-sources
boot/kernel/livecd64/config: /home/gmsoft/specs/installcd-3.10.7-gentoo-livecd64.config
boot/kernel/livecd64/gk_kernargs: --cross-compile=hppa64-unknown-linux-gnu
boot/kernel/livecd64/use:
	-*
	atm
	fbcon
	ipv6
	livecd
	ncurses
	nls
	nptl
	pam
	png
	readline
	socks5
	ssl
	truetype
	unicode
	usb

boot/kernel/livecd32/extraversion: livecd32
boot/kernel/livecd64/extraversion: livecd64

livecd/unmerge:
	app-admin/eselect
	app-admin/eselect-lib-bin-symlink
	app-admin/eselect-pinentry
	app-admin/eselect-python
	app-admin/perl-cleaner
	app-admin/python-updater
	app-arch/cpio
	app-crypt/gnupg
	app-crypt/pinentry
	app-portage/portage-utils
	dev-libs/gmp
	app-text/build-docbook-catalog
	app-text/docbook-xml-dtd
	app-text/docbook-xsl-stylesheets
	app-text/openjade
	app-text/opensp
	app-text/po4a
	app-text/sgml-common
	dev-libs/elfutils
	dev-libs/eventlog
	dev-libs/libassuan
	dev-libs/pth
	dev-libs/libgpg-error
	dev-libs/libksba
	dev-libs/libpipeline
	dev-libs/libxml2
	dev-libs/libxslt
	dev-libs/mpc
	dev-libs/mpfr
	dev-libs/popt
	dev-util/gtk-doc-am
	dev-util/intltool
	dev-util/pkgconfig
	net-misc/netifrc
	net-misc/rsync
	perl-core/PodParser
	perl-core/Test-Harness
	sys-apps/debianutils
	sys-apps/diffutils
	sys-apps/groff
	sys-apps/help2man
	sys-apps/man-db
	sys-apps/sandbox
	sys-apps/tcp-wrappers
	sys-apps/texinfo
	sys-boot/palo
	sys-apps/miscfiles
	sys-devel/autoconf
	sys-devel/autoconf-wrapper
	sys-devel/automake
	sys-devel/automake-wrapper
	sys-devel/binutils
	sys-devel/binutils-hppa64
	sys-devel/binutils-config
	sys-devel/bison
	sys-devel/flex
	sys-devel/gcc
	sys-devel/kgcc64
	sys-devel/gcc-config
	sys-devel/gettext
	sys-devel/gnuconfig
	sys-devel/libtool
	sys-devel/m4
	sys-devel/make
	sys-devel/patch
	sys-kernel/genkernel
	sys-kernel/linux-headers
	sys-libs/db
	sys-libs/gdbm
	sys-libs/cracklib
	x11-misc/shared-mime-info	

livecd/empty:
	/boot
	/etc/cron.daily
	/etc/cron.hourly
	/etc/cron.monthly
	/etc/cron.weekly
	/etc/logrotate.d
	/etc/modules.autoload.d
	/etc/rsync
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
	/usr/include
	/usr/hppa*-unknown-linux-*
	/usr/include
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
	/usr/src
	/var/cache
	/var/empty
	/var/lib/portage
	/var/lock
	/var/log
	/var/run
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
	/usr/sbin/env-update
	/usr/sbin/etc-update
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
