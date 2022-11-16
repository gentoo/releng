subarch: loong
version_stamp: systemd-mergedusr-@TIMESTAMP@
target: stage1
rel_type: default
profile: default/linux/loong/22.0/la64v100/lp64d/systemd/merged-usr
snapshot: @TIMESTAMP@
source_subpath: default/stage3-loong-systemd-mergedusr-latest
compression_mode: pixz
update_seed: no
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
interpreter: /usr/bin/qemu-loongarch64
