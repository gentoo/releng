subarch: hppa1.1
target: stage3
version_stamp: systemd-mergedusr-@TIMESTAMP@
rel_type: mergedusr
profile: default/linux/hppa/17.0/systemd/merged-usr
snapshot_treeish: @TREEISH@
source_subpath: mergedusr/stage1-hppa1.1-systemd-mergedusr-@TIMESTAMP@
interpreter: /usr/bin/qemu-hppa
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
compression_mode: pixz
decompressor_search_order: xz bzip2
