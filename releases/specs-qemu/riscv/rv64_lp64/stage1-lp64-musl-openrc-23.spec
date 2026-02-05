subarch: rv64_lp64_musl
target: stage1
chost: riscv64-unknown-linux-musl
version_stamp: openrc-@TIMESTAMP@
interpreter: /usr/bin/qemu-riscv64
rel_type: 23.0-musl
profile: default/linux/riscv/23.0/rv64/lp64/musl
snapshot_treeish: @TREEISH@
source_subpath: 23.0-musl/stage3-rv64_lp64_musl-openrc-latest
compression_mode: pixz
decompressor_search_order: xz bzip2
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
