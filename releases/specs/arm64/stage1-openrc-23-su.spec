subarch: arm64
target: stage1
version_stamp: openrc-splitusr-@TIMESTAMP@
rel_type: 23.0-splitusr
profile: default/linux/arm64/23.0/split-usr
snapshot_treeish: @TREEISH@
source_subpath: 23.0-splitusr/stage3-arm64-openrc-splitusr-latest.tar.xz
compression_mode: pixz
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
