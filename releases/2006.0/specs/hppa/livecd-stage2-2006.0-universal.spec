## Template for Gentoo Linux release bootable LiveCDs
## John Davis <zhen@gentoo.org>

subarch: hppa1.1
version_stamp: 2006.0
target: livecd-stage2
rel_type: default
profile: default-linux/hppa/2005.0
snapshot: 20060123
source_subpath: default/livecd-stage1-hppa1.1-2006.0

livecd/fstype: squashfs
#livecd/archscript: /usr/lib/catalyst/livecd/runscript/hppa-archscript.sh
#livecd/runscript: /usr/lib/catalyst/livecd/runscript/default-runscript.sh
livecd/cdtar: /usr/lib/catalyst2/livecd/cdtar/palo-1.5_pre20040515-cdtar.tar.bz2 

livecd/iso: /tmp/install-hppa-universal-2006.0.iso
livecd/devmanager: udev

# "global" arguments that are to be passed to genkernel
#livecd/gk_mainargs: --makeopts=-j1

# tweaks things such as the MOTD for release LiveCDs
livecd/type: gentoo-release-universal
livecd/bootargs: dokeymap

# the standard Gentoo release MOTD is included with Catalyst
#livecd/motd: /usr/lib/catalyst/livecd/files/motd.txt

# Put directories, files (README,Handbook), etc that you want to show up in /mnt/cdrom
# when the LiveCD is booted in the overlay. The layout that is in the overlay
# mirrors how it will be on the LiveCD.
livecd/overlay: /root/2006.0/overlay

# This directory will be laid over the rootfs of the LiveCD.
#livecd/root_overlay: /tmp/livecd-root-overlay

# list of modules that you want to blacklist for hotplug
#livecd/modblacklist: siimage eth1394

# bootsplash theme to use - must be present in /etc/bootsplash of the
# livecd-stage1.
#livecd/bootsplash: livecd-2004.1

# livecd/rcadd and livecd/rcdel allow for programs to be added or removed
# from a specific runlevel
#livecd/rcadd: mkxf86config:default
#livecd/rcdel: net.eth0:boot

# livecd/fsscript is a script that is copied into the build root
# and then executed. Use it to modify your build root in any way that
# you choose.
#livecd/fsscript: /tmp/fsscript.sh

# livecd/xinitrc lets you provide catalyst with an xinitrc for XLiveCDs.
#livecd/xinitrc: /tmp/xinitrc

# There *must* be a kernel config specified or else Catalyst will fail the
# build
boot/kernel: livecd32 livecd64

boot/kernel/livecd32/sources: sys-kernel/hppa-sources
boot/kernel/livecd32/config: /root/2006.0/kconfig-hppa32

# per-kernel arguments for genkernel
#boot/kernel/gentoo/gk_kernargs: --makeopts=-j2

boot/kernel/livecd64/sources: sys-kernel/hppa-sources
boot/kernel/livecd64/config: /root/2006.0/kconfig-hppa64
boot/kernel/livecd64/gk_kernargs:  --kernel-cc=hppa64-linux-gcc --kernel-ld=hppa64-linux-ld 
# per-kernel arguments for genkernel
#boot/kernel/smp/gk_kernargs: --makeopts=-j1

#this next line sets any USE settings you want exported to the environment for
#your kernel build *and* during the build of any kernel-dependent packages
#boot/kernel/gentoo/use: pcmcia usb
#boot/kernel/smp/use: pcmcia usb

#use this next option to add an extension to the name of your kernel. This
#allows you to have 2 identical kernels on the livecd built with different
#options, and each with their own modules dir in /lib/modules (otherwise
#the second kernel would overwrite the first modules directory.
boot/kernel/livecd32/extraversion: livecd32
boot/kernel/livecd64/extraversion: livecd64

#this next line is for merging kernel-dependent packages after your kernel
#is built. This is where you merge third-party ebuilds that contain kernel
#modules.
#boot/kernel/livecd32/packages:
#	iptables
#	pcmcia-cs
	
#boot/kernel/livecd64/packages:
#	iptables
#	pcmcia-cs

# remove gcc from the list if you want distcc
livecd/unmerge:
	autoconf
	automake
	gcc
	binutils
	gcc-hppa64
	binutils-hppa64
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
	miscfiles
	
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
	/usr/share/gtk-doc
	/usr/share/man
	/root/.ccache

livecd/rm:
	/lib/*.a
	/usr/lib/*.a
	/usr/lib/gcc-lib/*/*/libgcj*
	/usr/X11R6/lib/*.a
	/var/log/emerge.log
	/var/log/genkernel.log
