subarch: mipsel3_multilib
target: stage1
version_stamp: openrc-@TIMESTAMP@
interpreter: /usr/bin/qemu-mipsn32el /usr/bin/qemu-mipsel /usr/bin/qemu-mips64el
rel_type: default
profile: default/linux/mips/17.0/mipsel/multilib/n32
snapshot_treeish: @TIMESTAMP@
source_subpath: default/stage3-mipsel3_multilib-openrc-latest
compression_mode: pixz
decompressor_search_order: xz bzip2
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
