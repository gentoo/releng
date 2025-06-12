subarch: m68k
version_stamp: t64-systemd-@TIMESTAMP@
target: stage1
rel_type: 23.0-time64
profile: default/linux/m68k/23.0/time64/systemd
snapshot_treeish: @TREEISH@
source_subpath: 23.0-time64/stage3-m68k-t64-systemd-latest
compression_mode: pixz
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
interpreter: /usr/bin/qemu-m68k
