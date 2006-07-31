subarch: i686
version_stamp: 2006.1
target: livecd-stage2
rel_type: default
profile: default-linux/x86/2006.1/desktop
snapshot: 2006.1
source_subpath: default/livecd-stage1-i686-installer-2006.1

livecd/fstype: squashfs
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/isolinux-3.09-memtest86+-cdtar.tar.bz2
livecd/iso: /var/tmp/catalyst2/builds/default/livecd-i686-installer-2006.1.iso
livecd/splash_type: gensplash
livecd/splash_theme: livecd-2006.1
livecd/xdm: gdm
livecd/xsession: gnome

livecd/type: gentoo-release-livecd
livecd/users: gentoo
livecd/volid: Gentoo Linux 2006.1 x86 LiveCD

livecd/overlay: /root/livecd/overlays/livecd/2006.1
livecd/root_overlay: /root/livecd/overlays/root-livecd

livecd/bootargs: dokeymap
livecd/gk_mainargs: --lvm2 --dmraid --evms2 --unionfs-dev

boot/kernel: gentoo
boot/kernel/gentoo/sources: gentoo-sources

boot/kernel/gentoo/config: /root/livecd/kconfig/releases/2006.1/x86/livecd-2.6.17.config

boot/kernel/gentoo/use: pcmcia usb oss atm

boot/kernel/gentoo/packages:
	media-gfx/splashutils
	media-gfx/splash-themes-livecd
	sys-apps/pcmciautils
	net-dialup/slmodem
	net-dialup/globespan-adsl
	net-wireless/hostap-utils
	net-dialup/fritzcapi
	net-dialup/fcdsl
	sys-apps/acpid
	sys-fs/cryptsetup-luks
#	net-wireless/at76c503a
#	net-wireless/rt2500
#	net-wireless/rtl8180
#	net-wireless/adm8211
	net-wireless/rt2500
	net-wireless/acx
	net-wireless/ipw3945
# These three are removed for licensing reasons.
#	media-video/nvidia-kernel
#	media-video/nvidia-glx
#	x11-drivers/ati-drivers
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
