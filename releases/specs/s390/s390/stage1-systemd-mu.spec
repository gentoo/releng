subarch: s390
version_stamp: systemd-mergedusr-@TIMESTAMP@
target: stage1
rel_type: mergedusr
profile: default/linux/s390/17.0/systemd/merged-usr
snapshot: @TIMESTAMP@
source_subpath: mergedusr/stage3-s390-systemd-mergedusr-latest
update_seed: yes
update_seed_command: --update --deep --newuse @world
compression_mode: pixz
portage_confdir: @REPO_DIR@/releases/portage/stages
