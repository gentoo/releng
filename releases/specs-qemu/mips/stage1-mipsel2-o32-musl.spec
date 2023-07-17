subarch: mipsel2_musl
target: stage1
version_stamp: @TIMESTAMP@
interpreter: /usr/bin/qemu-mipsel
rel_type: musl
profile: default/linux/mips/17.0/mipsel/o32/musl
snapshot_treeish: @TREEISH@
source_subpath: musl/stage3-mipsel2_musl-latest
compression_mode: pixz
decompressor_search_order: xz bzip2
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
