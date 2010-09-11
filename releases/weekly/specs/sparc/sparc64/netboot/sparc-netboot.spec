# $Id: sparc-netboot.spec,v 1.7 2010/01/28 23:10:59 tiago Exp $

# Use testing versions of genkernel.
#portage_confdir:	/etc/portage
# Use special versions of dropbear, and genkernel.
#portage_overlay:	/usr/local/portage
profile:		default/linux/sparc/10.0
rel_type:		default
snapshot:		20100906
source_subpath:		default/stage3-sparc64-20100906
subarch:		sparc64
target:			netboot2
version_stamp:		20100906

boot/kernel:			gentoo
boot/kernel/gentoo/config:	sparc-netboot-kernel.conf
boot/kernel/gentoo/gk_kernargs:	--makeopts=-j33
boot/kernel/gentoo/sources:	gentoo-sources

netboot2/busybox_config:	sparc-netboot-busybox.conf
netboot2/packages:
	dropbear
	e2fsprogs
	e2fsprogs-libs
	mdadm
	nano
	ncurses
# bug 300368
	portmap
	qla-fc-firmware
	sdparm
	util-linux
netboot2/use:
	-*
	multicall

netboot2/packages/dropbear/files:
	/usr/bin/dbclient
	/usr/bin/dbscp
	/usr/bin/dropbearconvert
	/usr/bin/dropbearkey
	/usr/bin/dropbearmulti
# bug 300368
	/usr/bin/scp
	/usr/sbin/dropbear

netboot2/packages/e2fsprogs/files:
	/lib/libe2p.so*
	/lib/libext2fs.so*
	/sbin/badblocks
	/sbin/debugfs
	/sbin/dumpe2fs
	/sbin/e2fsck
	/sbin/e2image
	/sbin/e2label
	/sbin/findfs
	/sbin/fsck
	/sbin/fsck.ext2
	/sbin/fsck.ext3
	/sbin/fsck.ext4
	/sbin/fsck.ext4dev
	/sbin/logsave
	/sbin/mke2fs
	/sbin/mkfs.ext2
	/sbin/mkfs.ext3
	/sbin/mkfs.ext4
	/sbin/mkfs.ext4dev
	/sbin/resize2fs
	/sbin/tune2fs
	/usr/bin/chattr
	/usr/bin/lsattr
	/usr/lib/e2initrd_helper
	/usr/lib/libe2p.so*
	/usr/lib/libext2fs.so*
	/usr/sbin/filefrag
	/usr/sbin/mklost+found

netboot2/packages/e2fsprogs-libs/files:
	/lib/libcom_err.so*
	/lib/libss.so*
	/usr/bin/compile_et
	/usr/bin/mk_cmds
	/usr/lib/libcom_err.so*
	/usr/lib/libss.so*

netboot2/packages/mdadm/files:
	/etc/mdadm.conf
	/sbin/mdadm

netboot2/packages/nano/files:
	/bin/nano
	/bin/rnano
	/usr/bin/nano

netboot2/packages/ncurses/files:
	/etc/terminfo
	/lib/libcurses.so*
	/lib/libncurses.so*
	/usr/bin/toe
	/usr/lib/libcurses.so*
	/usr/lib/libform.so*
	/usr/lib/libmenu.so*
	/usr/lib/libncurses.so*
	/usr/lib/libpanel.so*
	/usr/lib/terminfo
	/usr/share/tabset/std
	/usr/share/tabset/stdcrt
	/usr/share/tabset/vt100
	/usr/share/tabset/vt300
	/usr/share/terminfo/a/ansi
	/usr/share/terminfo/d/dumb
	/usr/share/terminfo/e/eterm
	/usr/share/terminfo/l/linux
	/usr/share/terminfo/r/rxvt
	/usr/share/terminfo/s/screen
	/usr/share/terminfo/s/sun
	/usr/share/terminfo/v/vt100
	/usr/share/terminfo/v/vt102
	/usr/share/terminfo/v/vt200
	/usr/share/terminfo/v/vt220
	/usr/share/terminfo/v/vt52
	/usr/share/terminfo/x/xterm
	/usr/share/terminfo/x/xterm-color
	/usr/share/terminfo/x/xterm-xfree86

netboot2/packages/portmap/files:
	/sbin/portmap
	/usr/sbin/pmap_set
	/usr/sbin/pmap_dump

netboot2/packages/qla-fc-firmware/files:
	/lib/firmware/ql2200_fw.bin*
	/usr/share/doc/qla-fc-firmware-*/LICENSE

netboot2/packages/sdparm/files:
	/usr/bin/sdparm

netboot2/packages/util-linux/files:
	/lib/libblkid.so*
	/lib/libuuid.so*
	/sbin/fdisk
	/usr/lib/libblkid.so*
	/usr/lib/libuuid.so*
# glibc
	/etc/ld.so.cache
	/lib/ld-*.so*
	/lib/ld-linux.so*
	/lib/libc-*.so*
	/lib/libc.so*
	/lib/libcrypt-*.so*
	/lib/libcrypt.so*
	/lib/libdl-*.so*
	/lib/libdl.so*
	/lib/libnss_compat.so*
	/lib/libnss_compat-*.so*
	/lib/libnss_dns.so*
	/lib/libnss_dns-*.so*
	/lib/libnss_files.so*
	/lib/libnss_files-*.so*
	/lib/libpthread-*.so*
	/lib/libpthread.so*
	/lib/libresolv.so*
	/lib/libresolv-*.so*
	/lib/libutil-*.so*
	/lib/libutil.so*
