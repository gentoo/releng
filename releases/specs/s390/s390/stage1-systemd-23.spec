subarch: s390
version_stamp: systemd-@TIMESTAMP@
target: stage1
rel_type: 23.0-default
profile: default/linux/s390/23.0/systemd
snapshot_treeish: @TREEISH@
source_subpath: 23.0-default/stage3-s390-systemd-latest
update_seed: yes
update_seed_command: --update --deep --newuse @world
compression_mode: pixz
portage_confdir: @REPO_DIR@/releases/portage/stages
