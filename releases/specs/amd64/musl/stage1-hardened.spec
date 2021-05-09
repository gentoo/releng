subarch: amd64
target: stage1
version_stamp: musl-hardened-@TIMESTAMP@
rel_type: musl-hardened
profile: default/linux/amd64/17.0/musl/hardened
snapshot: @TIMESTAMP@
source_subpath: musl-hardened/stage3-amd64-musl-hardened-latest
chost: x86_64-gentoo-linux-musl
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_overlay: /release/trees/musl-auto
portage_prefix: releng
update_seed: yes
update_seed_command: --update --deep --newuse @world
compression_mode: pixz_x
