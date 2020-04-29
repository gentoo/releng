profile:		default/linux/sparc/17.0/64ul
rel_type:		default
snapshot:		@TIMESTAMP@
source_subpath:		default/stage3-sparc64-@TIMESTAMP@
subarch:		sparc64
target:			netboot2
version_stamp:		@TIMESTAMP@

boot/kernel:			gentoo
boot/kernel/gentoo/gk_kernargs:	--makeopts=-j256
boot/kernel/gentoo/sources:	gentoo-sources

netboot2/packages:
	net-misc/dropbear
	sys-fs/e2fsprogs
	sys-libs/e2fsprogs-libs
	sys-fs/mdadm
	app-editors/nano
	sys-libs/ncurses
	sys-block/qla-fc-firmware
	sys-apps/sdparm
	sys-apps/util-linux
netboot2/use:
	-*
	multicall

netboot2/packages/net-misc/dropbear/files:
	/usr/bin/dbclient
	/usr/bin/dbscp
	/usr/bin/dropbearconvert
	/usr/bin/dropbearkey
	/usr/bin/dropbearmulti
	/usr/bin/scp
	/usr/sbin/dropbear

netboot2/packages/sys-fs/e2fsprogs/files:
	/lib64/libe2p.so*
	/lib64/libext2fs.so*
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
	/sbin/logsave
	/sbin/mke2fs
	/sbin/mkfs.ext2
	/sbin/mkfs.ext3
	/sbin/mkfs.ext4
	/sbin/resize2fs
	/sbin/tune2fs
	/usr/bin/chattr
	/usr/bin/lsattr
	/usr/lib64/e2initrd_helper
	/usr/lib64/libe2p.so*
	/usr/lib64/libext2fs.so*
	/usr/sbin/filefrag
	/usr/sbin/mklost+found

netboot2/packages/sys-libs/e2fsprogs-libs/files:
	/lib64/libcom_err.so*
	/lib64/libss.so*
	/usr/bin/compile_et
	/usr/bin/mk_cmds
	/usr/lib64/libcom_err.so*
	/usr/lib64/libss.so*

netboot2/packages/sys-fs/mdadm/files:
	/etc/mdadm.conf
	/sbin/mdadm

netboot2/packages/app-editors/nano/files:
	/bin/nano
	/bin/rnano
	/usr/bin/nano

netboot2/packages/sys-libs/ncurses/files:
	/etc/terminfo
	/lib64/libncurses.so*
	/usr/bin/toe
	/usr/lib64/libcurses.so*
	/usr/lib64/libform.so*
	/usr/lib64/libmenu.so*
	/usr/lib64/libncurses.so*
	/usr/lib64/libpanel.so*
	/usr/lib64/terminfo
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

netboot2/packages/sys-block/qla-fc-firmware/files:
	/lib/firmware/ql2200_fw.bin*
	/usr/share/doc/qla-fc-firmware-*/LICENSE*

netboot2/packages/sys-apps/sdparm/files:
	/usr/bin/sdparm

netboot2/packages/sys-apps/util-linux/files:
	/lib64/libblkid.so*
	/lib64/libuuid.so*
	/sbin/fdisk
	/usr/lib64/libblkid.so*
	/usr/lib64/libuuid.so*
# glibc
	/etc/ld.so.cache
	/lib64/ld-*.so*
	/lib64/ld-linux.so*
	/lib64/libc-*.so*
	/lib64/libc.so*
	/lib64/libcrypt-*.so*
	/lib64/libcrypt.so*
	/lib64/libdl-*.so*
	/lib64/libdl.so*
	/lib64/libnss_compat.so*
	/lib64/libnss_compat-*.so*
	/lib64/libnss_dns.so*
	/lib64/libnss_dns-*.so*
	/lib64/libnss_files.so*
	/lib64/libnss_files-*.so*
	/lib64/libpthread-*.so*
	/lib64/libpthread.so*
	/lib64/libresolv.so*
	/lib64/libresolv-*.so*
	/lib64/libutil-*.so*
	/lib64/libutil.so*
