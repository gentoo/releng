subarch: arm64
target: stage1
version_stamp: systemd-@TIMESTAMP@
rel_type: 23.0-default
profile: default/linux/arm64/23.0/systemd
snapshot_treeish: @TIMESTAMP@
source_subpath: 23.0-default/stage3-arm64-systemd-latest.tar.xz
compression_mode: pixz
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
