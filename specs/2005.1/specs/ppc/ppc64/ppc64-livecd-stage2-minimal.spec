subarch: ppc64-64ul
target: livecd-stage2

rel_type: default
rel_version: 2005.1
snapshot: 20050709
version_stamp: minimal-2005.1
profile: default-linux/ppc/2005.1/ppc64/64bit-userland/
source_subpath: default/livecd-stage1-ppc64-64ul-2005.1

livecd/type: gentoo-release-minimal

livecd/gk_mainargs: --makeopts=-j8

livecd/cdfstype: zisofs
livecd/archscript: /usr/lib/catalyst/livecd/runscript/ppc-archscript.sh
livecd/runscript: /usr/lib/catalyst/livecd/runscript/default-runscript.sh
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/yaboot-1.3.11-cdtar.tar.bz2

livecd/devmanager: udev

boot/kernel: pseries js20 G5 xserv 

boot/kernel/pseries/sources: =sys-kernel/vanilla-sources-2.6.12.2
boot/kernel/pseries/use: extlib udev
boot/kernel/pseries/config: /2005.1_release/kernel_configs/pseries
boot/kernel/pseries/extraversion: pseries

boot/kernel/js20/sources: =sys-kernel/vanilla-sources-2.6.12.2
boot/kernel/js20/gk_kernargs: --bladecenter
boot/kernel/js20/use: usb extlib udev bladecenter
boot/kernel/js20/config: /2005.1_release/kernel_configs/js20
boot/kernel/js20/extraversion: js20

boot/kernel/G5/sources: =sys-kernel/vanilla-sources-2.6.12.2
boot/kernel/G5/use: extlib udev
boot/kernel/G5/config: /2005.1_release/kernel_configs/G5
boot/kernel/G5/extraversion: G5

boot/kernel/xserv/sources: =sys-kernel/vanilla-sources-2.6.12.2
boot/kernel/xserv/use: extlib udev
boot/kernel/xserv/config: /2005.1_release/kernel_configs/xserv
boot/kernel/xserv/extraversion: xserv

livecd/unmerge:
	autoconf automake binutils libtool m4 bison  make perl patch 
	linux-headers man-pages sandbox
	sash bison flex gettext sys-apps/texinfo ccache addpatches 
	man groff lib-compat gcc python miscfiles devfsd

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
	/usr/lib/portage
	/usr/share/i18n
	/usr/src
	/usr/lib/portage
	
livecd/rm:
	/lib/*.a
	/usr/lib/*.a
	/usr/lib/gcc-lib/*/*/libgcj*
	/etc/dispatch-conf.conf
	/etc/env.d/05portage.envd
	/etc/etc-update.conf
	/etc/make.conf.example
	/etc/make.globals
	/usr/bin/ebuild
	/usr/bin/emerge
	/usr/bin/portage
	/usr/bin/repoman
	/usr/bin/tbz2tool
	/usr/bin/xpak
	/usr/sbin/archive-conf
	/usr/sbin/dispatch-conf
	/usr/sbin/ebuild
	/usr/sbin/emerge-webrsync
	/usr/sbin/env-update
	/usr/sbin/etc-update
	/usr/sbin/fixpackages
	/usr/sbin/quickpkg
	/usr/sbin/regenworld
