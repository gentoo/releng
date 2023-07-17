subarch: mips3_multilib
target: stage3
version_stamp: systemd-@TIMESTAMP@
interpreter: /usr/bin/qemu-mipsn32 /usr/bin/qemu-mips /usr/bin/qemu-mips64
rel_type: default
profile: default/linux/mips/17.0/multilib/n32/systemd
snapshot_treeish: @TREEISH@
source_subpath: default/stage1-mips3_multilib-systemd-@TIMESTAMP@
compression_mode: pixz
decompressor_search_order: xz bzip2
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
binrepo_path: mips/binpackages/17.0/mips3_multilib
