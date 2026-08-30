subarch: i686
target: stage1
version_stamp: musl-openrc-@TIMESTAMP@
rel_type: 23.0-musl
profile: default/linux/x86/23.0/i686/musl
snapshot_treeish: @TREEISH@
source_subpath: 23.0-musl/stage3-i686-musl-openrc-latest
chost: i686-pc-linux-musl
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
update_seed: yes
update_seed_command: --update --deep --newuse @world
compression_mode: pixz
