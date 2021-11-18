subarch: amd64
target: stage1
version_stamp: nomultilib-systemd-@TIMESTAMP@
rel_type: default
profile: default/linux/amd64/17.1/no-multilib/systemd
snapshot: @TIMESTAMP@
source_subpath: default/stage3-amd64-nomultilib-systemd-latest
compression_mode: pixz
update_seed: yes
update_seed_command: --update --deep --newuse @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
