subarch: rv64_lp64d
target: stage2
version_stamp: openrc-@TIMESTAMP@
cbuild: rv64_multilib
cflags: -O2 -pipe
rel_type: default
profile: default/linux/riscv/20.0/rv64gc/lp64d
snapshot: @TIMESTAMP@
source_subpath: default/stage1-rv64_lp64d-openrc-@TIMESTAMP@
compression_mode: pixz
decompressor_search_order: xz bzip2
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
