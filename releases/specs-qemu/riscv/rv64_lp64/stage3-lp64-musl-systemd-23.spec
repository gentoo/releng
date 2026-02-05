subarch: rv64_lp64_musl
target: stage3
version_stamp: systemd-@TIMESTAMP@
interpreter: /usr/bin/qemu-riscv64
rel_type: 23.0-musl
profile: default/linux/riscv/23.0/rv64/lp64/musl/systemd
snapshot_treeish: @TREEISH@
source_subpath: 23.0-musl/stage1-rv64_lp64_musl-systemd-@TIMESTAMP@
compression_mode: pixz
decompressor_search_order: xz bzip2
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
binrepo_path: riscv/binpackages/23.0/rv64_lp64_musl
