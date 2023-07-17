subarch: mips2_softfloat
target: stage1
version_stamp: systemd-mergedusr-@TIMESTAMP@
interpreter: /usr/bin/qemu-mips
rel_type: mergedusr
profile: default/linux/mips/17.0/o32/systemd/merged-usr
snapshot_treeish: @TREEISH@
source_subpath: mergedusr/stage3-mips2_softfloat-systemd-mergedusr-latest
compression_mode: pixz
decompressor_search_order: xz bzip2
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
