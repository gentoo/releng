# S390 Netboot spec file, based in HPPA Netboot spec file by Guy Martin
version_stamp: @TIMESTAMP@
snapshot_treeish: @TREEISH@
source_subpath: 23.0-default/stage3-s390x-openrc-@TIMESTAMP@
pkgcache_path: /var/tmp/catalyst/packages/23.0-default/netboot-s390x

# these shouldn't change
target:          netboot
subarch:         s390x
rel_type:        23.0-default
profile:         default/linux/s390/23.0/s390x
portage_prefix: releng
portage_confdir: @REPO_DIR@/releases/specs/s390/s390x/netboot/portage


boot/kernel:                      netboot64
boot/kernel/netboot64/sources:       sys-kernel/gentoo-sources
boot/kernel/netboot64/config: ../../kconfig/netboot64.config
boot/kernel/netboot64/gk_kernargs:   --all-ramdisk-modules

netboot/use:
 multicall
 shadow
 readline
 ssl
 unicode

netboot/packages:
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

netboot/packages/sys-apps/s390-tools/files:
	/usr/bin/ts-shell
	/usr/bin/ttyrun
	/usr/bin/iucvtty
	/usr/bin/iucvconn
	/usr/bin/dasdinfo
	/usr/bin/vmcp
	/usr/bin/vmconvert
	/usr/bin/znetconf
	/usr/bin/cio_ignore
	/usr/bin/chzcrypt
	/usr/bin/lszcrypt
	/usr/bin/chchp
	/usr/bin/lschp
	/usr/bin/lszfcp
	/usr/bin/lsqeth
	/usr/bin/chccwdev
	/usr/bin/lscss
	/usr/bin/lstape
	/usr/bin/lsdasd
	/usr/bin/scsi_logging_level
	/usr/bin/zfcpdbf
	/usr/bin/dbginfo.sh
	/usr/bin/qethconf
	/usr/bin/qetharp
	/usr/bin/tape390_crypt
	/usr/bin/tape390_display
	/usr/bin/tunedasd
	/usr/bin/dasdview
	/usr/bin/dasdfmt
	/usr/bin/fdasd
	/usr/bin/zgetdump
	/usr/bin/zipl
	/usr/bin/hyptop
	/usr/bin/chiucvallow
	/usr/bin/ziorep_traffic
	/usr/bin/ziorep_utilization
	/usr/bin/ziomon_zfcpdd
	/usr/bin/ziomon_mgr
	/usr/bin/ziomon_util
	/usr/bin/ziorep_config
	/usr/bin/ziomon_fcpconf
	/usr/bin/ziomon
	/usr/bin/lsshut
	/usr/bin/chshut
	/usr/bin/lsreipl
	/usr/bin/chreipl
	/usr/bin/cpuplugd
	/usr/bin/vmur
	/usr/bin/mon_procd
	/usr/bin/mon_fsstatd
	/usr/bin/lsluns
	/usr/bin/chmem
	/usr/bin/lsmem
	/usr/bin/xcec-bridge
	/usr/bin/ip_watcher.pl
	/usr/bin/start_hsnc.sh

netboot/packages/sys-fs/e2fsprogs/files:
	/usr/bin/chattr
	/usr/bin/lsattr
	/usr/bin/uuidgen
	/usr/bin/mklost+found
	/usr/bin/e2fsck
	/usr/bin/debugfs
	/usr/bin/mke2fs
	/usr/bin/badblocks
	/usr/bin/tune2fs
	/usr/bin/dumpe2fs
	/usr/bin/blkid
	/usr/bin/logsave
	/usr/bin/e2image
	/usr/bin/fsck
	/usr/bin/e2undo
	/usr/bin/filefrag
	/usr/bin/uuidd
	/usr/bin/resize2fs
	/usr/bin/findfs
	/usr/bin/e2label
	/usr/bin/mkfs.ext4
	/usr/bin/mkfs.ext3
	/usr/bin/mkfs.ext2
	/usr/bin/fsck.ext4
	/usr/bin/fsck.ext3
	/usr/bin/fsck.ext2
	/usr/lib64/libext2fs.so.*
	/usr/lib64/libcom_err.so.*
	/usr/lib64/libblkid.so.*
	/usr/lib64/libe2p.so.*
	/usr/lib64/e2initrd_helper
	/usr/lib64/libpthread*

netboot/packages/sys-apps/util-linux/files:
	/usr/bin/partx
	/usr/bin/delpart
	/usr/bin/rtcwake
	/usr/bin/addpart
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
	/usr/bin/raw
	/usr/bin/mkfs.bfs
	/usr/bin/sfdisk
	/usr/bin/fsck.minix
	/usr/bin/hwclock
	/usr/bin/ctrlaltdel
	/usr/bin/mkfs
	/usr/bin/mkfs.minix
	/usr/bin/blockdev
	/usr/bin/losetup
	/usr/bin/agetty
	/usr/bin/mkswap
	/usr/bin/pivot_root
	/usr/bin/fdisk
	/usr/bin/swapon
	/usr/bin/umount
	/usr/bin/dmesg
	/usr/bin/mount
	/usr/bin/swapoff
	/usr/lib64/libblkid.so.*
	/usr/lib64/libmount.so.*
	/usr/lib64/libsmartcols.so.*
	/usr/lib64/libuuid.so.*
	/usr/lib64/libfdisk.so.*

netboot/packages/app-editors/nano/files:
	/usr/bin/nano

netboot/packages/sys-libs/ncurses/files:
	/usr/lib64/libncurses.so.*
	/usr/lib64/libncursesw.so.*
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

netboot/packages/net-misc/wget/files:
	/usr/bin/wget
	/usr/lib64/libss.so.*
	/usr/lib64/libz.so.*

netboot/packages/dev-libs/openssl/files:
	/usr/lib64/libssl.so*
	/usr/lib64/libcrypto.so*

netboot/packages/net-misc/rsync/files:
	/usr/bin/rsync

netboot/packages/dev-libs/popt/files:
	/usr/lib64/libpopt.so*

netboot/packages/net-misc/dropbear/files:
	/usr/bin/dbclient
	/usr/bin/dbscp
	/usr/bin/dropbearconvert
	/usr/bin/dropbearkey
	/usr/bin/dropbearmulti
	/usr/bin/dropbear
	/usr/lib64/libcrypt*
	/usr/lib64/libnss*
	/usr/lib64/libnsl*
	/usr/lib64/libresolv*
	/usr/lib64/libnss_dns*
	/usr/lib64/ld64.so.1
	/usr/lib64/ld-*

netboot/packages/dev-libs/libtommath/files:
	/usr/lib64/libtommath.so*
	/usr/lib64/libtommath.so
	/usr/lib64/libutil*

netboot/packages/app-misc/screen/files:
	/usr/bin/screen
	/etc/screenrc
	/usr/lib64/libdl*

