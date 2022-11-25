subarch: mipsel3_multilib
target: stage3
version_stamp: systemd-@TIMESTAMP@
interpreter: /usr/bin/qemu-mipsn32el /usr/bin/qemu-mipsel /usr/bin/qemu-mips64el
rel_type: default
profile: default/linux/mips/17.0/mipsel/multilib/n32/systemd
snapshot: @TIMESTAMP@
source_subpath: default/stage1-mipsel3_multilib-systemd-@TIMESTAMP@
compression_mode: pixz
decompressor_search_order: xz bzip2
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
