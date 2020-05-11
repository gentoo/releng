subarch: x32
target: stage1
version_stamp: @TIMESTAMP@
rel_type: default
profile: default/linux/amd64/17.0/x32
snapshot: @TIMESTAMP@
source_subpath: default/stage3-x32-latest
compression_mode: pixz_x
decompressor_search_order: tar pixz xz lbzip2 bzip2 gzip
update_seed: yes
update_seed_command: --update --deep --newuse @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
