subarch: power9le
target: stage1
version_stamp: power9-@TIMESTAMP@
rel_type: power9
profile: default/linux/ppc64le/17.0
snapshot: @TIMESTAMP@
source_subpath: power9/stage3-ppc64le-power9-latest
compression_mode: pixz_x
update_seed: yes
update_seed_command: --update --deep --newuse @world --jobs 64 --load-average 128
portage_confdir: @REPO_DIR@/releases/portage/stages
