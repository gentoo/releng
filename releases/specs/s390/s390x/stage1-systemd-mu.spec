subarch: s390x
version_stamp: systemd-mergedusr-@TIMESTAMP@
target: stage1
rel_type: mergedusr
profile: default/linux/s390/17.0/s390x/systemd/merged-usr
snapshot: @TIMESTAMP@
source_subpath: mergedusr/stage3-s390x-systemd-mergedusr-latest
update_seed: no
update_seed_command: --update --deep --newuse @world
compression_mode: pixz
portage_confdir: @REPO_DIR@/releases/portage/stages
pkgcache_path: /var/tmp/catalyst/packages/default/stage1-s390x
