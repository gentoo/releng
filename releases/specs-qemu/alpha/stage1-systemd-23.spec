subarch: alpha
target: stage1
version_stamp: systemd-23.0-@TIMESTAMP@
rel_type: 23.0-default
profile: default/linux/alpha/23.0/systemd
snapshot_treeish: @TIMESTAMP@
source_subpath: 23.0-default/stage3-alpha-systemd-23.0-latest
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
interpreter: /usr/bin/qemu-alpha
compression_mode: pixz
