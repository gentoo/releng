subarch: rv64_lp64
target: stage3
version_stamp: systemd-@TIMESTAMP@
cflags: -O2 -pipe
interpreter: /usr/bin/qemu-riscv64
rel_type: 23.0-default
profile: default/linux/riscv/23.0/rv64/lp64/systemd
snapshot: @TIMESTAMP@
source_subpath: 23.0-default/stage1-rv64_lp64-systemd-@TIMESTAMP@
compression_mode: pixz
decompressor_search_order: xz bzip2
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
binrepo_path: riscv/binpackages/23.0/rv64_lp64
