subarch: ppc
target: stage1
version_stamp: t64-systemd-@TIMESTAMP@
rel_type: 23.0-time64
profile: default/linux/ppc/23.0/time64/systemd
snapshot_treeish: @TREEISH@
source_subpath: 23.0-time64/stage3-ppc-t64-systemd-latest
compression_mode: pixz
update_seed: yes
update_seed_command: --update --deep --newuse @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
