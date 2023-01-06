subarch: mips3_multilib
target: stage1
version_stamp: systemd-mergedusr-@TIMESTAMP@
interpreter: /usr/bin/qemu-mipsn32 /usr/bin/qemu-mips /usr/bin/qemu-mips64
rel_type: mergedusr
profile: default/linux/mips/17.0/multilib/n32/systemd/merged-usr
snapshot: @TIMESTAMP@
source_subpath: mergedusr/stage3-mips3_multilib-systemd-mergedusr-latest
compression_mode: pixz
decompressor_search_order: xz bzip2
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
