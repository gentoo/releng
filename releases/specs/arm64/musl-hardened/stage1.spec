subarch: arm64
target: stage1
version_stamp: musl-hardened-@TIMESTAMP@
rel_type: musl-hardened
profile: default/linux/arm64/17.0/musl/hardened
snapshot_treeish: @TIMESTAMP@
source_subpath: musl-hardened/stage3-arm64-musl-hardened-latest.tar.xz
compression_mode: pixz
update_seed: yes
update_seed_command: --update --deep --jobs=5 --newuse --complete-graph @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
chost: aarch64-gentoo-linux-musl
