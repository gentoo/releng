subarch: arm64
version_stamp: 2008.0
target: stage1
rel_type: default
profile: default/linux/arm64/17.0
snapshot: current
source_subpath: default/stage3-arm64-latest
pkgcache_path: /var/tmp/catalyst/packages/stage1
portage_confdir: @REPO_DIR@/releases/weekly/specs/arm64/portage-confdir
update_seed: yes
update_seed_command: --update --deep --jobs=5 --newuse --complete-graph @world
