subarch: armv7a_hardfp_musl
chost: armv7a-unknown-linux-musleabihf
version_stamp: openrc-@TIMESTAMP@
target: stage1
rel_type: 23.0-musl
profile: default/linux/arm/23.0/armv7a_hf/musl
snapshot_treeish: @TREEISH@
source_subpath: 23.0-musl/stage3-armv7a_hardfp_musl-openrc-latest.tar.xz
compression_mode: pixz
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
