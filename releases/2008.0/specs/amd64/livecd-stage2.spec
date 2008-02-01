subarch: amd64
version_stamp: 2008.0
target: livecd-stage2
rel_type: default
profile: default-linux/amd64/2008.0/dev/desktop
snapshot: 2008.0
source_subpath: default/livecd-stage1-amd64-installer-2008.0

livecd/fstype: squashfs
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/isolinux-elilo-memtest86+-cdtar.tar.bz2
livecd/iso: /var/tmp/catalyst/builds/default/livecd-amd64-installer-2008.0.iso
livecd/xsession: xfce
livecd/fsscript: /var/cvsroot/gentoo/src/releng/scripts/2008.0/livecd.sh

livecd/type: gentoo-release-livecd
livecd/users: gentoo
livecd/volid: Gentoo Linux 2008.0 amd64 LiveCD

livecd/overlay: /var/cvsroot/gentoo/src/releng/overlays/2008.0/common/overlay/livecd
livecd/root_overlay: /var/cvsroot/gentoo/src/releng/overlays/2008.0/common/root_overlay

livecd/bootargs: dokeymap
livecd/gk_mainargs: --lvm --dmraid --evms --mdadm

boot/kernel: gentoo
boot/kernel/gentoo/sources: gentoo-sources

boot/kernel/gentoo/config: /root/livecd/2008.0/kconfig/amd64/livecd-2.6.24.config

boot/kernel/gentoo/use: pcmcia usb oss atm

boot/kernel/gentoo/packages:
	media-libs/alsa-lib
	media-libs/alsa-oss
	media-sound/alsa-utils
	net-dialup/fcdsl
	net-dialup/fritzcapi
	net-dialup/globespan-adsl
	net-dialup/slmodem
	net-misc/br2684ctl
	net-wireless/acx
	net-wireless/hostap-utils
	net-wireless/madwifi-ng-tools
	net-wireless/rt2500
	net-wireless/rtl8187
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
