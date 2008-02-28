subarch: ppc64
target: livecd-stage2
rel_type: default
snapshot: 2008.0
version_stamp: 2008.0
profile: default/linux/powerpc/ppc64/2008.0/32bit-userland
source_subpath: default/livecd-stage1-ppc64-32ul-2008.0/

livecd/type: gentoo-release-universal
livecd/overlay: /2008.0/overlay/

livecd/gk_mainargs: --utils-arch=ppc --arch-override=ppc --makeopts=-j8 --lvm --dmraid --evms


livecd/fstype: squashfs 
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/yaboot-1.3.13-cdtar.tar.bz2
livecd/iso: /root/install-ppc64-universal-2008.0.iso
livecd/rcadd: pbbuttonsd|default


boot/kernel: ibmpower G5 ppc32

## IBM hardware
boot/kernel/ibmpower/sources: sys-kernel/gentoo-sources
boot/kernel/ibmpower/use: usb extlib
boot/kernel/ibmpower/config: /home/ranger/2008.0/svn/releng/trunk/releases/2008.0/kconfig/powerpc/installcd-ibm-2.6.23.config
boot/kernel/ibmpower/console: ttyS0,9600 hvc0 hvsi0
boot/kernel/ibmpower/machine_type: ibm
boot/kernel/ibmpower/extraversion: ibm
boot/kernel/ibmpower/gk_kernargs: --kernel-cross-compile=powerpc64-unknown-linux-gnu-


## Apple hardware
boot/kernel/G5/sources: sys-kernel/gentoo-sources
boot/kernel/G5/use: usb extlib
boot/kernel/G5/config: /home/ranger/2008.0/svn/releng/trunk/releases/2008.0/kconfig/powerpc/installcd-ppc64apple-2.6.23.config
boot/kernel/G5/console: ttyS0,57600
boot/kernel/G5/extraversion: G5
boot/kernel/G5/gk_kernargs: --kernel-cross-compile=powerpc64-unknown-linux-gnu-

## ppc32 hardware
boot/kernel/ppc32/config: /home/ranger/2008.0/svn/releng/trunk/releases/2008.0/kconfig/powerpc/installcd-ppc32apple-2.6.23.config
boot/kernel/ppc32/sources: gentoo-sources
boot/kernel/ppc32/extraversion: ppc32
boot/kernel/ppc32/use: pcmcia usb oss atm truetype -qt -qt3 -qt4 -ibam
boot/kernel/ppc32/packages:
        #media-gfx/splashutils
        #media-gfx/splash-themes-livecd
        sys-apps/pcmciautils
        sys-fs/cryptsetup
        app-laptop/pbbuttonsd


livecd/unmerge:
	autoconf automake binutils libtool m4 bison  make patch 
	linux-headers man-pages sandbox gcc kgcc64
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
