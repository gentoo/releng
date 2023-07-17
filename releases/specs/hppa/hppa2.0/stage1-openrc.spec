subarch: hppa2.0
target: stage1
version_stamp: openrc-@TIMESTAMP@
rel_type: default
profile: default/linux/hppa/17.0
snapshot_treeish: @TREEISH@
source_subpath: default/stage3-hppa2.0-openrc-latest
update_seed: yes
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
compression_mode: pixz
decompressor_search_order: xz bzip2
update_seed_command: --update --deep --newuse @world
