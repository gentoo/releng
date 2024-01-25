subarch: i686
target: stage1
version_stamp: musl-@TIMESTAMP@
rel_type: 23.0-musl
profile: default/linux/x86/23.0/i686/musl
snapshot: @TIMESTAMP@
source_subpath: 23.0-musl/stage3-i686-musl-latest
chost: i686-pc-linux-musl
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
update_seed: yes
update_seed_command: --update --deep --newuse @world
compression_mode: pixz
