# HPPA Netboot spec file by Guy Martin
version_stamp:  20130927
snapshot:       20130927
source_subpath: default/stage3-hppa1.1-20130927

# these shouldn't change
target:          netboot2
subarch:         hppa1.1
rel_type:        default
profile:         default/linux/hppa/13.0

# netboot2 stuff
boot/kernel:                      netboot32
boot/kernel/netboot32/sources:       sys-kernel/gentoo-sources
boot/kernel/netboot32/config:        /root/gmsoft-specs/netboot-3.10.7-gentoo-netboot32.config
boot/kernel/netboot32/gk_kernargs:   --arch-override=parisc --all-ramdisk-modules

#netboot2/busybox_config: /root/myspecs/busybox-config

netboot2/use:
 -*
 multicall
 shadow
 readline
 ssl

netboot2/packages:
	sys-boot/palo
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
	#needed for the kernel to compile 
	sys-devel/bc

netboot2/packages/sys-boot/palo/files:
	/sbin/palo
	/usr/share/palo/iplboot

netboot2/packages/sys-fs/mdadm/files:
	/sbin/mdadm

netboot2/packages/sys-fs/e2fsprogs/files:
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
	/sbin/mkfs.ext4dev
	/sbin/mkfs.ext4
	/sbin/mkfs.ext3
	/sbin/mkfs.ext2
	/sbin/fsck.ext4dev
	/sbin/fsck.ext4
	/sbin/fsck.ext3
	/sbin/fsck.ext2
	/lib/libext2fs.so.2.4
	/lib/libext2fs.so.2
	/lib/libcom_err.so.2.1
	/lib/libcom_err.so.2
	/lib/libblkid.so.1.1.0
	/lib/libblkid.so.1
	/lib/libe2p.so.2.3
	/lib/libe2p.so.2
	/usr/lib/e2initrd_helper
	/lib/libpthread-2.17.so
	/lib/libpthread.so.0

netboot2/packages/sys-fs/xfsprogs/files:
	/sbin/mkfs.xfs
	/sbin/fsck.xfs
	/sbin/xfs_repair
	/lib/libxfs.so.0.0.0
	/lib/libxfs.so.0
	/lib/libxlog.so.0.0.0
	/lib/libxlog.so.0
	/lib/librt-2.17.so
	/lib/librt.so.1


netboot2/packages/sys-apps/util-linux/files:
	/usr/sbin/partx
	/usr/sbin/delpart
	/usr/sbin/rtcwake
	/usr/sbin/addpart
	/usr/sbin/readprofile
	/usr/sbin/tunelp
	/usr/bin/mcookie
	/usr/bin/logger
	/usr/bin/setarch
	/usr/bin/script
	/usr/bin/scriptreplay
	/usr/bin/linux64
	/usr/sbin/fdformat
	/usr/bin/column
	/usr/bin/cal
	/usr/bin/ul
	/usr/bin/cytune
	/usr/bin/chrt
	/usr/bin/rename
	/usr/bin/tailf
	/usr/bin/setterm
	/usr/bin/colcrt
	/usr/bin/write
	/usr/bin/hexdump
	/usr/bin/line
	/usr/bin/namei
	/usr/bin/isosize
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
	/usr/bin/ddate
	/usr/bin/rev
	/usr/bin/linux32
	/usr/bin/chkdupexe
	/usr/bin/pg
	/usr/bin/colrm
	/sbin/cfdisk
	/sbin/raw
	/sbin/mkfs.bfs
	/sbin/sfdisk
	/sbin/fsck.minix
	/sbin/hwclock
	/sbin/ctrlaltdel
	/sbin/mkfs
	/sbin/mkfs.cramfs
	/sbin/mkfs.minix
	/sbin/blockdev
	/sbin/losetup
	/sbin/fsck.cramfs
	/sbin/agetty
	/sbin/mkswap
	/sbin/pivot_root
	/sbin/fdisk
	/sbin/swapon
	/bin/more
	/bin/umount
	/bin/dmesg
	/bin/mount
	/sbin/swapoff
	/lib/libblkid.so.1
	/lib/libblkid.so.1.1.0
	/lib/libmount.so.1
	/lib/libmount.so.1.1.0
	/lib/libuuid.so.1
	/lib/libuuid.so.1.3.0

netboot2/packages/app-editors/nano/files:
	/bin/nano

netboot2/packages/sys-libs/ncurses/files:
	/lib/libncurses.so.5.9
	/lib/libncurses.so.5
	/lib/libncursesw.so.5.9
	/lib/libncursesw.so.5
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

netboot2/packages/net-misc/wget/files:
	/usr/bin/wget
	/lib/libss.so.2.0
	/lib/libss.so.2
	/lib/libz.so.1.2.7
	/lib/libz.so.1

netboot2/packages/dev-libs/openssl/files:
	/usr/lib/libssl.so.1.0.0
	/usr/lib/libssl.so
	/usr/lib/libcrypto.so.1.0.0
	/usr/lib/libcrypto.so

netboot2/packages/net-misc/rsync/files:
	/usr/bin/rsync

netboot2/packages/dev-libs/popt/files:
	usr/lib/libpopt.so.0.0.0
	/usr/lib/libpopt.so.0
	/usr/lib/libpopt.so

netboot2/packages/net-misc/dropbear/files:
	/usr/bin/dbclient
	/usr/bin/dbscp
	/usr/bin/dropbearconvert
	/usr/bin/dropbearkey
	/usr/bin/dropbearmulti
	/usr/sbin/dropbear
	/lib/libcrypt-2.17.so
	/lib/libcrypt.so.1
	/lib/libnss_compat-2.17.so
	/lib/libnss_compat.so.2
	/lib/libnsl-2.17.so
	/lib/libnsl.so.1

netboot2/packages/dev-libs/libtommath/files:
	/usr/lib/libtommath.so.0.0.41
	/usr/lib/libtommath.so.0
	/usr/lib/libtommath.so
	/lib/libutil-2.17.so
	/lib/libutil.so.1

netboot2/packages/app-misc/screen/files:
	/usr/bin/screen
	/etc/screenrc
	/lib/libdl-2.17.so
	/lib/libdl.so.2

