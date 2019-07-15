subarch: amd64
target: stage1
version_stamp: hardened+nomultilib-latest
rel_type: hardened
profile: default/linux/amd64/17.1/no-multilib/hardened
snapshot: latest
source_subpath: hardened/stage3-amd64-hardened+nomultilib-latest
compression_mode: pixz_x
decompressor_search_order: tar pixz xz lbzip2 bzip2 gzip
update_seed: yes
update_seed_command: --update --deep @world
portage_confdir: @REPO_DIR@/releases/weekly/portage/stages
portage_prefix: releng
