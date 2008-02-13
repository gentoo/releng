subarch: alpha
version_stamp: 2008.0
target: livecd-stage2
rel_type: default
profile: default/linux/alpha/2008.0/desktop
snapshot: 2008.0
source_subpath: default/livecd-stage1-alpha-installer-2008.0

livecd/fstype: squashfs
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/aboot-0.9-r1-cdtar.tar.bz2

livecd/iso: /var/tmp/catalyst/builds/default/livecd-alpha-installer-2008.0.iso

livecd/xdm: gdm
livecd/xsession: xfce
livecd/fsscript: /var/cvsroot/gentoo/src/releng/scripts/2008.0/livecd.sh

livecd/volid: Gentoo Linux alpha LiveCD 2008.0
livecd/users: gentoo
livecd/type: gentoo-release-livecd

livecd/overlay: /root/livecd/overlays/livecd/2008.0/common/overlay/livecd
livecd/root_overlay: /root/livecd/overlays/2008.0/common/root_overlay

livecd/bootargs: dokeymap
livecd/gk_mainargs: --lvm --dmraid --evms --mdadm

boot/kernel: gentoo
boot/kernel/gentoo/sources: gentoo-sources
boot/kernel/gentoo/config: /var/svnroot/releng/trunk/releases/2008.0/kconfig/alpha/livecd-2.6.19.config
boot/kernel/gentoo/use: atm fbcondecor mng png truetype usb
boot/kernel/gentoo/packages:
	media-libs/alsa-lib
	media-libs/alsa-oss
	media-sound/alsa-utils
	net-misc/br2684ctl

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
	/etc/splash/gentoo
	/etc/splash/emergence
	/usr/share/genkernel/pkg/amd64/cpio

livecd/rm:
	/etc/*-
	/etc/*.old
	/root/.viminfo
	/var/log/*.log
	/usr/share/genkernel/pkg/amd64/*.bz2
