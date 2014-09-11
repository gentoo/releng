subarch: s390x
version_stamp:  20130301
target: netboot2
rel_type: default
profile: default/linux/s390/13.0/s390x
snapshot:  20130301
source_subpath: default/stage3-s390x-20130112

#portage_overlay:

boot/kernel: gentoo
boot/kernel/gentoo/sources: gentoo-sources
boot/kernel/gentoo/config: config
boot/kernel/gentoo/gk_kernargs: --all-ramdisk-modules --lvm --dmraid --firmware --firmware-dir=/usr/src/linux/firmware --arch-override=s390



#netboot2/builddate: 20100339
netboot2/busybox_config: bs.conf


netboot2/use:
	-*
	multicall

netboot2/packages:
	bzip2
	dropbear
	e2fsprogs
	e2fsprogs-libs
	glibc
	lvm2
	nano
	ncurses
	openssl
	openssh
	popt
	portmap
	rsync
	s390-tools
	tar
	util-linux
	wget

netboot2/packages/bzip2/files:
	/bin/bunzip2
	/bin/bzcat
	/bin/bzip2
	/lib64/libbz2.so*

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
	/sbin/fsck.ext*
	/sbin/logsave
	/sbin/mke2fs
	/sbin/mkfs.ext*
	/sbin/resize2fs
	/sbin/tune2fs
	/usr/lib64/e2initrd_helper
	/lib64/libblkid.so*
	/lib64/libe2p.so*
	/lib64/libext2fs.so*
	/lib64/libuuid.so*
	/usr/sbin/mklost+found

netboot2/packages/e2fsprogs-libs/files:
	/lib64/libcom_err*
	/lib64/libss.*

netboot2/packages/glibc/files:
	/lib64/ld-linux.so*
	/lib64/ld-*
	/lib64/libc.so*
	/lib64/libc-*
	/lib64/libcrypt.so*
	/lib64/libcrypt-*
	/lib64/libdl.so*
	/lib64/libdl-*
	/lib64/libpthr*
	/lib64/librt*
	/lib64/libutil.so*
	/lib64/libutil-*.so
	/lib64/libz.so*
	/lib64/libnss*
	/lib64/libreso*

netboot2/packages/lvm2/files:
	/lib64/libdevmap*
	/lib64/liblvm*
	/sbin/lv*
	/sbin/vg*
	/usr/lib64/liblvm*
	/usr/lib64/libdevmapp*

netboot2/packages/nano/files:
	/bin/nano
	/bin/rnano
	/usr/bin/nano

netboot2/packages/ncurses/files:
	/etc/terminfo
	/lib64/libcurses.so*
	/lib64/libncurses.so*
	/lib64/libncursesw.so*
	/usr/bin/toe
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

netboot2/packages/openssl/files:
	/usr/lib64/libcrypto.so*
	/usr/lib64/libssl.so*

netboot2/packages/openssh/files:
	/usr/bin/ssh

netboot2/packages/popt/files:
	/usr/lib64/libpopt.so
	/usr/lib64/libpopt.so.0
	/usr/lib64/libpopt.so.0.0.0

netboot2/packages/portmap/files:
	/sbin/portmap

netboot2/packages/rsync/files:
	/usr/bin/rsync

netboot2/packages/s390-tools/files:
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

netboot2/packages/tar/files:
	/bin/tar

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
