subarch: ppc
target: stage2
version_stamp: uclibc-@TIMESTAMP@
rel_type: embedded
profile: uclibc/ppc
snapshot: @TIMESTAMP@
source_subpath: embedded/stage1-ppc-uclibc-@TIMESTAMP@
cflags: -Os -pipe
ldflags: -Wl,-O1
chost: powerpc-gentoo-linux-uclibc
