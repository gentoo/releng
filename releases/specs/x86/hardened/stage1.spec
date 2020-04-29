subarch: i686
target: stage1
version_stamp: hardened-@TIMESTAMP@
rel_type: hardened
profile: default/linux/x86/17.0/hardened
snapshot: @TIMESTAMP@
source_subpath: hardened/stage3-i686-hardened-latest
compression_mode: pixz_x
decompressor_search_order: tar pixz xz lbzip2 bzip2 gzip
update_seed: yes
update_seed_command: --update --deep @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
