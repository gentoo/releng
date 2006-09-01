subarch: amd64
version_stamp: 2007.0
target: livecd-stage2
rel_type: default
profile: default-linux/amd64/2007.0/desktop
snapshot: 2007.0
source_subpath: default/livecd-stage1-amd64-installer-2007.0

livecd/fstype: squashfs
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/isolinux-3.09-memtest86+-cdtar.tar.bz2
livecd/iso: /var/tmp/catalyst/builds/default/livecd-amd64-installer-2007.0.iso
livecd/splash_type: gensplash
livecd/splash_theme: livecd-2007.0
livecd/xdm: gdm
livecd/xsession: gnome
livecd/fsscript: /root/livecd/scripts/2007.0/livecd.sh

livecd/type: gentoo-release-livecd
livecd/users: gentoo
livecd/volid: Gentoo Linux 2007.0 amd64 LiveCD

livecd/overlay: /root/livecd/overlays/livecd/2007.0
livecd/root_overlay: /root/livecd/overlays/root-livecd

livecd/bootargs: dokeymap
livecd/gk_mainargs: --makeopts=-j16 --lvm2 --dmraid --evms2
#--unionfs-dev

boot/kernel: gentoo
boot/kernel/gentoo/sources: gentoo-sources

boot/kernel/gentoo/config: /root/livecd/kconfig/releases/2007.0/amd64/livecd-2.6.17.config

boot/kernel/gentoo/use: pcmcia usb oss atm

boot/kernel/gentoo/packages:
	media-gfx/splashutils
	media-gfx/splash-themes-livecd
	sys-apps/pcmciautils
	sys-power/acpid
	sys-fs/cryptsetup-luks
	net-wireless/rt2500
#	net-wireless/ipw3945
	media-libs/alsa-lib
	media-libs/alsa-oss
	media-sound/alsa-utils

livecd/unmerge:
	sys-kernel/gentoo-sources

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
	/usr/share/genkernel/pkg/x86/cpio

livecd/rm:
	/etc/*-
	/etc/*.old
	/root/.viminfo
	/var/log/*.log
	/usr/share/genkernel/pkg/x86/*.bz2
