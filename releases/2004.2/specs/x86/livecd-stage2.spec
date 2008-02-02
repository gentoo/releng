subarch: x86
version_stamp: 2004.2
target: livecd-stage2
rel_type: default
profile: default-x86-2004.0
snapshot: 20040710
distcc_hosts: localhost/3 gravity/3 orion/3
source_subpath: default/livecd-stage1-x86-2004.2

livecd/cdfstype: squashfs
livecd/archscript: /usr/lib/catalyst/livecd/runscript/x86-archscript.sh
livecd/runscript: /usr/lib/catalyst/livecd/runscript/default-runscript.sh
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/isolinux-2.08-memtest86-cdtar.tar.bz2
livecd/iso: /tmp/livecd.iso
livecd/bootsplash: livecd-2004.2

livecd/type: gentoo-release-minimal
livecd/modblacklist: siimage 8139cp
livecd/overlay: /root/livecd/overlay-minimal

boot/kernel: gentoo smp
boot/kernel/gentoo/sources: sys-kernel/gentoo-sources
boot/kernel/smp/sources: sys-kernel/gentoo-dev-sources

boot/kernel/gentoo/config: /root/livecd/kconfig/20040622-x86-gentoo-2.4.26-r3.config
boot/kernel/smp/config: /root/livecd/kconfig/20040622-x86-smp-2.6.7-r3.config

boot/kernel/gentoo/use: pcmcia usb
boot/kernel/smp/use: pcmcia usb

boot/kernel/gentoo/packages:
	pcmcia-cs
	slmodem
	ipw2100
	linux-wlan-ng

boot/kernel/smp/packages:
	pcmcia-cs

livecd/unmerge:
	autoconf
	automake
	bin86
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
	addpatches
	man
	groff
	lib-compat
	gcc
	miscfiles
	sysklogd

livecd/empty:
	/var/tmp
	/var/cache
	/var/db
	/var/empty
	/var/cache
	/var/lock
	/var/log
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

livecd/rm:
	/lib/*.a
	/usr/lib/*.a
	/usr/lib/gcc-lib/*/*/libgcj*
	/usr/X11R6/lib/*.a
