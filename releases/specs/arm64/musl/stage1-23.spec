subarch: arm64
target: stage1
version_stamp: musl-@TIMESTAMP@
rel_type: 23.0-musl
profile: default/linux/arm64/23.0/musl
snapshot: @TIMESTAMP@
source_subpath: 23.0-musl/stage3-arm64-musl-latest.tar.xz
compression_mode: pixz
update_seed: yes
update_seed_command: --update --deep --newuse @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
