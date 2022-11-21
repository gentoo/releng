subarch: alpha
target: stage1
version_stamp: systemd-mergedusr-@TIMESTAMP@
rel_type: default
profile: default/linux/alpha/17.0/systemd/merged-usr
snapshot: @TIMESTAMP@
source_subpath: default/stage3-alpha-systemd-mergedusr-latest
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
interpreter: /usr/bin/qemu-alpha
compression_mode: pixz
