subarch: armv7a_hardfp_musl
version_stamp: openrc-@TIMESTAMP@
target: stage1
rel_type: musl
profile: default/linux/arm/17.0/musl/armv7a
snapshot_treeish: @TIMESTAMP@
source_subpath: musl/stage3-armv7a_hardfp_musl-openrc-latest.tar.xz
compression_mode: pixz
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
