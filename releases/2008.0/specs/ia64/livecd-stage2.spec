subarch: ia64
version_stamp: 2008.0
target: livecd-stage2
rel_type: default
profile: default/linux/ia64/2008.0/desktop
snapshot: 2008.0
source_subpath: default/livecd-stage1-ia64-installer-2008.0

livecd/bootargs: dokeymap
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/elilo-3.6-cdtar.tar.bz2
livecd/fsscript: /var/cvsroot/gentoo/src/releng/scripts/2008.0/livecd.sh
livecd/fstype: squashfs
livecd/gk_mainargs: --dmraid --evms --lvm --mdadm
livecd/iso: /var/tmp/catalyst/builds/default/livecd-ia64-installer-2008.0.iso
livecd/type: gentoo-release-livecd
livecd/volid: Gentoo Linux 2008.0 IA64 LiveCD
livecd/xdm: gdm
livecd/xsession: xfce

livecd/overlay: /var/cvsroot/gentoo/src/releng/overlays/2008.0/common/overlay/livecd
livecd/root_overlay: /var/cvsroot/gentoo/src/releng/overlays/2008.0/common/root_overlay

boot/kernel: gentoo
boot/kernel/gentoo/sources: gentoo-sources
boot/kernel/gentoo/config: /var/cvsroot/gentoo/src/releng/kconfig/2008.0/ia64/livecd-2.6.18.config
boot/kernel/gentoo/use: atm fbcondecor mng png truetype usb
boot/kernel/gentoo/packages:
	media-libs/alsa-oss
	media-sound/alsa-utils
#	net-dialup/fcdsl
#	net-dialup/fritzcapi
#	net-dialup/globespan-adsl
#	net-dialup/slmodem
#	net-misc/br2684ctl
#	net-wireless/acx
#	net-wireless/hostap-utils
#	net-wireless/ipw3945
#	net-wireless/madwifi-ng-tools
#	net-wireless/rt2500
#	net-wireless/rtl8187
#	sys-apps/pcmciautils
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
	/usr/share/genkernel/pkg/x86/cpio

livecd/rm:
	/etc/*-
	/etc/*.old
	/root/.viminfo
	/var/log/*.log
	/usr/share/genkernel/pkg/x86/*.bz2
