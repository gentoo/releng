subarch: i686
target: stage1
version_stamp: hardened-openrc-@TIMESTAMP@
rel_type: hardened
profile: default/linux/x86/17.0/hardened
snapshot_treeish: @TIMESTAMP@
source_subpath: hardened/stage3-i686-hardened-openrc-latest
compression_mode: pixz
update_seed: yes
update_seed_command: --update --deep --newuse @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
