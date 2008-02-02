# $Header: /var/cvsroot/gentoo/src/releng/specs/2006.0/ppc/ppc32/livecd-stage2-universal.spec,v 1.1 2006-02-22 23:09:32 pylon Exp $
subarch: ppc
version_stamp: 2006.0
target: livecd-stage2
rel_type: official
profile: default-linux/ppc/ppc32
snapshot: official
source_subpath: official/livecd-stage1-ppc-2006.0

livecd/type: gentoo-release-universal
livecd/fstype: squashfs
livecd/cdtar: /var/tmp/catalyst2/specs/cdtar/yaboot-1.3.13-cdtar.tar.bz2
livecd/iso: /var/tmp/catalyst2/iso/install-ppc-universal-2006.0.iso
livecd/volid: Gentoo Linux 2006.0 PPC
livecd/modblacklist: 8139cp

livecd/overlay: /var/tmp/catalyst2/overlay/livecd-universal/

livecd/gk_mainargs: --lvm2

boot/kernel: ppc32 pegasos

boot/kernel/ppc32/config: /usr/src/configs/ppc32
boot/kernel/ppc32/sources: sys-kernel/gentoo-sources
boot/kernel/ppc32/use: pcmcia usb -X png truetype
boot/kernel/ppc32/extraversion: ppc32
boot/kernel/ppc32/packages:
	pbbuttonsd
	cryptsetup-luks
	pcmcia-cs

boot/kernel/pegasos/config: /usr/src/configs/pegasos
boot/kernel/pegasos/sources: sys-kernel/gentoo-sources
boot/kernel/pegasos/use: usb -X png truetype
boot/kernel/pegasos/extraversion: pegasos
boot/kernel/pegasos/gk_kernargs: --no-initrdmodules --genzimage

livecd/rcadd: syslog-ng|default pbbuttonsd|default
livecd/bootargs: dokeymap

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
	/usr/lib/nfs
	/usr/lib/portage
	/usr/lib/python2.2
	/usr/local
	/usr/portage
	/usr/share/consolefonts/partialfonts
	/usr/share/consoletrans
	/usr/share/dict
	/usr/share/doc
	/usr/share/emacs
	/usr/share/gcc-data
	/usr/share/genkernel
	/usr/share/gettext
	/usr/share/gnuconfig
	/usr/share/i18n
	/usr/share/info
	/usr/share/lcms
	/usr/share/locale
	/usr/share/man
	/usr/share/man
	/usr/share/rfc
	/usr/share/ss
	/usr/share/state
	/usr/share/texinfo
	/usr/share/unimaps
	/usr/share/zoneinfo
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
	/etc/etc-update.conf
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
        /etc/splash/livecd-2005.1/images/silent-12*
        /etc/splash/livecd-2005.1/images/silent-14*
        /etc/splash/livecd-2005.1/images/silent-16*
        /etc/splash/livecd-2005.1/images/silent-19*
        /etc/splash/livecd-2005.1/images/silent-6*
        /etc/splash/livecd-2005.1/images/silent-8*
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
	/root/.bash_history
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
	/usr/sbin/fsck.cramfs
	/usr/sbin/fsck.minix
	/usr/sbin/mkfs.bfs
	/usr/sbin/mkfs.cramfs
	/usr/sbin/mkfs.minix
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
