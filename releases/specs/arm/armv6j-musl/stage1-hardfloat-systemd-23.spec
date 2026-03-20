subarch: armv6j_hardfp_musl
chost: armv6j-unknown-linux-musleabihf
version_stamp: systemd-@TIMESTAMP@
target: stage1
rel_type: 23.0-musl
profile: default/linux/arm/23.0/armv6j_hf/musl/systemd
snapshot_treeish: @TREEISH@
source_subpath: 23.0-musl/stage3-armv6j_hardfp_musl-systemd-latest.tar.xz
compression_mode: pixz
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
