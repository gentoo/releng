subarch: amd64
target: stage1
version_stamp: hardened-selinux+nomultilib-latest
rel_type: hardened
profile: hardened/linux/amd64/no-multilib/selinux
snapshot: latest
source_subpath: hardened/stage3-amd64-hardened-selinux+nomultilib-latest
compression_mode: pixz_x
decompressor_search_order: tar pixz xz lbzip2 bzip2 gzip
update_seed: yes
#update_seed_command: --update --deep @world
portage_confdir: @REPO_DIR@/releases/weekly/portage/stages
