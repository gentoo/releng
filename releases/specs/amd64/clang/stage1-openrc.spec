subarch: amd64
target: stage1
version_stamp: llvm-openrc-@TIMESTAMP@
rel_type: clang
profile: default/linux/amd64/17.1/clang
snapshot_treeish: @TREEISH@
source_subpath: clang/stage3-amd64-llvm-openrc-latest
compression_mode: pixz
update_seed: yes
update_seed_command: --update --deep --newuse @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
