subarch: amd64
version_stamp: 20041011
target: livecd-stage2
rel_type: default
profile: default-linux/amd64/2004.3
snapshot: 20041011
source_subpath: default/livecd-stage1-amd64-20041011

livecd/cdfstype: squashfs
livecd/archscript: /usr/lib/catalyst/livecd/runscript/x86-archscript.sh
livecd/runscript: /usr/lib/catalyst/livecd/runscript/default-runscript.sh
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/isolinux-2.08-memtest86+-cdtar.tar.bz2
livecd/iso: /var/tmp/catalyst/builds/default/install-amd64-minimal-20041011-r1.iso
livecd/bootsplash: livecd-2004.3
livecd/type: gentoo-release-minimal
livecd/modblacklist: siimage 8139cp

boot/kernel: gentoo smp

# gentoo livecd kernel
boot/kernel/gentoo/sources: sys-kernel/gentoo-dev-sources
boot/kernel/gentoo/config: kconfig/kernel-config-2.6
boot/kernel/gentoo/use: pcmcia usb -X
boot/kernel/gentoo/extraversion: up
boot/kernel/gentoo/packages:
	pcmcia-cs
	iptables
	xfsdump

# smp livecd kernel
boot/kernel/smp/sources: sys-kernel/gentoo-dev-sources
boot/kernel/smp/config: /root/livecd/kconfig/20040713-gentoo-dev-sources-2.6.7-smp-amd64.config
boot/kernel/smp/use: pcmcia usb -X
boot/kernel/smp/extraversion: smp
boot/kernel/smp/packages:
	pcmcia-cs
	iptables

# emachines livecd kernel
# boot/kernel/emachines/sources: =sys-kernel/gentoo-dev-sources-2.6.3-r1
# boot/kernel/emachines/config: /root/livecd/kconfig/20040710-gentoo-dev-sources-2.6.3-emachines-amd64.config
# boot/kernel/emachines/kernelopts: pci=noacpi noapic
# boot/kernel/emachines/use: pcmcia usb -X
# boot/kernel/emachines/extraversion: emachines
# boot/kernel/emachines/packages:
#	pcmcia-cs
#	iptables

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
	/usr/src
	/usr/share/doc
	/usr/share/man
	/root/.ccache

livecd/rm:
	/lib/*.a
	/usr/lib/*.a
	/usr/lib/gcc-lib/*/*/libgcj*
	/usr/X11R6/lib/*.a
