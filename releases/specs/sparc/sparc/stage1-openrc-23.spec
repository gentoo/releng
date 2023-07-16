subarch: sparc
target: stage1
version_stamp: openrc-@TIMESTAMP@
rel_type: 23.0-default
profile: default/linux/sparc/23.0
snapshot_treeish: @TIMESTAMP@
source_subpath: 23.0-default/stage3-sparc-openrc-latest
compression_mode: pixz
update_seed: yes
update_seed_command: --update --deep --newuse @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
