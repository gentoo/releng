subarch: armv5tel
version_stamp: t64-openrc-@TIMESTAMP@
target: stage1
rel_type: 23.0-time64
profile: default/linux/arm/23.0/time64/armv5te
snapshot_treeish: @TREEISH@
source_subpath: 23.0-time64/stage3-armv5tel-t64-openrc-latest.tar.xz
compression_mode: pixz
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
