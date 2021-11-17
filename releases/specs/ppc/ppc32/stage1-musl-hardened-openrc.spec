subarch: ppc
target: stage1
version_stamp: musl-hardened-openrc-@TIMESTAMP@
rel_type: musl-hardened
profile: default/linux/ppc/17.0/musl/hardened
snapshot: @TIMESTAMP@
chost: powerpc-gentoo-linux-musl
source_subpath: musl-hardened/stage3-ppc-musl-hardened-openrc-latest
compression_mode: pixz
update_seed: yes
update_seed_command: --update --deep --newuse @world --jobs 8 --load-average 12
portage_confdir: @REPO_DIR@/releases/portage/stages-musl
portage_prefix: releng
repos: /var/db/repos/musl
