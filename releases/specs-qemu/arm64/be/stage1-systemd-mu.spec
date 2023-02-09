subarch: aarch64_be
version_stamp: systemd-mergedusr-@TIMESTAMP@
target: stage1
rel_type: mergedusr
profile: default/linux/arm64/17.0/big-endian/systemd/merged-usr
snapshot: @TIMESTAMP@
source_subpath: mergedusr/stage3-aarch64_be-systemd-mergedusr-latest
compression_mode: pixz
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
interpreter: /usr/bin/qemu-aarch64_be
