subarch: arm64
version_stamp: @TIMESTAMP@
target: diskimage-stage2
rel_type: 23.0-default
profile: default/linux/arm64/23.0/systemd
snapshot_treeish: @TREEISH@
source_subpath: 23.0-default/diskimage-stage1-arm64-cloudinit-@TIMESTAMP@
portage_confdir: @REPO_DIR@/releases/portage/diskimage

diskimage/qcow2: di-arm64-cloudinit-@TIMESTAMP@.qcow2
diskimage/type: cloud-init

boot/kernel: gentoo

boot/kernel/gentoo/distkernel: yes
boot/kernel/gentoo/dracut_args: --xz --no-hostonly -a dmsquash-live -a mdraid -o i18n -o usrmount -o lunmask -o qemu -o qemu-net -o nvdimm -o multipath -I busybox
boot/kernel/gentoo/config: @REPO_DIR@/releases/kconfig/arm64/arm64-5.15.12.config
