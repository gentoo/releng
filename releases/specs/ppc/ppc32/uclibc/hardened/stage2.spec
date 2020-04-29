subarch: ppc
target: stage2
version_stamp: uclibc-hardened-@TIMESTAMP@
rel_type: embedded
profile: uclibc/ppc/hardened
snapshot: @TIMESTAMP@
source_subpath: embedded/stage1-ppc-uclibc-hardened-@TIMESTAMP@
cflags: -Os -pipe
ldflags: -Wl,-O1
chost: powerpc-gentoo-linux-uclibc
