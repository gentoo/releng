subarch: ppc64le
target: stage1
version_stamp: openrc-@TIMESTAMP@
rel_type: default
profile: default/linux/ppc64le/17.0
snapshot_treeish: @TREEISH@
source_subpath: default/stage3-ppc64le-openrc-latest
compression_mode: pixz
update_seed: yes
update_seed_command: --update --deep --newuse @world --jobs 8 --load-average 12
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
