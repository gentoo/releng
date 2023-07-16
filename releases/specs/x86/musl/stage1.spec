subarch: i686
target: stage1
version_stamp: musl-@TIMESTAMP@
rel_type: musl
profile: default/linux/x86/17.0/musl
snapshot_treeish: @TIMESTAMP@
source_subpath: musl/stage3-i686-musl-latest
chost: i686-gentoo-linux-musl
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
update_seed: yes
update_seed_command: --update --deep --newuse @world
compression_mode: pixz
