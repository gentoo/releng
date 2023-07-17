subarch: arm64
target: stage1
version_stamp: musl-llvm-@TIMESTAMP@
rel_type: musl-llvm
profile: default/linux/arm64/17.0/musl/llvm
snapshot_treeish: @TREEISH@
source_subpath: musl-llvm/stage3-arm64-musl-llvm-latest.tar.xz
compression_mode: pixz
update_seed: yes
update_seed_command: --update --deep --jobs=5 --newuse --complete-graph @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
chost: aarch64-gentoo-linux-musl
