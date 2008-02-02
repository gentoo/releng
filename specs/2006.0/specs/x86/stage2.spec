subarch: x86
target: stage2
version_stamp: 2006.0
rel_type: default
profile: default-linux/x86/no-nptl/2.4
snapshot: 20060123
source_subpath: default/stage1-x86-2006.0
# Here we set it back for gcc 3.4
cflags: -O2 -mtune=i686 -pipe
cxxflags: -O2 -mtune=i686 -pipe
