version_stamp: 2006.0

subarch: ia64
target: livecd-stage2
rel_type: default
profile: default-linux/ia64/2006.0
snapshot: 20060123
source_subpath: default/livecd-stage1-ia64-2006.0

livecd/cdtar: /usr/lib/catalyst2/livecd/cdtar/elilo-3.4-cdtar.tar.bz2
livecd/cdfstype: squashfs
livecd/iso: /var/tmp/catalyst2/out.iso
livecd/type: gentoo-release-minimal
livecd/devmanager: udev
livecd/gk_mainargs: --lvm2
portage_overlay: overlay

boot/kernel: gentoo
boot/kernel/gentoo/config: installcd-2.6.15.config
boot/kernel/gentoo/sources: gentoo-sources
boot/kernel/gentoo/use: usb -X

livecd/unmerge:
	acl
	attr
	autoconf
	automake
	binutils
	libtool
	m4
	bison
	ld.so
	make
	perl
	patch
	linux-headers
	man-pages
	sash
	bison
	flex
	gettext
	texinfo
	ccache
	distcc
	addpatches
	man
	groff
	lib-compat
	miscfiles
	rsync
	sysklogd
	bc
	lcms
	libmng
	genkernel
	diffutils
#	file
	libperl
	gnuconfig
	gcc-config
	gcc
	cpio
	cronbase
	ed
	expat
	grub
	help2man
	libtool

livecd/empty:
	/var/tmp
	/var/cache
	/var/db
	/var/empty
	/var/lock
	/var/log
	/var/run
	/var/spool
	/var/state
	/tmp
	/usr/portage
	/usr/share/man
	/usr/share/info
	/usr/share/unimaps
	/usr/include
	/usr/share/zoneinfo
	/usr/share/dict
	/usr/share/doc
	/usr/share/ss
	/usr/share/state
	/usr/share/texinfo
	/usr/lib/python2.2
	/usr/lib/portage
	/usr/share/gettext
	/usr/share/i18n
	/usr/share/rfc
	/usr/X11R6/man
	/usr/X11R6/include
	/usr/X11R6/lib/X11/config
	/usr/X11R6/lib/X11/etc
	/usr/X11R6/lib/X11/doc
	/usr/src
	/usr/share/doc
	/usr/share/man
	/root/.ccache
# Added by wolf31o2
	/etc/cron.daily
	/etc/cron.hourly
	/etc/cron.monthly
	/etc/cron.weekly
	/etc/logrotate.d
	/etc/rsync
	/usr/X11R6
	/usr/include
	/usr/lib/awk
	/usr/lib/ccache
	/usr/lib/gcc-config
	/usr/lib/nfs
	/usr/local
	/usr/diet/include
	/usr/diet/man
	/usr/share/consolefonts/partialfonts
	/usr/share/consoletrans
	/usr/share/emacs
	/usr/share/gcc-data
	/usr/share/genkernel
	/etc/bootsplash/gentoo
	/etc/bootsplash/gentoo-highquality
	/etc/splash/gentoo
	/etc/splash/emergence
	/usr/share/gnuconfig
	/usr/share/lcms
	/usr/share/locale/af
	/usr/share/locale/be
	/usr/share/locale/bg
	/usr/share/locale/bs
	/usr/share/locale/ca
	/usr/share/locale/cs
	/usr/share/locale/da
	/usr/share/locale/de
	/usr/share/locale/el
	/usr/share/locale/en
	/usr/share/locale/en_GB
	/usr/share/locale/eo
	/usr/share/locale/es
	/usr/share/locale/et
	/usr/share/locale/et_EE
	/usr/share/locale/eu
	/usr/share/locale/eu_ES
	/usr/share/locale/fi
	/usr/share/locale/fr
	/usr/share/locale/ga
	/usr/share/locale/gl
	/usr/share/locale/gr
	/usr/share/locale/he
	/usr/share/locale/hr
	/usr/share/locale/hu
	/usr/share/locale/id
	/usr/share/locale/is
	/usr/share/locale/it
	/usr/share/locale/ja
	/usr/share/locale/ja_JP.EUC
	/usr/share/locale/ko
	/usr/share/locale/lug
	/usr/share/locale/ms
	/usr/share/locale/nb
	/usr/share/locale/nl
	/usr/share/locale/nn
	/usr/share/locale/no
	/usr/share/locale/pl
	/usr/share/locale/pt
	/usr/share/locale/pt_BR
	/usr/share/locale/ro
	/usr/share/locale/ru
	/usr/share/locale/sk
	/usr/share/locale/sl
	/usr/share/locale/sr
	/usr/share/locale/sv
	/usr/share/locale/tr
	/usr/share/locale/uk
	/usr/share/locale/vi
	/usr/share/locale/wa
	/usr/share/locale/zh_CN
	/usr/share/locale/zh_TW
	#/usr/share/misc/file
	#/usr/share/vim/vim63/doc
	#/usr/share/vim/vim63/syntax
	/etc/skel

livecd/rm:
	/lib/*.a
	/usr/lib/*.a
	/usr/lib/gcc-lib/*/*/libgcj*
	/usr/X11R6/lib/*.a
	/etc/dispatch-conf.conf
	/etc/etc-update.conf
	/etc/*-
	/etc/issue*
	/etc/make.conf
	/etc/man.conf
	/etc/*.old
	/root/.viminfo
	/usr/sbin/bootsplash*
	/usr/sbin/fb*
	/usr/sbin/fsck.cramfs
	/usr/sbin/fsck.minix
	/usr/sbin/mkfs.minix
	/usr/sbin/mkfs.bfs
	/usr/sbin/mkfs.cramfs
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
	/etc/bootsplash/livecd-2005.0/images/bootsplash-12*
	/etc/bootsplash/livecd-2005.0/images/bootsplash-16*
	/etc/bootsplash/livecd-2005.0/images/bootsplash-8*
	/etc/bootsplash/livecd-2005.0/images/silent-12*
	/etc/bootsplash/livecd-2005.0/images/silent-16*
	/etc/bootsplash/livecd-2005.0/images/silent-8*
	/etc/splash/livecd-2005.0/16*
	/etc/splash/livecd-2005.0/12*
	/etc/splash/livecd-2005.0/6*
	/etc/splash/livecd-2005.0/8*
	/etc/splash/livecd-2005.0/images/silent-16*
	/etc/splash/livecd-2005.0/images/silent-12*
	/etc/splash/livecd-2005.0/images/silent-6*
	/etc/splash/livecd-2005.0/images/silent-8*
	/etc/splash/livecd-2005.0/images/verbose-16*
	/etc/splash/livecd-2005.0/images/verbose-12*
	/etc/splash/livecd-2005.0/images/verbose-6*
	/etc/splash/livecd-2005.0/images/verbose-8*
	/etc/make.conf.example
	/etc/make.globals
	/etc/resolv.conf
