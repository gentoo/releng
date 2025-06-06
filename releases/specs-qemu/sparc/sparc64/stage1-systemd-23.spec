subarch: sparc64
target: stage1
version_stamp: systemd-@TIMESTAMP@
rel_type: 23.0-default
profile: default/linux/sparc/23.0/64ul/systemd
snapshot_treeish: @TREEISH@
source_subpath: 23.0-default/stage3-sparc64-systemd-latest
interpreter: /usr/bin/qemu-sparc64
compression_mode: pixz
update_seed: yes
update_seed_command: --update --deep --newuse @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
