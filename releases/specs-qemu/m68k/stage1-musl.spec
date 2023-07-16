subarch: m68k_musl
version_stamp: @TIMESTAMP@
target: stage1
rel_type: musl
profile: default/linux/m68k/17.0/musl
snapshot_treeish: @TIMESTAMP@
source_subpath: musl/stage3-m68k_musl-latest
compression_mode: pixz
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
interpreter: /usr/bin/qemu-m68k
