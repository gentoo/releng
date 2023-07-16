subarch: aarch64_be
version_stamp: systemd-@TIMESTAMP@
target: stage1
rel_type: 23.0-default
profile: default/linux/arm64/23.0/big-endian/systemd
snapshot_treeish: @TIMESTAMP@
source_subpath: 23.0-default/stage3-aarch64_be-systemd-latest
compression_mode: pixz
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
interpreter: /usr/bin/qemu-aarch64_be
