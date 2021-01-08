subarch: armv5tel
version_stamp: @TIMESTAMP@
target: stage1
rel_type: default
profile: default/linux/arm/17.0/armv5te
snapshot: @TIMESTAMP@
source_subpath: default/stage3-armv5tel-latest
compression_mode: pixz_x
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
interpreter: /usr/bin/qemu-arm
