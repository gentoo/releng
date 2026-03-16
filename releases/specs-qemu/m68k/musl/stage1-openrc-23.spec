subarch: m68k_musl
version_stamp: openrc-@TIMESTAMP@
target: stage1
rel_type: 23.0-musl
profile: default/linux/m68k/23.0/musl
chost: m68k-unknown-linux-musl
snapshot_treeish: @TREEISH@
source_subpath: 23.0-musl/stage3-m68k_musl-openrc-latest
compression_mode: pixz
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
interpreter: /usr/bin/qemu-m68k
