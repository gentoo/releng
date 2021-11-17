subarch: armv7a_hardfp
version_stamp: musl-@TIMESTAMP@
target: stage3
rel_type: musl
profile: default/linux/arm/17.0/musl/armv7a
snapshot: @TIMESTAMP@
source_subpath: musl/stage1-armv7a_hardfp-musl-@TIMESTAMP@
compression_mode: pixz_x
portage_confdir: @REPO_DIR@/releases/portage/stages-musl
portage_prefix: releng
repos: /root/musl
cflags: -O2 -pipe -march=armv7-a -mfpu=vfpv3-d16 -mfloat-abi=hard
