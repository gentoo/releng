subarch: rv64_lp64
target: stage3
version_stamp: systemd-mergedusr-@TIMESTAMP@
cflags: -O2 -pipe
interpreter: /usr/bin/qemu-riscv64
rel_type: mergedusr
profile: default/linux/riscv/20.0/rv64gc/lp64/systemd/merged-usr
snapshot_treeish: @TIMESTAMP@
source_subpath: mergedusr/stage1-rv64_lp64-systemd-mergedusr-@TIMESTAMP@
compression_mode: pixz
decompressor_search_order: xz bzip2
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
binrepo_path: riscv/binpackages/20.0/rv64_lp64
