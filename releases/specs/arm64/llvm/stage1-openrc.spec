subarch: arm64
target: stage1
version_stamp: llvm-openrc-@TIMESTAMP@
rel_type: llvm
profile: default/linux/arm64/17.0/llvm
snapshot: @TIMESTAMP@
source_subpath: llvm/stage3-arm64-llvm-openrc-latest.tar.xz
compression_mode: pixz
update_seed: yes
update_seed_command: --update --deep --jobs=5 --newuse --complete-graph @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
