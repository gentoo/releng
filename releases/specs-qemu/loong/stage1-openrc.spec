subarch: loong
version_stamp: openrc-@TIMESTAMP@
target: stage1
rel_type: default
profile: default/linux/loong/22.0/la64v100/lp64d
snapshot_treeish: @TIMESTAMP@
source_subpath: default/stage3-loong-openrc-latest
compression_mode: pixz
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
interpreter: /usr/bin/qemu-loongarch64
