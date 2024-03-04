subarch: mipsel3_n32
chost: mips64el-unknown-linux-gnuabin32
target: stage1
version_stamp: systemd-@TIMESTAMP@
interpreter: /usr/bin/qemu-mipsn32el
rel_type: 23.0-default
profile: default/linux/mips/23.0/mipsel/n32/systemd
snapshot_treeish: @TREEISH@
source_subpath: 23.0-default/stage3-mipsel3_n32-systemd-latest
compression_mode: pixz
decompressor_search_order: xz bzip2
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
