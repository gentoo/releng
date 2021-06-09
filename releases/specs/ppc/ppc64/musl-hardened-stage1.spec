subarch: ppc64
target: stage1
version_stamp: musl-hardened-@TIMESTAMP@
rel_type: musl-hardened
profile: default/linux/ppc64/17.0/musl/hardened
snapshot: @TIMESTAMP@
source_subpath: musl-hardened/stage3-ppc64-musl-hardened-latest
chost: powerpc64-gentoo-linux-musl
compression_mode: pixz_x
update_seed: yes
update_seed_command: --update --deep --newuse @world --jobs 5 --load-average 5
portage_confdir: @REPO_DIR@/releases/portage/stages-musl
portage_prefix: releng
repos: /var/db/repos/musl
