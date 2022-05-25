subarch: s390x
version_stamp: openrc-@TIMESTAMP@
target: stage1
rel_type: default
profile: default/linux/s390/17.0/s390x
snapshot: @TIMESTAMP@
source_subpath: default/stage3-s390x-openrc-latest
update_seed: yes
update_seed_command: --update --deep --newuse @world
compression_mode: pixz
portage_confdir: @REPO_DIR@/releases/portage/stages
pkgcache_path: /var/tmp/catalyst/packages/default/stage1-s390x
