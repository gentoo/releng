subarch: rv32_ilp32_musl
target: stage3
version_stamp: systemd-@TIMESTAMP@
interpreter: /usr/bin/qemu-riscv32
rel_type: 23.0-musl
profile: default/linux/riscv/23.0/rv32/ilp32/musl/systemd
snapshot_treeish: @TREEISH@
source_subpath: 23.0-musl/stage1-rv32_ilp32_musl-systemd-@TIMESTAMP@
compression_mode: pixz
decompressor_search_order: xz bzip2
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
binrepo_path: riscv/binpackages/23.0/rv32_ilp32_musl
