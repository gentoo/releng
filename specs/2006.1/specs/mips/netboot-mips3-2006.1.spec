subarch: mips3
version_stamp: 2006.1
target: netboot2
rel_type: default
profile: default-linux/mips/2006.1/generic-be/o32
snapshot: 2006.1
source_subpath: default/stage3-mips3-2006.1

chost: mips-unknown-linux-gnu
cflags: -Os -march=mips3 -pipe -fomit-frame-pointer -pie -ftracer -fforce-addr
makeopts: -j3

boot/kernel: ip28r10k ip30r10k ip32r5k ip32rm5k
boot/kernel/ip28r10k/sources: =mips-sources-2.6.16.27
boot/kernel/ip30r10k/sources: =mips-sources-2.6.16.27
boot/kernel/ip32r5k/sources: =mips-sources-2.6.16.27
boot/kernel/ip32rm5k/sources: =mips-sources-2.6.16.27

boot/kernel/ip28r10k/config: /usr/catalyst/2006.1/ip28r10k-2006_1.cf
boot/kernel/ip30r10k/config: /usr/catalyst/2006.1/ip30r10k-2006_1.cf
boot/kernel/ip32r5k/config: /usr/catalyst/2006.1/ip32r5k-2006_1.cf
boot/kernel/ip32rm5k/config: /usr/catalyst/2006.1/ip32rm5k-2006_1.cf

boot/kernel/ip28r10k/use: -doc ip28
boot/kernel/ip30r10k/use: -doc ip30
boot/kernel/ip32r5k/use: -doc
boot/kernel/ip32rm5k/use: -doc

boot/kernel/ip28r10k/gk_kernargs: --kernel-cross-compile=mips64-unknown-linux-gnu- --makeopts=-j2 --initramfs --static --no-initrdmodules --initramfs-overlay=/tmp/image
boot/kernel/ip30r10k/gk_kernargs: --kernel-cross-compile=mips64-unknown-linux-gnu- --makeopts=-j2 --initramfs --static --no-initrdmodules --initramfs-overlay=/tmp/image
boot/kernel/ip32r5k/gk_kernargs: --kernel-cross-compile=mips64-unknown-linux-gnu- --makeopts=-j2 --initramfs --static --no-initrdmodules --initramfs-overlay=/tmp/image
boot/kernel/ip32rm5k/gk_kernargs: --kernel-cross-compile=mips64-unknown-linux-gnu- --makeopts=-j2 --initramfs --static --no-initrdmodules --initramfs-overlay=/tmp/image --static


netboot2/builddate: 20060804

netboot2/use:
	-*
	multicall
	readline

netboot2/packages:
	com_err
	dropbear
	dvhtool
	e2fsprogs
	elinks
	gcc
	gcc-mips64
	glibc
	jfsutils
	mdadm
	mutt
	nano
	ncurses
	popt
	pork
	portmap
	reiserfsprogs
	rsync
	sdparm
	ss
	ttcp
	util-linux
	xfsprogs

netboot2/packages/com_err/files:
	/lib/libcom_err.so
	/lib/libcom_err.so.2
	/lib/libcom_err.so.2.1
	/usr/bin/compile_et
	/usr/lib/libcom_err.so

netboot2/packages/dropbear/files:
	/usr/bin/dbclient
	/usr/bin/dbscp
	/usr/bin/dropbearconvert
	/usr/bin/dropbearkey
	/usr/bin/dropbearmulti
	/usr/sbin/dropbear

netboot2/packages/dvhtool/files:
	/usr/sbin/dvhtool

netboot2/packages/e2fsprogs/files:
	/bin/chattr
	/bin/lsattr
	/bin/uuidgen
	/lib/libblkid.so
	/lib/libblkid.so.1
	/lib/libblkid.so.1.0
	/lib/libe2p.so
	/lib/libe2p.so.2
	/lib/libe2p.so.2.3
	/lib/libext2fs.so
	/lib/libext2fs.so.2
	/lib/libext2fs.so.2.4
	/lib/libuuid.so
	/lib/libuuid.so.1
	/lib/libuuid.so.1.2
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
	/usr/lib/libblkid.so
	/usr/lib/libe2p.so
	/usr/lib/libext2fs.so
	/usr/lib/libuuid.so
	/usr/sbin/mklost+found

