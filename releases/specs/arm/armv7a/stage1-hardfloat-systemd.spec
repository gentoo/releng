subarch: armv7a_hardfp
version_stamp: systemd-@TIMESTAMP@
target: stage1
rel_type: default
profile: default/linux/arm/17.0/armv7a/systemd
snapshot: @TIMESTAMP@
source_subpath: default/stage3-armv7a_hardfp-systemd-latest.tar.xz
compression_mode: pixz
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
