subarch: sparc64
target: stage1
version_stamp: @TIMESTAMP@
rel_type: default
profile: default/linux/sparc/17.0/64ul
snapshot: @TIMESTAMP@
source_subpath: default/stage3-sparc64-latest
compression_mode: pixz_x
update_seed: yes
update_seed_command: --update --deep --newuse @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
