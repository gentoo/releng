subarch: sparc64
target: stage1
version_stamp: systemd-mergedusr-@TIMESTAMP@
rel_type: mergedusr
profile: default/linux/sparc/17.0/64ul/systemd/merged-usr
snapshot: @TIMESTAMP@
source_subpath: mergedusr/stage3-sparc64-systemd-mergedusr-latest
compression_mode: pixz
update_seed: yes
update_seed_command: --update --deep --newuse @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
