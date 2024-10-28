subarch: amd64
version_stamp: plasma-@TIMESTAMP@
target: livecd-stage2
rel_type: 23.0-default
profile: default/linux/amd64/23.0/desktop/plasma
snapshot_treeish: @TREEISH@
source_subpath: 23.0-default/livecd-stage1-amd64-plasma-@TIMESTAMP@
portage_confdir: @REPO_DIR@/releases/portage/livegui

livecd/bootargs: nodhcp secureconsole
livecd/depclean: no
livecd/fstype: squashfs
livecd/iso: livegui-amd64-@TIMESTAMP@.iso
livecd/type: gentoo-release-livecd
livecd/volid: gentoo-amd64-livegui

livecd/fsscript: @REPO_DIR@/releases/specs/amd64/livegui/files/fsscript-stage2.sh
livecd/rcadd: udev|sysinit udev-mount|sysinit acpid|default dbus|default gpm|default NetworkManager|default elogind|boot
livecd/unmerge: net-misc/netifrc

livecd/empty:
	/var/db/repos
	/usr/src

boot/kernel: gentoo

boot/kernel/gentoo/distkernel: yes
boot/kernel/gentoo/dracut_args: --xz --no-hostonly -a dmsquash-live -a mdraid -o btrfs -o crypt -o i18n -o usrmount -o lunmask -o qemu -o qemu-net -o nvdimm -o multipath -i /lib/keymaps /lib/keymaps -I busybox
boot/kernel/gentoo/packages: --usepkg n sys-fs/zfs broadcom-sta
