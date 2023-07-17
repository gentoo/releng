subarch: rv64_multilib
target: stage3
version_stamp: systemd-mergedusr-@TIMESTAMP@
cflags: -O2 -pipe
interpreter: /usr/bin/qemu-riscv64 /usr/bin/qemu-riscv32
rel_type: mergedusr
profile: default/linux/riscv/20.0/rv64gc/multilib/systemd/merged-usr
snapshot_treeish: @TREEISH@
source_subpath: mergedusr/stage1-rv64_multilib-systemd-mergedusr-@TIMESTAMP@
compression_mode: pixz
decompressor_search_order: xz bzip2
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
binrepo_path: riscv/binpackages/20.0/rv64_multilib
