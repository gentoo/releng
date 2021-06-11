subarch: rv64_lp64d
target: stage3
version_stamp: 20.0-systemd-@TIMESTAMP@
cflags: -O2 -pipe
interpreter: /usr/bin/qemu-riscv64
rel_type: 20.0
profile: default/linux/riscv/20.0/rv64gc/lp64d/systemd
snapshot: @TIMESTAMP@
source_subpath: default/stage2-rv64_lp64d-20.0-systemd-@TIMESTAMP@
compression_mode: pixz
decompressor_search_order: xz bzip2
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
