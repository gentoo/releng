subarch: i686
target: stage2
version_stamp: hardened-@TIMESTAMP@
rel_type: hardened
profile: hardened/linux/x86
snapshot: @TIMESTAMP@
source_subpath: hardened/stage1-x86-hardened-@TIMESTAMP@
chost: i686-pc-linux-gnu
cflags: -mtune=i686 -O2 -pipe -fforce-addr
portage_prefix: releng
