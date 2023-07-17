subarch: ppc64
target: stage1
version_stamp: musl-hardened-openrc-@TIMESTAMP@
rel_type: musl-hardened
profile: default/linux/ppc64/17.0/musl/hardened
snapshot_treeish: @TREEISH@
source_subpath: musl-hardened/stage3-ppc64-musl-hardened-openrc-latest
chost: powerpc64-gentoo-linux-musl
compression_mode: pixz
update_seed: yes
update_seed_command: --update --deep --newuse @world --jobs 8 --load-average 12
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
repos: /var/db/repos/musl
