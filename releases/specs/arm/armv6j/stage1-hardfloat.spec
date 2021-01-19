subarch: armv6j_hardfp
version_stamp: @TIMESTAMP@
target: stage1
rel_type: default
profile: default/linux/arm/17.0/armv6j
snapshot: @TIMESTAMP@
source_subpath: default/stage3-armv6j_hardfp-latest
compression_mode: pixz_x
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
