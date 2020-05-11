subarch: ia64
version_stamp: @TIMESTAMP@
target: stage1
rel_type: default
profile: default/linux/ia64/17.0
snapshot: @TIMESTAMP@
source_subpath: default/stage3-ia64-latest
compression_mode: pixz_x
decompressor_search_order: tar pixz xz lbzip2 bzip2 gzip
update_seed: yes
update_seed_command: --update --deep --newuse @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
