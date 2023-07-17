subarch: arm64
target: stage1
version_stamp: musl-hardened-@TIMESTAMP@
rel_type: 23.0-musl-hardened
profile: default/linux/arm64/23.0/musl/hardened
snapshot_treeish: @TREEISH@
source_subpath: 23.0-musl-hardened/stage3-arm64-musl-hardened-latest.tar.xz
compression_mode: pixz
update_seed: yes
update_seed_command: --update --deep --newuse @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
