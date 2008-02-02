subarch: alpha
version_stamp: 2005.0
target: livecd-stage2
rel_type: default
rel_version: 2005.0
profile: default-linux/alpha/2005.0
snapshot: 20050303
source_subpath: default/livecd-stage1-alpha-2005.0
distcc_hosts: gendcc01 gendcc02 gendcc03 gendcc04 gendcc05 gendcc06 gendcc07
livecd/cdfstype: zisofs
livecd/archscript: /usr/lib/catalyst/livecd/runscript/alpha-archscript.sh
livecd/runscript: /usr/lib/catalyst/livecd/runscript/default-runscript.sh
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/aboot-0.9-r1-cdtar.tar.bz2
livecd/iso: /home/kloeri/install-alpha-minimal-2005.0.iso

livecd/type: gentoo-release-minimal

livecd/devmanager: devfs

livecd/rcadd:
	metalog:default
	gpm:default

livecd/gk_mainargs: --do-keymap-auto
livecd/overlay: /home/kloeri/overlay-minimal
		
boot/kernel: gentoo-2.6 gentoo-2.4
boot/kernel/gentoo-2.4/sources: =sys-kernel/vanilla-sources-2.4.28
boot/kernel/gentoo-2.6/sources: =sys-kernel/vanilla-sources-2.6.10

boot/kernel/gentoo-2.4/config: /home/kloeri/livecd/kconfig/2.4.28.config
boot/kernel/gentoo-2.6/config: /home/kloeri/livecd/kconfig/2.6.10.config

boot/kernel/gentoo-2.4/use: -X -doc
boot/kernel/gentoo-2.6/use: -X -doc

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
