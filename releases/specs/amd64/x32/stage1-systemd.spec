subarch: x32
target: stage1
version_stamp: systemd-@TIMESTAMP@
rel_type: default
profile: default/linux/amd64/17.0/x32/systemd
snapshot: @TIMESTAMP@
source_subpath: default/stage3-x32-systemd-latest
compression_mode: pixz
update_seed: yes
update_seed_command: --update --deep --newuse @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
