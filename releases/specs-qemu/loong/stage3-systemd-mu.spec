subarch: loong
version_stamp: systemd-mergedusr-@TIMESTAMP@
target: stage3
rel_type: mergedusr
profile: default/linux/loong/22.0/la64v100/lp64d/systemd/merged-usr
snapshot_treeish: @TIMESTAMP@
source_subpath: mergedusr/stage1-loong-systemd-mergedusr-@TIMESTAMP@
compression_mode: pixz
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
interpreter: /usr/bin/qemu-loongarch64
