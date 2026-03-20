subarch: armv7a_hardfp_musl
chost: armv7a-unknown-linux-musleabihf
version_stamp: hardened-openrc-@TIMESTAMP@
target: stage1
rel_type: 23.0-musl-hardened
profile: default/linux/arm/23.0/armv7a_hf/musl/hardened
snapshot_treeish: @TREEISH@
source_subpath: 23.0-musl-hardened/stage3-armv7a_hardfp_musl-hardened-openrc-latest.tar.xz
compression_mode: pixz
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
