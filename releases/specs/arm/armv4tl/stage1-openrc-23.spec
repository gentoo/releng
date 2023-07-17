subarch: armv4tl
version_stamp: openrc-@TIMESTAMP@
target: stage1
rel_type: 23.0-default
profile: default/linux/arm/23.0/armv4t
snapshot_treeish: @TREEISH@
source_subpath: 23.0-default/stage3-armv4tl-openrc-latest.tar.xz
compression_mode: pixz
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
