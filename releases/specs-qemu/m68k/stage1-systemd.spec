subarch: m68k
version_stamp: systemd-@TIMESTAMP@
target: stage1
rel_type: default
profile: default/linux/m68k/17.0/systemd
snapshot_treeish: @TREEISH@
source_subpath: default/stage3-m68k-systemd-latest
compression_mode: pixz
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
interpreter: /usr/bin/qemu-m68k
