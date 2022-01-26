subarch: armv5tel
version_stamp: systemd-@TIMESTAMP@
target: stage1
rel_type: default
profile: default/linux/arm/17.0/armv5te/systemd
snapshot: @TIMESTAMP@
source_subpath: default/stage3-armv5tel-systemd-latest.tar.xz
compression_mode: pixz
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
