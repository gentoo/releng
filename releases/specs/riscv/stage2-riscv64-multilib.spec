subarch: riscv
target: stage2
version_stamp: @TIMESTAMP@
cflags: -O2 -pipe -g
rel_type: riscv64-multilib
profile: default/linux/riscv/17.0/rv64gc
snapshot: @TIMESTAMP@
source_subpath: riscv64-multilib/stage1-riscv-@TIMESTAMP@
compression_mode: pixz
decompressor_search_order: xz bzip2
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
