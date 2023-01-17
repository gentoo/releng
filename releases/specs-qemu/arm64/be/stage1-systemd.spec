subarch: aarch64_be
version_stamp: systemd-@TIMESTAMP@
target: stage1
rel_type: default
profile: default/linux/arm64/17.0/big-endian/systemd
snapshot: @TIMESTAMP@
source_subpath: default/stage3-aarch64_be-systemd-latest
compression_mode: pixz
update_seed: no
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
interpreter: /usr/bin/qemu-aarch64_be
