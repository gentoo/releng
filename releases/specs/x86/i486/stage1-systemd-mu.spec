subarch: i486
target: stage1
version_stamp: systemd-mergedusr-@TIMESTAMP@
rel_type: mergedusr
profile: default/linux/x86/17.0/systemd/merged-usr
snapshot: @TIMESTAMP@
source_subpath: mergedusr/stage3-i486-systemd-mergedusr-latest
compression_mode: pixz
update_seed: no
update_seed_command: --update --deep --newuse @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
