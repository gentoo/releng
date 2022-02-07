subarch: amd64
version_stamp: plasma-@TIMESTAMP@
target: livecd-stage2
rel_type: default
profile: default/linux/amd64/17.1/desktop/plasma
snapshot: @TIMESTAMP@
source_subpath: default/livecd-stage1-amd64-plasma-@TIMESTAMP@
portage_confdir: @REPO_DIR@/releases/portage/isos

livecd/bootargs: dokeymap
livecd/fstype: squashfs
livecd/iso: livedvd-amd64-@TIMESTAMP@.iso
livecd/type: gentoo-release-livecd
livecd/volid: Gentoo amd64 @TIMESTAMP@

boot/kernel: gentoo

boot/kernel/gentoo/sources: gentoo-sources
boot/kernel/gentoo/config: @REPO_DIR@/releases/kconfig/amd64/amd64-5.10.61.config
