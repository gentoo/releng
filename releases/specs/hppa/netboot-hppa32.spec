# HPPA Netboot spec file by Guy Martin
version_stamp: @TIMESTAMP@
snapshot_treeish: @TREEISH@
source_subpath: default/stage3-hppa1.1-openrc-@TIMESTAMP@
pkgcache_path: /var/tmp/catalyst/packages/default/netboot-hppa32

# these shouldn't change
target:          netboot
subarch:         hppa1.1
rel_type:        default
profile:         default/linux/hppa/17.0

# netboot stuff
boot/kernel:                      hppa32
boot/kernel/hppa32/sources:       sys-kernel/gentoo-sources
boot/kernel/hppa32/config:        @REPO_DIR@/releases/kconfig/hppa/hppa32.config
boot/kernel/hppa32/gk_kernargs:   --all-ramdisk-modules

netboot/use:
 -*
 python_targets_python3_10
 python_single_target_python3_10
 libtommath # dropbear requires libtomcrypt[libtommath]
 multicall
 shadow
 readline
 ssl
 unicode
 xml
 gnu # for app-alternatives/cpio

netboot/packages:
	sys-boot/palo
	sys-fs/lvm2
	sys-fs/mdadm
	sys-fs/e2fsprogs
	sys-fs/reiserfsprogs
	sys-fs/xfsprogs
	sys-apps/util-linux
	app-editors/nano
	sys-libs/ncurses
	dev-libs/popt
	net-misc/wget
	net-misc/rsync
	dev-libs/libtommath
	net-misc/dropbear
	dev-libs/openssl
	app-misc/screen

netboot/packages/sys-boot/palo/files:
	/sbin/palo
	/usr/share/palo/iplboot

netboot/packages/sys-fs/mdadm/files:
	/sbin/mdadm

netboot/packages/sys-fs/e2fsprogs/files:
	/usr/bin/chattr
	/usr/bin/lsattr
	/usr/bin/uuidgen
	/usr/sbin/mklost+found
	/sbin/e2fsck
	/sbin/debugfs
	/sbin/mke2fs
	/sbin/badblocks
	/sbin/tune2fs
	/sbin/dumpe2fs
	/sbin/blkid
	/sbin/logsave
	/sbin/e2image
	/sbin/fsck
	/sbin/e2undo
	/usr/sbin/filefrag
	/usr/sbin/uuidd
	/sbin/resize2fs
	/sbin/findfs
	/sbin/e2label
	/sbin/mkfs.ext4
	/sbin/mkfs.ext3
	/sbin/mkfs.ext2
	/sbin/fsck.ext4
	/sbin/fsck.ext3
	/sbin/fsck.ext2
	/lib/libext2fs.so.*
	/lib/libcom_err.so.*
	/lib/libe2p.so.*
	/usr/lib/e2initrd_helper
	/lib/libpthread*

netboot/packages/sys-fs/xfsprogs/files:
	/sbin/mkfs.xfs
	/sbin/fsck.xfs
	/sbin/xfs_repair
	/lib/librt*


netboot/packages/sys-apps/util-linux/files:
	/usr/sbin/partx
	/usr/sbin/delpart
	/usr/sbin/rtcwake
	/usr/sbin/addpart
	/usr/bin/logger
	/usr/bin/setarch
	/usr/bin/linux64
	/usr/bin/column
	/usr/bin/cal
	/usr/bin/chrt
	/usr/bin/rename
	/usr/bin/colcrt
	/usr/bin/hexdump
	/usr/bin/namei
	/usr/bin/look
	/usr/bin/ipcs
	/usr/bin/parisc
	/usr/bin/flock
	/usr/bin/ionice
	/usr/bin/renice
	/usr/bin/getopt
	/usr/bin/parisc32
	/usr/bin/col
	/usr/bin/taskset
	/usr/bin/ipcrm
	/usr/bin/parisc64
	/usr/bin/whereis
	/usr/bin/setsid
	/usr/bin/rev
	/usr/bin/linux32
	/usr/bin/colrm
	/sbin/raw
	/sbin/mkfs.bfs
	/sbin/sfdisk
	/sbin/fsck.minix
	/sbin/hwclock
	/sbin/ctrlaltdel
	/sbin/mkfs
	/sbin/mkfs.minix
	/sbin/blockdev
	/sbin/losetup
	/sbin/agetty
	/sbin/mkswap
	/sbin/pivot_root
	/sbin/fdisk
	/sbin/swapon
	/bin/umount
	/bin/dmesg
	/bin/mount
	/sbin/swapoff
	/lib/libblkid.so.*
	/lib/libfdisk.so.*
	/lib/libmount.so.*
	/lib/libsmartcols.so.*
	/lib/libuuid.so.*
	/usr/lib/libblkid.so
	/usr/lib/libfdisk.so
	/usr/lib/libmount.so
	/usr/lib/libsmartcols.so
	/usr/lib/libuuid.so

netboot/packages/app-editors/nano/files:
	/bin/nano

netboot/packages/sys-libs/ncurses/files:
	/lib/libncurses.so.*
	/lib/libncursesw.so.*
	/etc/terminfo
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

netboot/packages/net-misc/wget/files:
	/usr/bin/wget
	/lib/libss.so.*
	/lib/libz.so.*

netboot/packages/dev-libs/openssl/files:
	/usr/lib/libssl.so*
	/usr/lib/libcrypto.so*

netboot/packages/net-misc/rsync/files:
	/usr/bin/rsync

netboot/packages/dev-libs/popt/files:
	/usr/lib/libpopt.so*

netboot/packages/net-misc/dropbear/files:
	/usr/bin/dbclient
	/usr/bin/dbscp
	/usr/bin/dropbearconvert
	/usr/bin/dropbearkey
	/usr/bin/dropbearmulti
	/usr/sbin/dropbear
	/lib/libcrypt*
	/lib/libnss_compat*
	/lib/libnsl*
	/lib/libresolv*
	/lib/libnss_dns*

netboot/packages/dev-libs/libtommath/files:
	/usr/lib/libtommath.so*
	/usr/lib/libtommath.so
	/lib/libutil*

netboot/packages/app-misc/screen/files:
	/usr/bin/screen
	/etc/screenrc
	/lib/libdl*

