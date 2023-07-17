subarch: mips2
target: stage1
version_stamp: openrc-@TIMESTAMP@
interpreter: /usr/bin/qemu-mips
rel_type: default
profile: default/linux/mips/17.0/o32
snapshot_treeish: @TREEISH@
source_subpath: default/stage3-mips2-openrc-latest
compression_mode: pixz
decompressor_search_order: xz bzip2
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
