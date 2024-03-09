subarch: arm64
chost: aarch64-unknown-linux-musl
target: stage1
version_stamp: musl-llvm-@TIMESTAMP@
rel_type: 23.0-musl-llvm
profile: default/linux/arm64/23.0/musl/llvm
snapshot_treeish: @TREEISH@
source_subpath: 23.0-musl-llvm/stage3-arm64-musl-llvm-latest.tar.xz
compression_mode: pixz
update_seed: yes
update_seed_command: --update --deep --newuse @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
