subarch: ia64
version_stamp: 2007.0
target: livecd-stage2
rel_type: default
profile: default-linux/ia64/2007.0/desktop
snapshot: 2007.0
source_subpath: default/livecd-stage1-ia64-installer-2007.0

livecd/fstype: squashfs
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/elilo-3.6-cdtar.tar.bz2
livecd/iso: /var/tmp/catalyst/builds/default/livecd-ia64-installer-2007.0.iso
#livecd/splash_type: gensplash
#livecd/splash_theme: livecd-2007.0
livecd/xdm: gdm
livecd/xsession: gnome
livecd/fsscript: /root/livecd/scripts/2007.0/livecd.sh

livecd/type: gentoo-release-livecd
livecd/users: gentoo
livecd/volid: Gentoo Linux 2007.0 IA64 LiveCD

livecd/overlay: /root/livecd/overlays/2007.0/common/overlay/livecd
livecd/root_overlay: /root/livecd/overlays/2007.0/common/root_overlay

livecd/bootargs: dokeymap
livecd/gk_mainargs: --makeopts=-j16 --dmraid --evms2 --unionfs-dev

boot/kernel: gentoo
boot/kernel/gentoo/sources: gentoo-sources

boot/kernel/gentoo/config: /root/livecd/kconfig/releases/2007.0/ia64/livecd-2.6.19.config

boot/kernel/gentoo/use: pcmcia usb oss atm

boot/kernel/gentoo/packages:
#	media-gfx/splashutils
#	media-gfx/splash-themes-livecd
	media-libs/alsa-lib
	media-libs/alsa-oss
	media-sound/alsa-utils
#	net-dialup/fcdsl
#	net-dialup/fritzcapi
#	net-dialup/globespan-adsl
#	net-dialup/slmodem
#	net-wireless/acx
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
