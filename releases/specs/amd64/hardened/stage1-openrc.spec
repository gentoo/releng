subarch: amd64
target: stage1
version_stamp: hardened-openrc-@TIMESTAMP@
rel_type: hardened
profile: default/linux/amd64/17.1/hardened
snapshot_treeish: @TREEISH@
source_subpath: hardened/stage3-amd64-hardened-openrc-latest
compression_mode: pixz
update_seed: yes
update_seed_command: --update --deep --newuse @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
