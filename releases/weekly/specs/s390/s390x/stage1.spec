subarch: s390x
version_stamp: 2008.0
target: stage1
rel_type: default
profile: default/linux/s390/17.0/s390x
snapshot: 2008.0
source_subpath: default/stage3-s390x-latest
update_seed: yes
update_seed_command: --update --deep @world --jobs 2 --load-average 2
compression_mode: pixz_x
decompressor_search_order: tar pixz xz lbzip2 bzip2 gzip
portage_confdir: @REPO_DIR@/releases/weekly/portage/stages
