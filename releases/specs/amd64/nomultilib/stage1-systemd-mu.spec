subarch: amd64
target: stage1
version_stamp: nomultilib-systemd-mergedusr-@TIMESTAMP@
rel_type: mergedusr
profile: default/linux/amd64/17.1/no-multilib/systemd/merged-usr
snapshot: @TIMESTAMP@
source_subpath: mergedusr/stage3-amd64-nomultilib-systemd-mergedusr-latest
compression_mode: pixz
update_seed: yes
update_seed_command: --update --deep --newuse @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
