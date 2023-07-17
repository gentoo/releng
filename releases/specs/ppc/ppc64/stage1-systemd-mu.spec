subarch: ppc64
target: stage1
version_stamp: systemd-mergedusr-@TIMESTAMP@
rel_type: mergedusr
profile: default/linux/ppc64/17.0/systemd/merged-usr
snapshot_treeish: @TREEISH@
source_subpath: mergedusr/stage3-ppc64-systemd-mergedusr-latest
compression_mode: pixz
update_seed: yes
update_seed_command: --update --deep --newuse @world --jobs 8 --load-average 12
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
