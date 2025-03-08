subarch: rv64_lp64d
version_stamp: @TIMESTAMP@
target: diskimage-stage2
rel_type: 23.0-default
profile: default/linux/riscv/23.0/rv64/lp64d/systemd
snapshot_treeish: @TREEISH@
source_subpath: 23.0-default/diskimage-stage1-rv64_lp64d-console-@TIMESTAMP@
portage_confdir: @REPO_DIR@/releases/portage/diskimage-qemu

diskimage/qcow2: di-rv64_lp64d-console-@TIMESTAMP@.qcow2
diskimage/type: console

boot/kernel: gentoo

boot/kernel/gentoo/distkernel: yes
boot/kernel/gentoo/dracut_args: --xz --no-hostonly -a dmsquash-live -a mdraid -o i18n -o usrmount -o lunmask -o qemu -o qemu-net -o nvdimm -o multipath -I busybox
