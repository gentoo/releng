subarch: alpha
version_stamp: 2004.3
target: livecd-stage2
rel_type: default
rel_version: 2004.3
profile: default-linux/alpha/2004.3
snapshot: 20041023
source_subpath: default/livecd-stage1-alpha-2004.3
livecd/cdfstype: zisofs
livecd/archscript: /root/alphacds/livecd/runscript/alpha-archscript.sh
livecd/runscript: /root/alphacds/livecd/runscript/default-runscript.sh
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/aboot-0.9-r1-cdtar.tar.bz2
livecd/iso: /root/alphacds/minimal-alpha-2004.3.iso
boot/kernel: gentoo
boot/kernel/gentoo/sources: =sys-kernel/vanilla-sources-2.4.27
boot/kernel/gentoo/config: /root/alphacds/livecd/kconfig/config-2004.3-vanilla-sources-2.4.27
#boot/kernel/gentoo/packages: >=sys-apps/pcmcia-cs-3.2.7
boot/kernel/gentoo/extraversion: gentoo
boot/kernel/gentoo/kernelopts:
boot/kernel/gentoo/use: -X

livecd/unmerge:
	autoconf automake binutils libtool m4 bison make perl patch linux-headers man-pages
	sash bison flex gettext texinfo ccache addpatches man groff lib-compat gcc python miscfiles ucl
livecd/empty:
	/var/tmp
	/var/cache
	/var/db
	/var/empty
	/var/cache
	/var/lock
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
	/usr/share/genkernel
	/usr/share/gtk-doc
	/boot/kernel*
	/boot/initrd*

