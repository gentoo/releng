subarch: hppa1.1
target: stage1
version_stamp: systemd-@TIMESTAMP@
rel_type: default
profile: default/linux/hppa/17.0/systemd
snapshot_treeish: @TIMESTAMP@
source_subpath: default/stage3-hppa1.1-systemd-latest
update_seed: yes
interpreter: /usr/bin/qemu-hppa
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
compression_mode: pixz
decompressor_search_order: xz bzip2
update_seed_command: --update --deep --newuse @world
