subarch: mips2_softfloat
target: stage1
version_stamp: systemd-@TIMESTAMP@
interpreter: /usr/bin/qemu-mips
rel_type: 23.0-default
profile: default/linux/mips/23.0/o32_sf/systemd
snapshot_treeish: @TREEISH@
source_subpath: 23.0-default/stage3-mips2_softfloat-systemd-latest
compression_mode: pixz
decompressor_search_order: xz
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
