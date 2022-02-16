subarch: rv64_lp64d
target: stage1
version_stamp: musl-@TIMESTAMP@
cbuild: rv64_multilib
cflags: -O2 -pipe
rel_type: musl
profile: default/linux/riscv/20.0/rv64gc/lp64d/musl
snapshot: @TIMESTAMP@
source_subpath: musl/stage3-rv64_lp64d-musl-latest
compression_mode: pixz
decompressor_search_order: xz bzip2
update_seed: yes
update_seed_command: --update --deep --newuse @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
