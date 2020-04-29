subarch: ppc
target: stage2
version_stamp: uclibc-softfloat-@TIMESTAMP@
rel_type: embedded
profile: uclibc/ppc
snapshot: @TIMESTAMP@
source_subpath: embedded/stage1-ppc-uclibc-softfloat-@TIMESTAMP@
cflags: -Os -pipe
ldflags: -Wl,-O1
chost: powerpc-softfloat-linux-uclibc
