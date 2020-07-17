subarch: riscv
target: stage1
version_stamp: @TIMESTAMP@
cflags: -O2 -pipe -g
rel_type: riscv64-multilib
profile: default/linux/riscv/17.0/rv64gc
snapshot: @TIMESTAMP@
source_subpath: riscv64-multilib/stage3-riscv-latest
compression_mode: pixz
decompressor_search_order: xz bzip2
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
