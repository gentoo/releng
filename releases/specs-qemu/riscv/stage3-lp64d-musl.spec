subarch: rv64_lp64d
target: stage3
version_stamp: musl-@TIMESTAMP@
interpreter: /usr/bin/qemu-riscv64
rel_type: musl
profile: default/linux/riscv/20.0/rv64gc/lp64d/musl
snapshot: @TIMESTAMP@
source_subpath: musl/stage1-rv64_lp64d-musl-@TIMESTAMP@
compression_mode: pixz
decompressor_search_order: xz bzip2
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
