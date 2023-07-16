subarch: power9le
target: stage1
version_stamp: systemd-@TIMESTAMP@
rel_type: power9le
profile: default/linux/ppc64le/17.0/systemd
snapshot_treeish: @TIMESTAMP@
source_subpath: power9le/stage3-power9le-systemd-latest
compression_mode: pixz
update_seed: yes
update_seed_command: --update --deep --newuse @world --jobs 8 --load-average 12
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
