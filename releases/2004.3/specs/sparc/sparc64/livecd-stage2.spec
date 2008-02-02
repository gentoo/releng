subarch: sparc64
version_stamp: 2004.3
target: livecd-stage2
rel_type: default
profile: default-linux/sparc/sparc64/2004.3
snapshot: 20041022
source_subpath: default/livecd-stage1-sparc64-2004.3

livecd/cdfstype: zisofs
livecd/iso: gentoo-sparc64-2004.3.iso
livecd/archscript: /usr/lib/catalyst/livecd/runscript/sparc64-archscript.sh
livecd/runscript: /usr/lib/catalyst/livecd/runscript/default-runscript.sh
livecd/cdtar: /root/livecd/cdtar/silo-1.3.2-sparc64-cdtar.tar.bz2

#livecd/type: gentoo-release-universal
livecd/type: gentoo-release-minimal
#livecd/motd: /root/files/motd
#livecd/readme: /root/files/README
#livecd/fsscript: /root/livecd/fsscript

boot/kernel: gentoo-2.4 gentoo-2.4-smp
boot/kernel/gentoo-2.4/sources: >=sys-kernel/sparc-sources-2.4.27
boot/kernel/gentoo-2.4/config: config-2.4.27-sparc64-up
boot/kernel/gentoo-2.4/use: ultra1
boot/kernel/gentoo-2.4-smp/sources: >=sys-kernel/sparc-sources-2.4.27
boot/kernel/gentoo-2.4-smp/config: config-2.4.27-sparc64-smp
boot/kernel/gentoo-2.4-smp/extraversion: smp

livecd/rcadd:
	syslog-ng:default

livecd/unmerge:
	addpatches
	autoconf
	automake
	binutils
	bison
	ccache
	flex
	gcc
	gcc-sparc64
	gettext
	groff
	ld.so
	lib-compat
	libtool
	linux-headers
	m4
	make
	man
	man-pages
	miscfiles
	patch
	perl
	python
	sash
	texinfo
	ucl

livecd/empty:
	/etc/cron.daily
	/etc/cron.hourly
	/etc/cron.monthly
	/etc/cron.weekly
	/etc/rsync
	/etc/skel
	/root/.ccache
	/tmp
	/usr/lib/perl5
	/usr/lib/python2.3
	/usr/lib/portage
	/usr/portage
	/usr/share/man
	/usr/share/info
	/usr/share/unimaps
	/usr/include
	/usr/share/zoneinfo
	/usr/share/consolefonts/partialfonts
	/usr/share/consoletrans
	/usr/share/dict
	/usr/share/doc
	/usr/share/emacs
	/usr/share/genkernel
	/usr/share/gettext
	/usr/share/gcc-data
	/usr/share/gnuconfig
	/usr/share/gtk-doc
	/usr/share/i18n
	/usr/share/locale/af
	/usr/share/locale/am
	/usr/share/locale/ar
	/usr/share/locale/az
	/usr/share/locale/be
	/usr/share/locale/bg
	/usr/share/locale/bn
	/usr/share/locale/ca
	/usr/share/locale/cs
	/usr/share/locale/cy
	/usr/share/locale/da
	/usr/share/locale/de
	/usr/share/locale/el
	/usr/share/locale/en
	/usr/share/locale/en_CA
	/usr/share/locale/en_GB
	/usr/share/locale/en_US
	/usr/share/locale/eo
	/usr/share/locale/es
	/usr/share/locale/et
	/usr/share/locale/et_EE
	/usr/share/locale/eu
	/usr/share/locale/fa
	/usr/share/locale/fi
	/usr/share/locale/fr
	/usr/share/locale/ga
	/usr/share/locale/gl
	/usr/share/locale/gr
	/usr/share/locale/gu
	/usr/share/locale/he
	/usr/share/locale/hi
	/usr/share/locale/hr
	/usr/share/locale/hu
	/usr/share/locale/id
	/usr/share/locale/is
	/usr/share/locale/it
	/usr/share/locale/ja
	/usr/share/locale/ko
	/usr/share/locale/lt
	/usr/share/locale/lug
	/usr/share/locale/lv
	/usr/share/locale/mk
	/usr/share/locale/mn
	/usr/share/locale/ms
	/usr/share/locale/nb
	/usr/share/locale/ne
	/usr/share/locale/nl
	/usr/share/locale/nn
	/usr/share/locale/no
	/usr/share/locale/pa
	/usr/share/locale/pl
	/usr/share/locale/pt
	/usr/share/locale/pt_BR
	/usr/share/locale/ro
	/usr/share/locale/ru
	/usr/share/locale/sk
	/usr/share/locale/sl
	/usr/share/locale/sq
	/usr/share/locale/sr
	/usr/share/locale/sr@Latn
	/usr/share/locale/sr@ije
	/usr/share/locale/sv
	/usr/share/locale/ta
	/usr/share/locale/tr
	/usr/share/locale/uk
	/usr/share/locale/vi
	/usr/share/locale/wa
	/usr/share/locale/yi
	/usr/share/locale/zh_CN
	/usr/share/locale/zh_TW
	/usr/share/man
	/usr/share/rfc
	/usr/share/ss
	/usr/share/state
	/usr/share/texinfo
	/usr/src
	/usr/X11R6
	/var/cache
	/var/db
	/var/empty
	/var/lib/portage
	/var/lock
	/var/log
	/var/tmp

livecd/rm:
	/etc/*-
	/etc/*.old
	/etc/default/audioctl
	/etc/dispatch-conf.conf
	/etc/etc-update.conf
	/etc/genkernel.conf
	/etc/make.conf
	/etc/make.conf.example
	/etc/make.globals
	/etc/make.profile
	/etc/man.conf
	/etc/resolv.conf
	/lib/*.a
	/lib/security/pam_access.so
	/lib/security/pam_chroot.so
	/lib/security/pam_debug.so
	/lib/security/pam_ftp.so
	/lib/security/pam_issue.so
	/lib/security/pam_mail.so
	/lib/security/pam_motd.so
	/lib/security/pam_mkhomedir.so
	/lib/security/pam_postgresok.so
	/lib/security/pam_rhosts_auth.so
	/lib/security/pam_userdb.so
	/sbin/fsck.cramfs
	/sbin/fsck.minix
	/sbin/mkfs.bfs
	/sbin/mkfs.cramfs
	/sbin/mkfs.minix
	/usr/bin/audioctl
	/usr/bin/elftoaout
	/usr/bin/piggyback
	/usr/bin/piggyback64
	/usr/lib/*.a
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
