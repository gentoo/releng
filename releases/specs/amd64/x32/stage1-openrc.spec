subarch: x32
target: stage1
version_stamp: openrc-@TIMESTAMP@
rel_type: default
profile: default/linux/amd64/17.0/x32
snapshot_treeish: @TIMESTAMP@
source_subpath: default/stage3-x32-openrc-latest
compression_mode: pixz
update_seed: yes
update_seed_command: --update --deep --newuse @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
