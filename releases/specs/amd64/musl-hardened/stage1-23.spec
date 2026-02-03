subarch: amd64
target: stage1
version_stamp: musl-hardened-openrc-@TIMESTAMP@
rel_type: 23.0-musl-hardened
profile: default/linux/amd64/23.0/musl/hardened
snapshot_treeish: @TREEISH@
source_subpath: 23.0-musl-hardened/stage3-amd64-musl-hardened-openrc-latest
chost: x86_64-pc-linux-musl
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
update_seed: yes
update_seed_command: --update --deep --newuse @world
compression_mode: pixz
