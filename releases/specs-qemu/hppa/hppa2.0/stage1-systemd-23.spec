subarch: hppa2.0
target: stage1
version_stamp: systemd-@TIMESTAMP@
rel_type: 23.0-default
profile: default/linux/hppa/23.0/hppa2.0/systemd
snapshot_treeish: @TREEISH@
source_subpath: 23.0-default/stage3-hppa2.0-systemd-latest
update_seed: yes
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
compression_mode: pixz
decompressor_search_order: xz bzip2
update_seed_command: --update --deep --newuse @world
interpreter: /usr/bin/qemu-hppa
