subarch: x32
target: stage1
version_stamp: systemd-mergedusr-@TIMESTAMP@
rel_type: mergedusr
profile: default/linux/amd64/17.0/x32/systemd/merged-usr
snapshot: @TIMESTAMP@
source_subpath: default/stage3-x32-systemd-mergedusr-latest
compression_mode: pixz
update_seed: no
update_seed_command: --update --deep --newuse @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
