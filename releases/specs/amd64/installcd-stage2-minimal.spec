subarch: amd64
version_stamp: @TIMESTAMP@
target: livecd-stage2
rel_type: 23.0-default
profile: default/linux/amd64/23.0/no-multilib
snapshot_treeish: @TREEISH@
source_subpath: 23.0-default/livecd-stage1-amd64-@TIMESTAMP@
portage_confdir: @REPO_DIR@/releases/portage/isos

livecd/bootargs: dokeymap nodhcp
livecd/fstype: squashfs
livecd/iso: install-amd64-minimal-@TIMESTAMP@.iso
livecd/type: gentoo-release-minimal
livecd/volid: Gentoo-amd64-@DATESTAMP@
livecd/cdtar: /usr/share/catalyst/livecd/cdtar/grub-theme-gentoo_frosted.tar.bz2

livecd/rcadd: dbus|default gpm|default NetworkManager|default

boot/kernel: gentoo

boot/kernel/gentoo/distkernel: yes
boot/kernel/gentoo/dracut_args: --xz --no-hostonly -a dmsquash-live -a dmsquash-live-ntfs -a mdraid -o btrfs -o crypt -o i18n -o usrmount -o lunmask -o qemu -o qemu-net -o nvdimm -o multipath -i /lib/keymaps /lib/keymaps -I busybox
boot/kernel/gentoo/config: @REPO_DIR@/releases/kconfig/amd64/dist-amd64-livecd.config
boot/kernel/gentoo/packages: --usepkg n net-wireless/broadcom-sta sys-fs/zfs

livecd/unmerge:
	app-admin/eselect-ctags
	app-admin/eselect-vi
	app-admin/perl-cleaner
	app-admin/python-updater
	app-portage/gentoolkit
	app-arch/cpio
	dev-build/cmake
	dev-lang/rust-bin
	dev-python/pycrypto
	perl-core/PodParser
	perl-core/Test-Harness
	sys-apps/debianutils
	sys-apps/diffutils
	sys-apps/man-db
	sys-apps/man-pages
	sys-apps/memtest86+
	sys-kernel/dracut
	sys-kernel/gentoo-kernel

livecd/empty:
	/boot
	/etc/cron.daily
	/etc/cron.hourly
	/etc/cron.monthly
	/etc/cron.weekly
	/etc/kernel/config.d
	/etc/logrotate.d
	/etc/modules.autoload.d
	/etc/rsync
	/etc/runlevels/single
	/etc/skel
	/root/.ccache
	/tmp
	/usr/local
	/usr/share/aclocal
	/usr/share/baselayout
	/usr/share/consolefonts/partialfonts
	/usr/share/consoletrans
	/usr/share/dict
	/usr/share/doc
	/usr/share/emacs
	/usr/share/et
	/usr/share/gettext
	/usr/share/glib-2.0
	/usr/share/gtk-doc
	/usr/share/i18n
	/usr/share/info
	/usr/share/lcms
	/usr/share/man
	/usr/share/rfc
	/usr/share/ss
	/usr/share/state
	/usr/share/texinfo
	/usr/share/unimaps
	/usr/share/zoneinfo
	/usr/src
	/var/cache
	/var/empty
	/var/log
	/var/spool
	/var/state
	/var/tmp

livecd/rm:
	/etc/*-
	/etc/*.old
	/etc/default/audioctl
	/etc/dispatch-conf.conf
	/etc/etc-update.conf
	/etc/hosts.bck
	/etc/issue*
	/etc/man.conf
	/etc/resolv.conf
	/root/.bash_history
	/root/.viminfo
	/usr/bin/*.static
	/usr/bin/fsck.cramfs
	/usr/bin/fsck.minix
	/usr/bin/mkfs.bfs
	/usr/bin/mkfs.cramfs
	/usr/bin/mkfs.minix
	/usr/bin/addr2line
	/usr/share/consolefonts/1*
	/usr/share/consolefonts/7*
	/usr/share/consolefonts/8*
	/usr/share/consolefonts/9*
	/usr/share/consolefonts/A*
	/usr/share/consolefonts/C*
	/usr/share/consolefonts/E*
	/usr/share/consolefonts/G*
	/usr/share/consolefonts/L*
	/usr/share/consolefonts/M*
	/usr/share/consolefonts/R*
	/usr/share/consolefonts/a*
	/usr/share/consolefonts/c*
	/usr/share/consolefonts/dr*
	/usr/share/consolefonts/g*
	/usr/share/consolefonts/i*
	/usr/share/consolefonts/k*
	/usr/share/consolefonts/l*
	/usr/share/consolefonts/r*
	/usr/share/consolefonts/s*
	/usr/share/consolefonts/t*
	/usr/share/consolefonts/v*
	/usr/share/misc/*.old
