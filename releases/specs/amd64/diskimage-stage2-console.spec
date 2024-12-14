subarch: amd64
version_stamp: @TIMESTAMP@
target: diskimage-stage2
rel_type: 23.0-default
profile: default/linux/amd64/23.0/no-multilib/systemd
snapshot_treeish: @TREEISH@
source_subpath: 23.0-default/diskimage-stage1-amd64-@TIMESTAMP@
portage_confdir: @REPO_DIR@/releases/portage/diskimage

diskimage/qcow2: di-amd64-console-@TIMESTAMP@.qcow2
diskimage/type: console

boot/kernel: gentoo

boot/kernel/gentoo/distkernel: yes
boot/kernel/gentoo/dracut_args: --xz --no-hostonly -a dmsquash-live -a mdraid -o i18n -o usrmount -o lunmask -o qemu -o qemu-net -o nvdimm -o multipath -I busybox
boot/kernel/gentoo/config: /root/releng/releases/kconfig/amd64/dist-amd64-livecd.config
