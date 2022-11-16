subarch: ia64
version_stamp: systemd-mergedusr-@TIMESTAMP@
target: stage1
rel_type: default
profile: default/linux/ia64/17.0/systemd/merged-usr
snapshot: @TIMESTAMP@
source_subpath: default/stage3-ia64-systemd-mergedusr-latest
compression_mode: pixz
update_seed: no
update_seed_command: --update --deep --newuse @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
