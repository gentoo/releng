# S390 Netboot spec file, based in HPPA Netboot spec file by Guy Martin
version_stamp: 20140929
snapshot: 20140929
source_subpath: default/stage3-s390x-latest

# these shouldn't change
target:          netboot2
subarch:         s390x
rel_type:        default
profile:         default/linux/s390/13.0/s390x
portage_confdir: /root/releng/releases/weekly/specs/s390/s390x/netboot/portage


boot/kernel:                      netboot64
boot/kernel/netboot64/sources:       sys-kernel/gentoo-sources
boot/kernel/netboot64/config: ../../kconfig/netboot64.config
boot/kernel/netboot64/gk_kernargs:   --arch-override=s390 --all-ramdisk-modules

netboot2/use:
 -*
 multicall
 shadow
 readline
 ssl

netboot2/packages:
	sys-apps/s390-tools
	sys-fs/e2fsprogs
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

netboot2/packages/sys-apps/s390-tools/files:
	/sbin/ts-shell
	/sbin/ttyrun
	/sbin/iucvtty
	/sbin/iucvconn
	/sbin/dasdinfo
	/sbin/vmcp
	/sbin/vmconvert
	/sbin/znetconf
	/sbin/cio_ignore
	/sbin/chzcrypt
	/sbin/lszcrypt
	/sbin/chchp
	/sbin/lschp
	/sbin/lszfcp
	/sbin/lsqeth
	/sbin/chccwdev
	/sbin/lscss
	/sbin/lstape
	/sbin/lsdasd
	/sbin/scsi_logging_level
	/sbin/zfcpdbf
	/sbin/dbginfo.sh
	/sbin/qethconf
	/sbin/qetharp
	/sbin/tape390_crypt
	/sbin/tape390_display
	/sbin/tunedasd
	/sbin/dasdview
	/sbin/dasdfmt
	/sbin/fdasd
	/sbin/zgetdump
	/sbin/zipl
	/usr/sbin/hyptop
	/usr/sbin/chiucvallow
	/usr/sbin/ziorep_traffic
	/usr/sbin/ziorep_utilization
	/usr/sbin/ziomon_zfcpdd
	/usr/sbin/ziomon_mgr
	/usr/sbin/ziomon_util
	/usr/sbin/ziorep_config
	/usr/sbin/ziomon_fcpconf
	/usr/sbin/ziomon
	/usr/sbin/lsshut
	/usr/sbin/chshut
	/usr/sbin/lsreipl
	/usr/sbin/chreipl
	/usr/sbin/cpuplugd
	/usr/sbin/vmur
	/usr/sbin/mon_procd
	/usr/sbin/mon_fsstatd
	/usr/sbin/lsluns
	/usr/sbin/chmem
	/usr/sbin/lsmem
	/usr/sbin/xcec-bridge
	/usr/sbin/ip_watcher.pl
	/usr/sbin/start_hsnc.sh

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
	/lib64/libext2fs.so.*
	/lib64/libcom_err.so.*
	/lib64/libblkid.so.*
	/lib64/libe2p.so.*
	/usr/lib64/e2initrd_helper
	/lib64/libpthread*

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
	/usr/bin/cytune
	/usr/bin/chrt
	/usr/bin/rename
	/usr/bin/tailf
	/usr/bin/colcrt
	/usr/bin/write
	/usr/bin/hexdump
	/usr/bin/namei
	/usr/bin/isosize
	/usr/bin/look
	/usr/bin/ipcs
	/usr/bin/flock
	/usr/bin/ionice
	/usr/bin/renice
	/usr/bin/getopt
	/usr/bin/col
	/usr/bin/taskset
	/usr/bin/ipcrm
	/usr/bin/whereis
	/usr/bin/setsid
	/usr/bin/rev
	/usr/bin/linux32
	/usr/bin/s390x
	/usr/bin/s390
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
	/lib64/libblkid.so.*
	/lib64/libmount.so.*
	/lib64/libuuid.so.*

netboot2/packages/app-editors/nano/files:
	/bin/nano

netboot2/packages/sys-libs/ncurses/files:
	/lib64/libncurses.so.*
	/lib64/libncursesw.so.*
	/etc/terminfo
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

netboot2/packages/net-misc/wget/files:
	/usr/bin/wget
	/lib64/libss.so.*
	/lib64/libz.so.*

netboot2/packages/dev-libs/openssl/files:
	/usr/lib64/libssl.so*
	/usr/lib64/libcrypto.so*

netboot2/packages/net-misc/rsync/files:
	/usr/bin/rsync

netboot2/packages/dev-libs/popt/files:
	/usr/lib64/libpopt.so*

netboot2/packages/net-misc/dropbear/files:
	/usr/bin/dbclient
	/usr/bin/dbscp
	/usr/bin/dropbearconvert
	/usr/bin/dropbearkey
	/usr/bin/dropbearmulti
	/usr/sbin/dropbear
	/lib64/libcrypt*
	/lib64/libnss*
	/lib64/libnsl*
	/lib64/libresolv*
	/lib64/libnss_dns*
	/lib64/ld64.so.1
	/lib64/ld-*

netboot2/packages/dev-libs/libtommath/files:
	/usr/lib64/libtommath.so*
	/usr/lib64/libtommath.so
	/lib64/libutil*

netboot2/packages/app-misc/screen/files:
	/usr/bin/screen
	/etc/screenrc
	/lib64/libdl*

