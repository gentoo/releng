subarch: arm64
target: stage1
version_stamp: llvm-systemd-mergedusr-@TIMESTAMP@
rel_type: llvm-mergedusr
profile: default/linux/arm64/17.0/systemd/llvm/merged-usr
snapshot_treeish: @TIMESTAMP@
source_subpath: llvm-mergedusr/stage3-arm64-llvm-systemd-mergedusr-latest.tar.xz
compression_mode: pixz
update_seed: yes
update_seed_command: --update --deep --jobs=5 --newuse --complete-graph @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
