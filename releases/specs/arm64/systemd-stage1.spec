subarch: arm64
target: stage1
version_stamp: systemd-@TIMESTAMP@
rel_type: default
profile: default/linux/arm64/17.0/systemd
snapshot: @TIMESTAMP@
source_subpath: default/stage3-arm64-systemd-latest
compression_mode: pixz
update_seed: yes
update_seed_command: --update --deep --jobs=5 --newuse --complete-graph @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
