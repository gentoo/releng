subarch: ppc
target: stage1
version_stamp: uclibc-softfloat-@TIMESTAMP@
rel_type: embedded
profile: uclibc/ppc
snapshot: @TIMESTAMP@
source_subpath: embedded/stage3-ppc-uclibc-softfloat-latest
cflags: -Os -pipe
ldflags: -Wl,-O1
chost: powerpc-softfloat-linux-uclibc
update_seed: yes
