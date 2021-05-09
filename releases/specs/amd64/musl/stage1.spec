subarch: amd64
target: stage1
version_stamp: musl-@TIMESTAMP@
rel_type: musl
profile: default/linux/amd64/17.0/musl
snapshot: @TIMESTAMP@
source_subpath: musl/stage3-amd64-musl-latest
chost: x86_64-gentoo-linux-musl
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_overlay: /release/trees/musl-auto
portage_prefix: releng
update_seed: yes
update_seed_command: --update --deep --newuse @world
compression_mode: pixz_x
