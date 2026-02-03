subarch: amd64
target: stage1
version_stamp: musl-llvm-openrc-@TIMESTAMP@
rel_type: 23.0-musl-llvm
profile: default/linux/amd64/23.0/musl/llvm
snapshot_treeish: @TREEISH@
source_subpath: 23.0-musl-llvm/stage3-amd64-musl-llvm-openrc-latest
chost: x86_64-pc-linux-musl
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
update_seed: yes
update_seed_command: --update --deep --newuse @world
compression_mode: pixz
