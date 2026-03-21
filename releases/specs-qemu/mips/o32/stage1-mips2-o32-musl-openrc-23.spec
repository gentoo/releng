subarch: mips2_musl
chost: mips-unknown-linux-musl
target: stage1
version_stamp: openrc-@TIMESTAMP@
interpreter: /usr/bin/qemu-mips
rel_type: 23.0-musl
profile: default/linux/mips/23.0/o32/musl
snapshot_treeish: @TREEISH@
source_subpath: 23.0-musl/stage3-mips2_musl-openrc-latest
compression_mode: pixz
decompressor_search_order: xz bzip2
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
