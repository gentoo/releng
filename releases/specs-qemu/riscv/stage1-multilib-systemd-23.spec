subarch: rv64_multilib
target: stage1
version_stamp: systemd-@TIMESTAMP@
cflags: -O2 -pipe
interpreter: /usr/bin/qemu-riscv64 /usr/bin/qemu-riscv32
rel_type: 23.0-default
profile: default/linux/riscv/23.0/rv64/multilib/systemd
snapshot_treeish: @TIMESTAMP@
source_subpath: 23.0-default/stage3-rv64_multilib-systemd-latest
compression_mode: pixz
decompressor_search_order: xz bzip2
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
