subarch: armv6j_hardfp
version_stamp: systemd-mergedusr-@TIMESTAMP@
target: stage1
rel_type: default
profile: default/linux/arm/17.0/armv6j/systemd/merged-usr
snapshot: @TIMESTAMP@
source_subpath: default/stage3-armv6j_hardfp-systemd-mergedusr-latest.tar.xz
compression_mode: pixz
update_seed: no
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
