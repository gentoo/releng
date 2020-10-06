subarch: ppc64le
target: stage1
version_stamp: musl-hardened-@TIMESTAMP@
rel_type: default
profile: default/linux/ppc64le/17.0/musl/hardened
snapshot: @TIMESTAMP@
source_subpath: default/stage3-ppc64le-musl-hardened-latest
chost: powerpc64le-gentoo-linux-musl
compression_mode: pixz_x
update_seed: yes
update_seed_command: --update --deep --newuse @world --jobs 5 --load-average 5
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
portage_overlay: /var/db/repos/musl
