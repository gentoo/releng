subarch: amd64
target: stage1
version_stamp: hardened-nomultilib-selinux-openrc-@TIMESTAMP@
rel_type: hardened
profile: default/linux/amd64/17.1/no-multilib/hardened/selinux
snapshot: @TIMESTAMP@
source_subpath: hardened/stage3-amd64-hardened-nomultilib-selinux-openrc-latest
compression_mode: pixz_x
update_seed: yes
update_seed_command: --update --deep --newuse @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
