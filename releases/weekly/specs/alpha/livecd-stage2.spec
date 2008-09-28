subarch: alpha
version_stamp: 2008.0
target: livecd-stage2
rel_type: default
profile: default/linux/alpha/2008.0/desktop
snapshot: 2008.0
source_subpath: default/livecd-stage1-alpha-installer-2008.0

livecd/bootargs: dokeymap
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/aboot-1.0_pre20040408-r2-cdtar.tar.bz2
livecd/fsscript: /var/cvsroot/gentoo/src/releng/scripts/2008.0/livecd.sh
livecd/fstype: squashfs
livecd/gk_mainargs: --lvm --dmraid --evms --mdadm
livecd/iso: /var/tmp/catalyst/builds/default/livecd-alpha-installer-2008.0.iso
livecd/type: gentoo-release-livecd
livecd/volid: Gentoo Linux alpha LiveCD 2008.0
livecd/xdm: gdm
livecd/xsession: xfce

livecd/overlay: /root/livecd/overlays/livecd/2008.0/common/overlay/livecd
livecd/root_overlay: /root/livecd/overlays/2008.0/common/root_overlay

boot/kernel: gentoo
boot/kernel/gentoo/sources: gentoo-sources
boot/kernel/gentoo/config: /var/svnroot/releng/trunk/releases/2008.0/kconfig/alpha/livecd-2.6.19.config
boot/kernel/gentoo/use: atm fbcondecor mng png truetype usb
boot/kernel/gentoo/packages:
	media-libs/alsa-oss
	media-sound/alsa-utils
	net-misc/br2684ctl
	sys-fs/ntfs3g

livecd/empty:
	/var/tmp
	/var/empty
	/var/run
	/var/state
	/var/cache/edb/dep
	/tmp
	/usr/portage
	/usr/src
	/root/.ccache
	/usr/share/genkernel/pkg/amd64/cpio

livecd/rm:
	/etc/*-
	/etc/*.old
	/root/.viminfo
	/var/log/*.log
	/usr/share/genkernel/pkg/amd64/*.bz2
