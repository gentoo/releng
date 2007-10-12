subarch: i686
version_stamp: 2007.1
target: livecd-stage2
rel_type: default
profile: default-linux/x86/2007.1/desktop
snapshot: 2007.1
source_subpath: default/livecd-stage1-i686-installer-2007.1

livecd/fstype: squashfs
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/isolinux-elilo-memtest86+-cdtar.tar.bz2
livecd/iso: /var/tmp/catalyst/builds/default/livecd-i686-installer-2007.1.iso
livecd/splash_type: gensplash
livecd/splash_theme: livecd-2007.1
livecd/xdm: gdm
livecd/xsession: gnome
livecd/fsscript: /root/livecd/scripts/2007.1/livecd.sh

livecd/type: gentoo-release-livecd
livecd/users: gentoo
livecd/volid: Gentoo Linux 2007.1 x86 LiveCD

livecd/overlay: /root/livecd/overlays/2007.1/common/overlay/livecd
livecd/root_overlay: /root/livecd/overlays/2007.1/common/root_overlay

livecd/bootargs: dokeymap
livecd/gk_mainargs: --lvm --dmraid --emvs --unionfs-dev

boot/kernel: gentoo
boot/kernel/gentoo/sources: gentoo-sources

boot/kernel/gentoo/config: /root/livecd/kconfig/2007.1/x86/livecd-2.6.19.config

boot/kernel/gentoo/use: pcmcia usb oss atm

boot/kernel/gentoo/packages:
	media-gfx/splashutils
	media-gfx/splash-themes-livecd
	media-libs/alsa-lib
	media-sound/alsa-utils
#	net-dialup/fcdsl
#	net-dialup/fritzcapi
	net-dialup/globespan-adsl
	net-dialup/slmodem
	net-wireless/acx
	net-wireless/hostap-utils
	net-wireless/ipw3945
	net-wireless/madwifi-ng-tools
	net-wireless/rt2500
#	net-wireless/rtl8187
	sys-apps/pcmciautils
	sys-fs/cryptsetup-luks

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
