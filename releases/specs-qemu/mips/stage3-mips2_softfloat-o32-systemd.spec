subarch: mips2_softfloat
target: stage3
version_stamp: systemd-@TIMESTAMP@
interpreter: /usr/bin/qemu-mips
rel_type: default
profile: default/linux/mips/17.0/o32/systemd
snapshot: @TIMESTAMP@
source_subpath: default/stage1-mips2_softfloat-systemd-@TIMESTAMP@
compression_mode: pixz
decompressor_search_order: xz bzip2
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
binrepo_path: mips/binpackages/17.0/mips2_o32_softfloat
