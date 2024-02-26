subarch: amd64
target: stage1
version_stamp: hardened-systemd-@TIMESTAMP@
rel_type: 23.0-hardened
profile: default/linux/amd64/23.0/hardened/systemd
snapshot_treeish: @TREEISH@
source_subpath: 23.0-hardened/stage3-amd64-hardened-systemd-latest
compression_mode: pixz
update_seed: yes
update_seed_command: --update --deep --newuse @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
