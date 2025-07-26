subarch: mipsel3_multilib
target: stage1
version_stamp: t64-openrc-@TIMESTAMP@
interpreter: /usr/bin/qemu-mipsn32el /usr/bin/qemu-mipsel /usr/bin/qemu-mips64el
rel_type: 23.0-time64
profile: default/linux/mips/23.0/time64/mipsel/multilib/n32
snapshot_treeish: @TREEISH@
source_subpath: 23.0-time64/stage3-mipsel3_multilib-t64-openrc-latest
compression_mode: pixz
decompressor_search_order: xz bzip2
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
