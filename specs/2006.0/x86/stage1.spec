subarch: x86
target: stage1
version_stamp: 2006.0
rel_type: default
profile: default-linux/x86/2006.0
snapshot: 20060123
source_subpath: default/stage3-x86-2005.1-r1
# These are here since our seed stage was gcc 3.3 and did not support -mtune
cflags: -O2 -mcpu=i686 -pipe
cxxflags: -O2 -mcpu=i686 -pipe
