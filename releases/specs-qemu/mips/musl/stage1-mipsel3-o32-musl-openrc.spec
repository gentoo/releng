subarch: mipsel3
target: stage1
version_stamp: musl-openrc-@TIMESTAMP@
interpreter: /usr/bin/qemu-mipsel
rel_type: default
profile: default/linux/mips/17.0/musl/mipsel/o32
snapshot: @TIMESTAMP@
source_subpath: musl/stage3-mipsel3-musl-@TIMESTAmP@
compression_mode: pixz
decompressor_search_order: xz bzip2
update_seed: yes
update_seed_command: -uDN @world
chost: mipsel-unknown-linux-musl
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
