subarch: mips2_musl
target: stage3
version_stamp: @TIMESTAMP@
interpreter: /usr/bin/qemu-mips
rel_type: musl
profile: default/linux/mips/17.0/o32/musl
snapshot_treeish: @TREEISH@
source_subpath: musl/stage1-mips2_musl-@TIMESTAMP@
compression_mode: pixz
decompressor_search_order: xz bzip2
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
