subarch: mipsel2_softfloat
target: stage1
version_stamp: t64-openrc-@TIMESTAMP@
interpreter: /usr/bin/qemu-mipsel
rel_type: 23.0-time64
profile: default/linux/mips/23.0/time64/mipsel/o32_sf
snapshot_treeish: @TREEISH@
source_subpath: 23.0-time64/stage3-mipsel2_softfloat-t64-openrc-latest
compression_mode: pixz
decompressor_search_order: xz
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
