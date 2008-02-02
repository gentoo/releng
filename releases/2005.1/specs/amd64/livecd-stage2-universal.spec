subarch: amd64
version_stamp: universal-2005.1
target: livecd-stage2
rel_type: default
profile: default-linux/amd64/2005.1
snapshot: official
source_subpath: default/livecd-stage1-amd64-2005.1

distcc_hosts: pitr-int/2 localhost

livecd/cdfstype: squashfs
livecd/archscript: /usr/lib/catalyst/livecd/runscript/x86-archscript.sh
livecd/runscript: /usr/lib/catalyst/livecd/runscript/default-runscript.sh
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/isolinux-3.09-memtest86+-cdtar.tar.bz2
livecd/iso: /release/buildroot/amd64-default/builds/default/install-amd64-universal-2005.1.iso
livecd/splash_type: gensplash
livecd/splash_theme: livecd-2005.1

livecd/type: gentoo-release-universal
#livecd/modblacklist: 8139cp

livecd/overlay: overlay-universal

livecd/devmanager: udev

livecd/bootargs: dokeymap
livecd/gk_mainargs: --lvm2 --dmraid --evms2

boot/kernel: gentoo
boot/kernel/gentoo/sources: gentoo-sources
boot/kernel/gentoo/config: kconfig/2.6.12-smp.config
boot/kernel/gentoo/use: pcmcia usb -X png truetype

boot/kernel/gentoo/packages:
	splashutils
	splash-themes-livecd
	pcmcia-cs
	speedtouch
#	globespan-adsl
#	hostap-driver
#	hostap-utils
#	ipw2100
#	madwifi-driver
	cryptsetup

livecd/unmerge:
	acl
	addpatches
	attr
	autoconf
	automake
	bc
	bin86
	binutils
	bison
	busybox
	ccache
	cpio
	cronbase
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
	/etc/logrotate.d
	/etc/rsync
	/etc/skel
	/etc/splash/emergence
	/etc/splash/gentoo
	/root/.ccache
	/tmp
	/usr/diet/include
	/usr/diet/man
	/usr/include
	/usr/lib/X11/config
	/usr/lib/X11/doc
	/usr/lib/X11/etc
	/usr/lib/awk
	/usr/lib/ccache
	/usr/lib/gcc-config
	/usr/lib32/gconv
	/usr/lib64/gconv
	/usr/lib/nfs
	/usr/lib/perl5
	/usr/lib/portage
	/usr/lib/python2.2
	/usr/local
	/usr/portage
	/usr/share/aclocal
	/usr/share/baselayout
	/usr/share/consolefonts/partialfonts
	/usr/share/consoletrans
	/usr/share/emacs
	/usr/share/gcc-data
	/usr/share/genkernel
	/usr/share/gettext
	/usr/share/gnuconfig
	/usr/share/lcms
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
	/etc/splash/livecd-2005.1/12*
	/etc/splash/livecd-2005.1/14*
	/etc/splash/livecd-2005.1/16*
	/etc/splash/livecd-2005.1/19*
	/etc/splash/livecd-2005.1/6*
	/etc/splash/livecd-2005.1/8*
	/etc/splash/livecd-2005.1/images/background-12*
	/etc/splash/livecd-2005.1/images/background-14*
	/etc/splash/livecd-2005.1/images/background-16*
	/etc/splash/livecd-2005.1/images/background-19*
	/etc/splash/livecd-2005.1/images/background-6*
	/etc/splash/livecd-2005.1/images/background-8*
	/etc/splash/livecd-2005.1/images/verbose-12*
	/etc/splash/livecd-2005.1/images/verbose-14*
	/etc/splash/livecd-2005.1/images/verbose-16*
	/etc/splash/livecd-2005.1/images/verbose-19*
	/etc/splash/livecd-2005.1/images/verbose-6*
	/etc/splash/livecd-2005.1/images/verbose-8*
	/lib/*.a
	/lib/security/pam_access.so
	/lib/security/pam_chroot.so
	/lib/security/pam_debug.so
	/lib/security/pam_ftp.so
	/lib/security/pam_issue.so
	/lib/security/pam_mail.so
	/lib/security/pam_mkhomedir.so
	/lib/security/pam_motd.so
	/lib/security/pam_postgresok.so
	/lib/security/pam_rhosts_auth.so
	/lib/security/pam_userdb.so
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
	/usr/bin/elftoaout
	/usr/bin/gprof
	/usr/bin/i386-gentoo-linux-uclibc-*
	/usr/bin/i386-pc-linux-*
	/usr/bin/ld
	/usr/bin/nm
	/usr/bin/objcopy
	/usr/bin/objdump
	/usr/bin/piggyback*
	/usr/bin/ranlib
	/usr/bin/readelf
	/usr/bin/size
	/usr/bin/sparc-unknown-linux-*
	/usr/bin/sparc64-unknown-linux-*
	/usr/bin/strings
	/usr/bin/strip
	/usr/lib/*.a
	/usr/lib/gcc-lib/*/*/libgcj*
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
