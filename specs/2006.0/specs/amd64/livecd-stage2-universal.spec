subarch: amd64
version_stamp: 2006.0
target: livecd-stage2
rel_type: default
profile: default-linux/amd64/2006.0
snapshot: official
source_subpath: default/livecd-stage1-amd64-2006.0

livecd/fstype: squashfs
livecd/cdtar: /usr/lib/catalyst2/livecd/cdtar/isolinux-3.09-memtest86+-cdtar.tar.bz2

livecd/iso: /tmp/installcd-amd64-universal-2006.0.iso
livecd/splash_type: gensplash
livecd/splash_theme: livecd-2006.0

livecd/volid: Gentoo Linux amd64 2006.0
livecd/type: gentoo-release-universal

livecd/overlay: /home/wolf31o2/livecd/overlays/amd64-universal

livecd/bootargs: dokeymap
livecd/gk_mainargs: --lvm2 --dmraid --evms2

boot/kernel: gentoo
boot/kernel/gentoo/sources: gentoo-sources

boot/kernel/gentoo/config: /home/wolf31o2/livecd/kconfig/releases/2006.0/amd64/installcd-2.6.15.config

boot/kernel/gentoo/use: pcmcia usb -X png truetype

boot/kernel/gentoo/packages:
	splashutils
	splash-themes-livecd
	pcmcia-cs
#	slmodem
#	globespan-adsl
#	hostap-driver
#	hostap-utils
#	ipw2100
#	ipw2200
#	fritzcapi
#	fcdsl
	cryptsetup-luks
# These were not stable at time of snapshot/release.
#	at76c503a
#	rt2500
#	rtl8180
#	rtl8187
#	adm8211
#	acx100

livecd/unmerge:
	acl
	addpatches
	attr
	autoconf
	autoconf-wrapper
	automake
	automake-wrapper
	bc
	bin86
	binutils
	binutils-config
	bison
	busybox
	ccache
	cpio
	cronbase
	devfsd
	diffutils
	distcc
	ed
	expat
	flex
	gcc
	gcc-config
	gcc-sparc64
	genkernel
	gentoo-sources
	gettext
	gnuconfig
	groff
	grub
	help2man
	lcms
	ld.so
	lib-compat
	libmng
	libperl
	libtool
	linux-headers
	m4
	make
	man
	man-pages
	miscfiles
	patch
	perl
	rsync
	sandbox
	sash
	sysklogd
	texinfo
	ucl
	vanilla-sources

livecd/empty:
	/etc/bootsplash/gentoo
	/etc/bootsplash/gentoo-highquality
	/etc/cron.daily
	/etc/cron.hourly
	/etc/cron.monthly
	/etc/cron.weekly
	/etc/kernels
	/etc/logrotate.d
	/etc/modules.autoload.d
	/etc/rsync
	/etc/runlevels/single
	/etc/skel
	/etc/splash/emergence
	/etc/splash/gentoo
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
	/usr/include
	/usr/lib/X11/config
	/usr/lib/X11/doc
	/usr/lib/X11/etc
	/usr/lib/awk
	/usr/lib/ccache
	/usr/lib/gcc-config
	/usr/lib/gconv
	/usr/lib/nfs
	/usr/lib/perl5
	/usr/lib/portage
	/usr/lib/python2.2
	/usr/lib/python2.3
	/usr/lib/python2.4/tests
	/usr/lib64/X11/config
	/usr/lib64/X11/doc
	/usr/lib64/X11/etc
	/usr/lib64/awk
	/usr/lib64/ccache
	/usr/lib64/gcc-config
	/usr/lib64/gconv
	/usr/lib64/nfs
	/usr/lib64/perl5
	/usr/lib64/portage
	/usr/lib64/python2.2
	/usr/lib64/python2.3
	/usr/lib64/python2.4/tests
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
	/usr/share/perl
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
	/var/db
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
	/etc/make.conf
	/etc/make.conf.example
	/etc/make.globals
	/etc/make.profile
	/etc/man.conf
	/etc/resolv.conf
	/etc/splash/livecd-2006.0/12*
	/etc/splash/livecd-2006.0/14*
	/etc/splash/livecd-2006.0/16*
	/etc/splash/livecd-2006.0/19*
	/etc/splash/livecd-2006.0/6*
	/etc/splash/livecd-2006.0/8*
	/etc/splash/livecd-2006.0/images/background-12*
	/etc/splash/livecd-2006.0/images/background-14*
	/etc/splash/livecd-2006.0/images/background-16*
	/etc/splash/livecd-2006.0/images/background-19*
	/etc/splash/livecd-2006.0/images/background-6*
	/etc/splash/livecd-2006.0/images/background-8*
	/etc/splash/livecd-2006.0/images/verbose-12*
	/etc/splash/livecd-2006.0/images/verbose-14*
	/etc/splash/livecd-2006.0/images/verbose-16*
	/etc/splash/livecd-2006.0/images/verbose-19*
	/etc/splash/livecd-2006.0/images/verbose-6*
	/etc/splash/livecd-2006.0/images/verbose-8*
	/lib*/*.a
	/lib*/*.la
	/lib*/cpp
	/lib*/security/pam_access.so
	/lib*/security/pam_chroot.so
	/lib*/security/pam_debug.so
	/lib*/security/pam_ftp.so
	/lib*/security/pam_issue.so
	/lib*/security/pam_mail.so
	/lib*/security/pam_mkhomedir.so
	/lib*/security/pam_motd.so
	/lib*/security/pam_postgresok.so
	/lib*/security/pam_rhosts_auth.so
	/lib*/security/pam_userdb.so
	/root/.viminfo
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
	/usr/bin/elftoaout
	/usr/bin/f77
	/usr/bin/g++*
	/usr/bin/g77
	/usr/bin/gcc*
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
	/usr/bin/ranlib
	/usr/bin/readelf
	/usr/bin/size
	/usr/bin/powerpc-unknown-linux-gnu-*
	/usr/bin/sparc-unknown-linux-gnu-*
	/usr/bin/sparc64-unknown-linux-gnu-*
	/usr/bin/strings
	/usr/bin/strip
	/usr/bin/x86_64-pc-linux-gnu-*
	/usr/lib*/*.a
	/usr/lib*/*.la
	/usr/lib*/gcc-lib/*/*/libgcj*
	/usr/sbin/bootsplash*
	/usr/sbin/fb*
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
