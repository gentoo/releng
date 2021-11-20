subarch: armv6j_hardfp_musl
version_stamp: openrc-@TIMESTAMP@
target: stage1
rel_type: musl
profile: default/linux/arm/17.0/musl/armv6j
snapshot: @TIMESTAMP@
source_subpath: musl/stage3-armv6j_hardfp_musl-openrc-latest
compression_mode: pixz
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-musl
portage_prefix: releng
repos: /root/musl
