subarch: mips3_n64
target: stage1
version_stamp: systemd-@TIMESTAMP@
interpreter: /usr/bin/qemu-mips64
rel_type: default
profile: default/linux/mips/17.0/n64/systemd
snapshot_treeish: @TIMESTAMP@
source_subpath: default/stage3-mips3_n64-systemd-latest
compression_mode: pixz
decompressor_search_order: xz bzip2
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
