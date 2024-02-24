subarch: mips2
target: stage1
version_stamp: systemd-@TIMESTAMP@
interpreter: /usr/bin/qemu-mips
rel_type: 23.0-default
profile: default/linux/mips/23.0/o32/systemd
snapshot_treeish: @TREEISH@
source_subpath: 23.0-default/stage3-mips2-systemd-latest
compression_mode: pixz
decompressor_search_order: xz bzip2
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
