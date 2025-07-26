subarch: mips3_n32
target: stage1
version_stamp: t64-openrc-@TIMESTAMP@
interpreter: /usr/bin/qemu-mipsn32
rel_type: 23.0-time64
profile: default/linux/mips/23.0/time64/n32
snapshot_treeish: @TREEISH@
source_subpath: 23.0-time64/stage3-mips3_n32-t64-openrc-latest
compression_mode: pixz
decompressor_search_order: xz bzip2
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
