subarch: arm64
target: stage1
version_stamp: systemd-mergedusr-@TIMESTAMP@
rel_type: mergedusr
profile: default/linux/arm64/17.0/systemd/merged-usr
snapshot: @TIMESTAMP@
source_subpath: mergedusr/stage3-arm64-systemd-mergedusr-latest.tar.xz
compression_mode: pixz
update_seed: no
update_seed_command: --update --deep --jobs=5 --newuse --complete-graph @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
