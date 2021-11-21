subarch: armv7a_hardfp_musl
version_stamp: hardened-openrc-@TIMESTAMP@
target: stage1
rel_type: musl-hardened
profile: default/linux/arm/17.0/musl/armv7a/hardened
snapshot: @TIMESTAMP@
source_subpath: musl/stage3-armv7a_hardfp_musl-hardened-openrc-latest
compression_mode: pixz
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
repos: /root/musl
