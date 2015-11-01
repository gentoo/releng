subarch: x86
target: stage2
version_stamp: uclibc-hardened-latest
rel_type: embedded
profile: uclibc/x86/hardened
snapshot: latest
source_subpath: embedded/stage1-x86-uclibc-hardened-latest
cflags: -Os -mtune=i386 -pipe -fforce-addr
ldflags: -Wl,-O1
chost: i386-gentoo-linux-uclibc
