subarch: sparc
target: stage1
version_stamp: latest
rel_type: default
profile: default/linux/sparc/17.0/systemd
snapshot: latest
source_subpath: default/stage3-sparc-latest
compression_mode: xz_x
decompressor_search_order: tar pixz xz lbzip2 bzip2 gzip
update_seed: yes
update_seed_command: --update --deep @world
portage_confdir: @REPO_DIR@/releases/weekly/portage/stages
portage_prefix: releng
