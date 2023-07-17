subarch: amd64
target: stage1
version_stamp: musl-llvm-@TIMESTAMP@
rel_type: musl-clang
profile: default/linux/amd64/17.0/musl/clang
snapshot_treeish: @TREEISH@
source_subpath: musl-clang/stage3-amd64-musl-llvm-latest
chost: x86_64-gentoo-linux-musl
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
update_seed: yes
update_seed_command: --update --deep --newuse @world
compression_mode: pixz
