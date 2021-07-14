subarch: power9le
target: stage1
version_stamp: openrc-@TIMESTAMP@
rel_type: power9le
profile: power9le/linux/ppc64le/17.0
snapshot: @TIMESTAMP@
source_subpath: power9le/stage3-power9le-openrc-latest
compression_mode: pixz_x
update_seed: yes
update_seed_command: --update --deep --newuse @world --jobs 8 --load-average 12
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
