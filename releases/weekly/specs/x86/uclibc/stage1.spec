subarch: x86
target: stage1
version_stamp: uclibc-latest
rel_type: embedded
profile: uclibc/x86
snapshot: latest
source_subpath: embedded/stage3-x86-uclibc-latest
cflags: -Os -mtune=i386 -pipe
ldflags: -Wl,-O1
chost: i386-gentoo-linux-uclibc
