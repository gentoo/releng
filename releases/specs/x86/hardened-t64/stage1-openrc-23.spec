subarch: i686
target: stage1
version_stamp: hardened-t64-openrc-@TIMESTAMP@
rel_type: 23.0-hardened-time64
profile: default/linux/x86/23.0/i686/time64/hardened
snapshot_treeish: @TREEISH@
source_subpath: 23.0-hardened-time64/stage3-i686-hardened-t64-openrc-latest
compression_mode: pixz
update_seed: yes
update_seed_command: --update --deep --newuse @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