netboot2/packages/gcc/files:
	/lib/libgcc_s.so.1	

netboot2/packages/glibc/files:
	/etc/ld.so.cache
	/lib/ld-2.3.6.so
	/lib/ld.so.1
	/lib/libc-2.3.6.so
	/lib/libc.so.6
	/lib/libcrypt-2.3.6.so
	/lib/libcrypt.so.1
	/lib/libdl-2.3.6.so
	/lib/libdl.so.2
	/lib/libm-2.3.6.so
	/lib/libm.so.6
	/lib/libnss_compat-2.3.6.so
	/lib/libnss_compat.so.2
	/lib/libnss_dns-2.3.6.so
	/lib/libnss_dns.so.2
	/lib/libnss_files-2.3.6.so
	/lib/libnss_files.so.2
	/lib/libnss_hesiod-2.3.6.so
	/lib/libnss_hesiod.so.2
	/lib/libnss_nis-2.3.6.so
	/lib/libnss_nis.so.2
	/lib/libnss_nisplus-2.3.6.so
	/lib/libnss_nisplus.so.2
	/lib/libpthread-0.10.so
	/lib/libpthread.so.0
	/lib/libresolv-2.3.6.so
	/lib/libresolv.so.2
	/lib/librt-2.3.6.so
	/lib/librt.so.1
	/lib/libutil-2.3.6.so
	/lib/libutil.so.1
	/usr/bin/ldd
	/usr/lib/libc.so
	/usr/lib/libcrypt.so
	/usr/lib/libdl.so
	/usr/lib/libpthread.so
	/usr/lib/libresolv.so
	/usr/lib/librt.so
	/usr/lib/libutil.so

netboot2/packages/jfsutils/files:
	/sbin/fsck.jfs
	/sbin/jfs_fsck
	/sbin/jfs_mkfs
	/sbin/jfs_tune
	/sbin/mkfs.jfs

netboot2/packages/mdadm/files:
	/etc/mdadm.conf
	/sbin/mdadm

netboot2/packages/nano/files:
	/bin/nano
	/bin/rnano
	/usr/bin/nano

netboot2/packages/ncurses/files:
	/etc/terminfo
	/lib/libcurses.so
	/lib/libncurses.so
	/lib/libncurses.so.5
	/lib/libncurses.so.5.4
	/usr/bin/toe
	/usr/lib/libcurses.so
	/usr/lib/libform.so
	/usr/lib/libform.so.5
	/usr/lib/libform.so.5.4
	/usr/lib/libmenu.so
	/usr/lib/libmenu.so.5
	/usr/lib/libmenu.so.5.4
	/usr/lib/libncurses.so
	/usr/lib/libpanel.so
	/usr/lib/libpanel.so.5
	/usr/lib/libpanel.so.5.4
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

netboot2/packages/popt/files:
	/usr/lib/libpopt.so
	/usr/lib/libpopt.so.0
	/usr/lib/libpopt.so.0.0.0

netboot2/packages/portmap/files:
	/sbin/portmap

netboot2/packages/reiserfsprogs/files:
	/sbin/fsck.reiserfs
	/sbin/mkfs.reiserfs
	/sbin/mkreiserfs
	/sbin/reiserfsck
	/sbin/reiserfstune

netboot2/packages/rsync/files:
	/usr/bin/rsync

netboot2/packages/sdparm/files:
	/usr/bin/sdparm

netboot2/packages/ss/files:
	/lib/libss.so
	/lib/libss.so.2
	/lib/libss.so.2.0
	/usr/bin/mk_cmds
	/usr/lib/libss.so

netboot2/packages/ttcp/files:
	/usr/bin/ttcp

netboot2/packages/util-linux/files:
	/sbin/fdisk
	/sbin/mkfs
	/sbin/mkswap
	/sbin/swapoff
	/sbin/swapon
	/usr/bin/ddate
	/usr/bin/setterm
	/usr/bin/whereis

netboot2/packages/xfsprogs/files:
	/lib/libhandle.so
	/lib/libhandle.so.1
	/lib/libhandle.so.1.0.3
	/sbin/fsck.xfs
	/sbin/mkfs.xfs
	/sbin/xfs_repair
	/usr/bin/xfs_copy
	/usr/bin/xfs_growfs
	/usr/bin/xfs_info
