subarch: ppc
target: stage1
version_stamp: uclibc-hardened-@TIMESTAMP@
rel_type: embedded
profile: uclibc/ppc/hardened
snapshot: @TIMESTAMP@
source_subpath: embedded/stage3-ppc-uclibc-hardened-latest
cflags: -Os -pipe
ldflags: -Wl,-O1
chost: powerpc-gentoo-linux-uclibc
update_seed: yes
