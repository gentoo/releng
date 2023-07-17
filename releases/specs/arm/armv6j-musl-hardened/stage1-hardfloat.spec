subarch: armv6j_hardfp_musl
version_stamp: hardened-openrc-@TIMESTAMP@
target: stage1
rel_type: musl-hardened
profile: default/linux/arm/17.0/musl/armv6j/hardened
snapshot_treeish: @TREEISH@
source_subpath: musl-hardened/stage3-armv6j_hardfp_musl-hardened-openrc-latest.tar.xz
compression_mode: pixz
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
