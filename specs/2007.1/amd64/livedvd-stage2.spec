subarch: amd64
version_stamp: 2007.1
target: livecd-stage2
rel_type: default
profile: default-linux/amd64/2007.1/desktop
snapshot: 2007.1
source_subpath: default/livecd-stage1-amd64-installer-2007.1

livecd/fstype: squashfs
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/isolinux-3.09-memtest86+-cdtar.tar.bz2
livecd/iso: /var/tmp/catalyst/builds/default/livedvd-amd64-installer-2007.1.iso
livecd/xdm: gdm
livecd/xsession: xfce
livecd/fsscript: /var/cvsroot/gentoo/src/releng/scripts/2007.1/livecd.sh

livecd/type: gentoo-release-livecd
livecd/users: gentoo
livecd/volid: Gentoo Linux AMD64 LiveDVD

livecd/overlay: /var/cvsroot/gentoo/src/releng/overlays/2007.1/common/overlay/livedvd
livecd/root_overlay: /var/cvsroot/gentoo/src/releng/overlays/root-livecd

livecd/bootargs: dokeymap
livecd/gk_mainargs: --lvm --dmraid --evms --mdadm

boot/kernel: gentoo
boot/kernel/gentoo/sources: gentoo-sources

boot/kernel/gentoo/config: /var/cvsroot/gentoo/src/releng/kconfig/2007.1/amd64/livecd-2.6.22.config

boot/kernel/gentoo/use: pcmcia usb oss atm truetype png

boot/kernel/gentoo/packages:
	media-libs/alsa-lib
	media-libs/alsa-oss
	media-sound/alsa-utils
#	net-dialup/fcdsl
#	net-dialup/fritzcapi
	net-dialup/globespan-adsl
#	net-dialup/slmodem
	net-misc/br2684ctl
#	net-wireless/acx
	net-wireless/hostap-utils
	net-wireless/ipw3945
	net-wireless/madwifi-ng-tools
	net-wireless/rt2500
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
	/usr/share/genkernel/pkg/amd64/cpio

livecd/rm:
	/etc/*-
	/etc/*.old
	/root/.viminfo
	/var/log/*.log
	/usr/share/genkernel/pkg/amd64/*.bz2
