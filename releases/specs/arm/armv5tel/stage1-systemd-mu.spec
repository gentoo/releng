subarch: armv5tel
version_stamp: systemd-mergedusr-@TIMESTAMP@
target: stage1
rel_type: mergedusr
profile: default/linux/arm/17.0/armv5te/systemd/merged-usr
snapshot: @TIMESTAMP@
source_subpath: mergedusr/stage3-armv5tel-systemd-mergedusr-latest.tar.xz
compression_mode: pixz
update_seed: no
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
