subarch: mipsel3_n32
target: stage1
version_stamp: systemd-mergedusr-@TIMESTAMP@
interpreter: /usr/bin/qemu-mipsn32el
rel_type: mergedusr
profile: default/linux/mips/17.0/mipsel/n32/systemd/merged-usr
snapshot: @TIMESTAMP@
source_subpath: mergedusr/stage3-mipsel3_n32-systemd-mergedusr-latest
compression_mode: pixz
decompressor_search_order: xz bzip2
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
