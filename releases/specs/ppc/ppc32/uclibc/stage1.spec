subarch: ppc
target: stage1
version_stamp: uclibc-@TIMESTAMP@
rel_type: embedded
profile: uclibc/ppc
snapshot: @TIMESTAMP@
source_subpath: embedded/stage3-ppc-uclibc-latest
cflags: -Os -pipe
ldflags: -Wl,-O1
chost: powerpc-gentoo-linux-uclibc
update_seed: yes
