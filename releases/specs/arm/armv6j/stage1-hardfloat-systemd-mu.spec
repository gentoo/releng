subarch: armv6j_hardfp
version_stamp: systemd-mergedusr-@TIMESTAMP@
target: stage1
rel_type: mergedusr
profile: default/linux/arm/17.0/armv6j/systemd/merged-usr
snapshot: @TIMESTAMP@
source_subpath: mergedusr/stage3-armv6j_hardfp-systemd-mergedusr-latest.tar.xz
compression_mode: pixz
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
