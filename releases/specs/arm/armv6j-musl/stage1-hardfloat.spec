subarch: armv6j_hardfp_musl
version_stamp: openrc-@TIMESTAMP@
target: stage1
rel_type: musl
profile: default/linux/arm/17.0/musl/armv6j
snapshot_treeish: @TREEISH@
source_subpath: musl/stage3-armv6j_hardfp_musl-openrc-latest.tar.xz
compression_mode: pixz
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
