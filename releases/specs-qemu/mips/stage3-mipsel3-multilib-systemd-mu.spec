subarch: mipsel3_multilib
target: stage3
version_stamp: systemd-mergedusr-@TIMESTAMP@
interpreter: /usr/bin/qemu-mipsn32el /usr/bin/qemu-mipsel /usr/bin/qemu-mips64el
rel_type: mergedusr
profile: default/linux/mips/17.0/mipsel/multilib/n32/systemd/merged-usr
snapshot_treeish: @TIMESTAMP@
source_subpath: mergedusr/stage1-mipsel3_multilib-systemd-mergedusr-@TIMESTAMP@
compression_mode: pixz
decompressor_search_order: xz bzip2
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
binrepo_path: mips/binpackages/17.0/mipsel3_multilib
