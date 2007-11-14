subarch: amd64
version_stamp: 2007.1
target: livecd-stage2
rel_type: default
profile: default-linux/amd64/2007.1/desktop
snapshot: 2007.1
source_subpath: default/livecd-stage1-amd64-installer-2007.1

livecd/fstype: squashfs
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/isolinux-elilo-memtest86+-cdtar.tar.bz2
livecd/iso: /var/tmp/catalyst/builds/default/livecd-amd64-installer-2007.1.iso
#livecd/splash_type: gensplash
#livecd/splash_theme: livecd-2007.1
livecd/xsession: xfce
#livecd/fsscript: /root/livecd/scripts/2007.1/livecd.sh

livecd/type: gentoo-release-livecd
livecd/users: gentoo
livecd/volid: Gentoo Linux 2007.1 amd64 LiveCD

livecd/overlay: /root/livecd/overlays/2007.1/common/overlay/livecd
livecd/root_overlay: /root/livecd/overlays/2007.1/common/root_overlay

livecd/bootargs: dokeymap
livecd/gk_mainargs: --makeopts=-j16 --lvm --dmraid --evms --mdadm

boot/kernel: gentoo
boot/kernel/gentoo/sources: gentoo-sources

boot/kernel/gentoo/config: /root/livecd/kconfig/2007.1/amd64/livecd-2.6.22.config

boot/kernel/gentoo/use: pcmcia usb oss atm

boot/kernel/gentoo/packages:
	media-gfx/splashutils
	media-gfx/splash-themes-livecd
	media-libs/alsa-lib
	media-libs/alsa-oss
	media-sound/alsa-utils
### Masked
#	net-dialup/fcdsl
### Masked
#	net-dialup/fritzcapi
### Masked
#	net-dialup/globespan-adsl
### Masked
#	net-dialup/slmodem
	net-misc/br2684ctl
### Masked
#	net-wireless/acx
	net-wireless/hostap-utils
	net-wireless/ipw3945
	net-wireless/madwifi-ng-tools
	net-wireless/rt2500
### Masked
#	net-wireless/rtl8187
	sys-apps/pcmciautils

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
