subarch: mipsel3_n64
chost: mips64el-unknown-linux-gnuabi64
target: stage1
version_stamp: systemd-@TIMESTAMP@
interpreter: /usr/bin/qemu-mips64el
rel_type: 23.0-default
profile: default/linux/mips/23.0/mipsel/n64/systemd
snapshot_treeish: @TREEISH@
source_subpath: 23.0-default/stage3-mipsel3_n64-systemd-latest
compression_mode: pixz
decompressor_search_order: xz bzip2
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
