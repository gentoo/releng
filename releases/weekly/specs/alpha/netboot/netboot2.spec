subarch: alpha
version_stamp: 20100329
target: netboot2
rel_type: default
profile: default/linux/alpha/10.0
snapshot: 20100329
source_subpath: default/stage3-alpha-20100329

#portage_overlay:

boot/kernel: gentoo
boot/kernel/gentoo/sources: gentoo-sources
boot/kernel/gentoo/config: config
boot/kernel/gentoo/gk_kernargs: --all-ramdisk-modules --makeopts=-j4 --lvm --dmraid --firmware --firmware-dir=/usr/src/linux/firmware



#netboot2/builddate: 20100339
netboot2/busybox_config: bs.conf


netboot2/use:
	-*
	multicall

netboot2/packages:
	dropbear
	e2fsprogs
	e2fsprogs-libs
	glibc
	lvm2
	mdadm
	nano
	ncurses
	openssl
	popt
	portmap
	rsync
	sdparm
	util-linux
	wget
	xfsprogs

netboot2/packages/dropbear/files:
	/usr/bin/dbclient
	/usr/bin/dbscp
	/usr/bin/dropbearconvert
	/usr/bin/dropbearkey
	/usr/bin/dropbearmulti
	/usr/sbin/dropbear

netboot2/packages/e2fsprogs/files:
	/bin/chattr
	/bin/lsattr
	/bin/uuidgen
	/sbin/badblocks
	/sbin/blkid
	/sbin/debugfs
	/sbin/dumpe2fs
	/sbin/e2fsck
	/sbin/e2image
	/sbin/e2label
	/sbin/filefrag
	/sbin/findfs
	/sbin/fsck
	/sbin/fsck.ext2
	/sbin/fsck.ext3
	/sbin/logsave
	/sbin/mke2fs
	/sbin/mkfs.ext2
	/sbin/mkfs.ext3
	/sbin/resize2fs
	/sbin/tune2fs
	/usr/lib/e2initrd_helper
	/lib/libblkid.so*
	/lib/libe2p.so*
	/lib/libext2fs.so*
	/lib/libuuid.so*
	/usr/sbin/mklost+found

netboot2/packages/e2fsprogs-libs/files:
	/lib/libcom_err*
	/lib/libss.*

netboot2/packages/glibc/files:
	/lib/ld-linux.so*
	/lib/ld-*
	/lib/libc.so*
	/lib/libc-*
	/lib/libcrypt.so*
	/lib/libcrypt-*
	/lib/libdl.so*
	/lib/libdl-*
	/lib/libpthr*
	/lib/librt*
	/lib/libutil.so*
	/lib/libutil-*.so
	/lib/libz.so*
	/lib/libnss*
	/lib/libreso*

netboot2/packages/lvm2/files:
	/lib/libdevmap*
	/lib/liblvm*
	/sbin/lv*
	/sbin/vg*
	/usr/lib/liblvm*
	/usr/lib/libdevmapp*

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
	/lib/libncursesw.so*
	/usr/bin/toe
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

netboot2/packages/openssl/files:
	/usr/lib/libcrypto.so*
	/usr/lib/libssl.so*

netboot2/packages/popt/files:
	/usr/lib/libpopt.so
	/usr/lib/libpopt.so.0
	/usr/lib/libpopt.so.0.0.0

netboot2/packages/portmap/files:
	/sbin/portmap

netboot2/packages/rsync/files:
	/usr/bin/rsync

netboot2/packages/sdparm/files:
	/usr/bin/sdparm

netboot2/packages/util-linux/files:
	/sbin/fdisk
	/sbin/mkfs
	/sbin/mkswap
	/sbin/swapoff
	/sbin/swapon
	/usr/bin/ddate
	/usr/bin/setterm
	/usr/bin/whereis

netboot2/packages/wget/files:
	/usr/bin/wget

netboot2/packages/xfsprogs/files:
	/bin/xfs_copy
	/bin/xfs_growfs
	/bin/xfs_info
	/lib/libhandle.so
	/lib/libhandle.so.1
	/lib/libhandle.so.1.0.3
	/sbin/fsck.xfs
	/sbin/mkfs.xfs
	/sbin/xfs_repair

