subarch: s390
version_stamp: @TIMESTAMP@
target: stage1
rel_type: default
profile: default/linux/s390/17.0
snapshot: @TIMESTAMP@
source_subpath: default/stage3-s390-latest
update_seed: yes
update_seed_command: --update --deep --newuse @world --jobs 2 --load-average 2
compression_mode: pixz_x
portage_confdir: @REPO_DIR@/releases/portage/stages
pkgcache_path: /var/tmp/catalyst/packages/default/stage1-s390
