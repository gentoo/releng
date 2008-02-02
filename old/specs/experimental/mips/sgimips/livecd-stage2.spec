subarch: mips3
version_stamp: 2005.1
target: livecd-stage2
rel_type: default
profile: default-linux/mips/2005.0
snapshot: 20051016
source_subpath: default/livecd-stage1-mips3-2005.1

livecd/fstype: normal
livecd/type: gentoo-mips-experimental-rc5
livecd/devmanager: udev
livecd/cdtar: /usr/catalyst/livecd/cdtar/arcload-0.43-cdtar.tar.bz2
livecd/iso: /usr/catalyst/builds/default/sgilivecd-2005_1.img

boot/kernel: ip22r4k ip22r5k ip27r10k ip28r10k ip30r10k ip32r5k
boot/kernel/ip22r4k/sources: =mips-sources-2.6.13.4
boot/kernel/ip22r5k/sources: =mips-sources-2.6.13.4
boot/kernel/ip27r10k/sources: =mips-sources-2.6.12.5
boot/kernel/ip28r10k/sources: =mips-sources-2.6.13.4
boot/kernel/ip30r10k/sources: =mips-sources-2.6.13.4
boot/kernel/ip32r5k/sources: =mips-sources-2.6.13.4

boot/kernel/ip22r4k/config: /usr/share/genkernel/mips/ip22r4k-2005_1.cf
boot/kernel/ip22r5k/config: /usr/share/genkernel/mips/ip22r5k-2005_1.cf
boot/kernel/ip27r10k/config: /usr/share/genkernel/mips/ip27r10k-2005_1.cf
boot/kernel/ip28r10k/config: /usr/share/genkernel/mips/ip28r10k-2005_1.cf
boot/kernel/ip30r10k/config: /usr/share/genkernel/mips/ip30r10k-2005_1.cf
boot/kernel/ip32r5k/config: /usr/share/genkernel/mips/ip32r5k-2005_1.cf

#boot/kernel/ip22r4k/extraversion: ip22r4k
#boot/kernel/ip22r5k/extraversion: ip22r5k
#boot/kernel/ip27r10k/extraversion: ip27r10k+
#boot/kernel/ip28r10k/extraversion: ip28r10k
#boot/kernel/ip30r10k/extraversion: ip30r10k+
#boot/kernel/ip32r5k/extraversion: ip32r5k

boot/kernel/ip22r4k/use: -doc
boot/kernel/ip22r5k/use: -doc
boot/kernel/ip27r10k/use: -doc ip27
boot/kernel/ip28r10k/use: -doc ip28
boot/kernel/ip30r10k/use: -doc ip30
boot/kernel/ip32r5k/use: -doc

boot/kernel/ip22r4k/gk_kernargs: --kernel-cross-compile=mips-unknown-linux-gnu- --makeopts=-j2
boot/kernel/ip22r5k/gk_kernargs: --kernel-cross-compile=mips-unknown-linux-gnu- --makeopts=-j2
boot/kernel/ip27r10k/gk_kernargs: --kernel-cross-compile=mips64-unknown-linux-gnu- --makeopts=-j2
boot/kernel/ip28r10k/gk_kernargs: --kernel-cross-compile=mips64-unknown-linux-gnu- --makeopts=-j2
boot/kernel/ip30r10k/gk_kernargs: --kernel-cross-compile=mips64-unknown-linux-gnu- --makeopts=-j2
boot/kernel/ip32r5k/gk_kernargs: --kernel-cross-compile=mips64-unknown-linux-gnu- --makeopts=-j2


livecd/rcadd: sshd|default

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
	cronbase
	diffutils
	distcc
	ed
	flex
	gcc
	gcc-mips64
	gcc-config
	genkernel
	getdvhoff
	gnuconfig
	help2man
	lcms
	lib-compat
	libtool
	mips-headers
	m4
	make
	man
	man-pages
	miscfiles
	patch
	sash
	sysklogd
	texinfo
	ucl
	mips-sources

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
	/usr/mips-unknown-linux-uclibc
	/usr/mips-unknown-linux-gnu
	/usr/mips64-unknown-linux-gnu
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
	/usr/local
	/usr/portage
	/usr/share/aclocal
	/usr/share/baselayout
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
	/usr/share/locale
	/usr/share/man
	/usr/share/perl
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
	/usr/bin/mips-unknown-linux-*
	/usr/bin/mips64-unknown-linux-*
	/usr/bin/ld
	/usr/bin/nm
	/usr/bin/objcopy
	/usr/bin/objdump
	/usr/bin/piggyback*
	/usr/bin/ranlib
	/usr/bin/readelf
	/usr/bin/size
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
