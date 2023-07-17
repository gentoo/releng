subarch: mipsel3
target: stage3
version_stamp: systemd-@TIMESTAMP@
interpreter: /usr/bin/qemu-mipsel
rel_type: default
profile: default/linux/mips/17.0/mipsel/o32/systemd
snapshot_treeish: @TREEISH@
source_subpath: default/stage1-mipsel3-systemd-@TIMESTAMP@
compression_mode: pixz
decompressor_search_order: xz bzip2
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
binrepo_path: mips/binpackages/17.0/mipsel3_o32
