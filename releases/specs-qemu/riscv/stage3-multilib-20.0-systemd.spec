subarch: rv64_multilib
target: stage3
version_stamp: 20.0-systemd-@TIMESTAMP@
cflags: -O2 -pipe
interpreter: /usr/bin/qemu-riscv64 /usr/bin/qemu-riscv32
rel_type: 20.0
profile: default/linux/riscv/20.0/rv64gc/multilib/systemd
snapshot: @TIMESTAMP@
source_subpath: 20.0/stage1-rv64_multilib-20.0-systemd-@TIMESTAMP@
compression_mode: pixz
decompressor_search_order: xz bzip2
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
