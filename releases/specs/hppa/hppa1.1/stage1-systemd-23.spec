subarch: hppa1.1
target: stage1
version_stamp: systemd-@TIMESTAMP@
rel_type: 23.0-default
profile: default/linux/hppa/23.0/hppa1.1/systemd
snapshot_treeish: @TREEISH@
source_subpath: 23.0-default/stage3-hppa1.1-systemd-latest
update_seed: yes
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
compression_mode: pixz
decompressor_search_order: xz bzip2
update_seed_command: --update --deep --newuse @world
