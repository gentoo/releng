subarch: i686
target: stage1
version_stamp: hardened-openrc-@TIMESTAMP@
rel_type: 23.0-hardened
profile: default/linux/x86/23.0/i686/hardened
snapshot_treeish: @TIMESTAMP@
source_subpath: 23.0-hardened/stage3-i686-hardened-openrc-latest
compression_mode: pixz
update_seed: yes
update_seed_command: --update --deep --newuse @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
