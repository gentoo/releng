subarch: amd64
target: stage1
version_stamp: hardened-selinux-latest
rel_type: hardened
profile: default/linux/amd64/17.0/hardened/selinux
snapshot: latest
source_subpath: hardened/stage3-amd64-hardened-selinux-latest
compression_mode: pixz_x
decompressor_search_order: tar pixz xz lbzip2 bzip2 gzip
update_seed: yes
update_seed_command: --update --deep @world
portage_confdir: @REPO_DIR@/releases/weekly/portage/stages
portage_prefix: releng
