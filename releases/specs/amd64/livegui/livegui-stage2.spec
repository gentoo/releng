subarch: amd64
version_stamp: plasma-@TIMESTAMP@
target: livecd-stage2
rel_type: default
profile: default/linux/amd64/17.1/desktop/plasma
snapshot: @TIMESTAMP@
source_subpath: default/livecd-stage1-amd64-plasma-@TIMESTAMP@
portage_confdir: @REPO_DIR@/releases/portage/livegui

livecd/bootargs: overlayfs nodhcp
livecd/depclean: no
livecd/fstype: squashfs
livecd/iso: livegui-amd64-@TIMESTAMP@.iso
livecd/type: gentoo-release-livecd
livecd/volid: Gentoo amd64 LiveGUI @TIMESTAMP@

livecd/fsscript: @REPO_DIR@/releases/specs/amd64/livegui/files/fsscript-stage2.sh
livecd/overlay: @REPO_DIR@/releases/specs/amd64/livegui/files/overlay
livecd/root_overlay: @REPO_DIR@/releases/specs/amd64/livegui/files/root_overlay
livecd/rcadd: udev|sysinit udev-mount|sysinit acpid|default dbus|default gpm|default NetworkManager|default
livecd/unmerge: net-misc/netifrc

boot/kernel: gentoo

boot/kernel/gentoo/sources: gentoo-sources
boot/kernel/gentoo/config: @REPO_DIR@/releases/kconfig/amd64/livegui-amd64-5.15.16.config

boot/kernel/gentoo/packages: --usepkg n zfs zfs-kmod
