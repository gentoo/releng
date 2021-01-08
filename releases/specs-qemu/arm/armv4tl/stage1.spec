subarch: armv4tl
version_stamp: @TIMESTAMP@
target: stage1
rel_type: default
profile: default/linux/arm/17.0/armv4t
snapshot: @TIMESTAMP@
source_subpath: default/stage3-armv4tl-latest
compression_mode: pixz_x
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
interpreter: /usr/bin/qemu-arm
