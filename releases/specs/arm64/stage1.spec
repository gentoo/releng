subarch: arm64
target: stage1
version_stamp: @TIMESTAMP@
rel_type: default
profile: default/linux/arm64/17.0
snapshot: @TIMESTAMP@
source_subpath: default/stage3-arm64-latest
compression_mode: pixz_x
update_seed: yes
update_seed_command: --update --deep --jobs=5 --newuse --complete-graph @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
