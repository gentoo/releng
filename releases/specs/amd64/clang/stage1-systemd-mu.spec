subarch: amd64
target: stage1
version_stamp: llvm-systemd-mergedusr-@TIMESTAMP@
rel_type: llvm-mergedusr
profile: default/linux/amd64/17.1/systemd/clang/merged-usr
snapshot: @TIMESTAMP@
source_subpath: llvm-mergedusr/stage3-amd64-llvm-systemd-mergedusr-latest
compression_mode: pixz
update_seed: yes
update_seed_command: --update --deep --newuse @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
