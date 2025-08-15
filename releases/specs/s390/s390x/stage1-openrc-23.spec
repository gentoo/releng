subarch: s390x
version_stamp: openrc-@TIMESTAMP@
target: stage1
rel_type: 23.0-default
profile: default/linux/s390/23.0/s390x
snapshot_treeish: @TREEISH@
source_subpath: 23.0-default/stage3-s390x-openrc-latest
update_seed: yes
update_seed_command: --update --deep --newuse @world
compression_mode: pixz
portage_prefix: releng
portage_confdir: @REPO_DIR@/releases/portage/stages
