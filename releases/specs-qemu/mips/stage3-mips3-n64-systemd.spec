subarch: mips3_n64
target: stage3
version_stamp: systemd-@TIMESTAMP@
interpreter: /usr/bin/qemu-mips64
rel_type: default
profile: default/linux/mips/17.0/n64/systemd
snapshot_treeish: @TREEISH@
source_subpath: default/stage1-mips3_n64-systemd-@TIMESTAMP@
compression_mode: pixz
decompressor_search_order: xz bzip2
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
