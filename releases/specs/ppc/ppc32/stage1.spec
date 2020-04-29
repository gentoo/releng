subarch: ppc
target: stage1
version_stamp: latest
rel_type: default
profile: default/linux/powerpc/ppc32/17.0
snapshot: latest
source_subpath: default/stage3-ppc-latest
compression_mode: pixz_x
decompressor_search_order: tar pixz xz lbzip2 bzip2 gzip
update_seed: yes
update_seed_command: --update --deep @world --jobs 5 --load-average 5
portage_confdir: @REPO_DIR@/releases/portage/stages
