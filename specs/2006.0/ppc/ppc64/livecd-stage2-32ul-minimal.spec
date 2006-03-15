subarch: ppc64
target: livecd-stage2

rel_type: default
snapshot: 20060123
version_stamp: 2006.0
profile: default-linux/ppc/ppc64/2006.0/32bit-userland
source_subpath: default/livecd-stage1-ppc64-2006.0

chost: powerpc-unknown-linux-gnu
cflags: -O2 -pipe
cxxflags: -O2 -pipe

#portage_overlay: /home/ranger/overlay/portage

livecd/readme: /2006/overlay/README.txt
livecd/overlay: /2006/minimal-overlay/

livecd/type: gentoo-release-minimal

livecd/gk_mainargs: --kernel-cross-compile=powerpc64-unknown-linux-gnu- --utils-arch=ppc --arch-override=ppc --makeopts=-j8 --lvm2
#--utils-arch=ppc --kernel-cross-compile=powerpc64-unknown-linux-gnu

livecd/fstype: zisofs
#livecd/cdtar: /usr/lib/catalyst2/livecd/cdtar/yaboot-1.3.11-cdtar.tar.bz2
livecd/cdtar: /usr/lib/catalyst2/livecd/cdtar/yaboot-1.3.11-ppc-cdtar-r1.tar.bz2
livecd/iso: /root/install-ppc64-minimal-2006.0.iso

livecd/devmanager: udev

boot/kernel: ibmpower G5

## IBM hardware
boot/kernel/ibmpower/sources: sys-kernel/vanilla-sources
boot/kernel/ibmpower/use: usb extlib
boot/kernel/ibmpower/config: /2006/kernel_configs/power_merged
boot/kernel/ibmpower/console: ttyS0,9600 hvc0 hvsi0
boot/kernel/ibmpower/machine_type: ibm
boot/kernel/ibmpower/extraversion: ibm

## Apple hardware
boot/kernel/G5/sources: sys-kernel/vanilla-sources
boot/kernel/G5/use: usb extlib
boot/kernel/G5/config: /2006/kernel_configs/G5
boot/kernel/G5/console: ttyS0,57600
boot/kernel/G5/extraversion: G5



livecd/unmerge:
	autoconf automake binutils libtool m4 bison  make perl patch 
	linux-headers man-pages sandbox
	sash bison flex gettext sys-apps/texinfo ccache addpatches 
	man groff lib-compat miscfiles devfsd

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
