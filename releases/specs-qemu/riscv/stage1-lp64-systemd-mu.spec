subarch: rv64_lp64
target: stage1
version_stamp: systemd-mergedusr-@TIMESTAMP@
cflags: -O2 -pipe
interpreter: /usr/bin/qemu-riscv64
rel_type: mergedusr
profile: default/linux/riscv/20.0/rv64gc/lp64/systemd/merged-usr
snapshot_treeish: @TREEISH@
source_subpath: mergedusr/stage3-rv64_lp64-systemd-mergedusr-latest
compression_mode: pixz
decompressor_search_order: xz bzip2
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
