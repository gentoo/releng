subarch: i686
version_stamp: @TIMESTAMP@
target: livecd-stage2
rel_type: default
profile: default/linux/x86/17.0/desktop
snapshot: @TIMESTAMP@
source_subpath: default/livecd-stage1-i686-installer-@TIMESTAMP@

livecd/bootargs: dokeymap
livecd/cdtar: /usr/share/catalyst/livecd/cdtar/isolinux-elilo-memtest86+-cdtar.tar.bz2
livecd/fsscript: @REPO_DIR@/releases/@TIMESTAMP@/scripts/livecd.sh
livecd/fstype: squashfs
livecd/iso: livecd-i686-installer-@TIMESTAMP@.iso
livecd/type: gentoo-release-livecd
livecd/volid: Gentoo x86 LiveCD @TIMESTAMP@
livecd/xdm: gdm
livecd/xsession: xfce

livecd/overlay: @REPO_DIR@/releases/@TIMESTAMP@/overlays/common/overlay/livecd
livecd/root_overlay: @REPO_DIR@/releases/@TIMESTAMP@/overlays/common/root_overlay

boot/kernel: gentoo

boot/kernel/gentoo/sources: gentoo-sources
boot/kernel/gentoo/config: @REPO_DIR@/releases/@TIMESTAMP@/kconfig/livecd-2.6.24.config
boot/kernel/gentoo/use: atm png truetype usb
boot/kernel/gentoo/packages:
	media-libs/alsa-oss
	media-sound/alsa-utils
#	net-dialup/fcdsl
#	net-dialup/fritzcapi
### Compile failure w/ 2.6.24
#	net-dialup/slmodem
	net-misc/br2684ctl
### Compile failure
#	net-wireless/acx
	net-wireless/hostap-utils
### In-kernel
#	net-wireless/ipw3945
#	net-wireless/madwifi-ng-tools
### Compile failure and in-kernel
#	net-wireless/rt2500
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
	/usr/share/genkernel/pkg/x86/cpio

livecd/rm:
	/etc/*-
	/etc/*.old
	/root/.viminfo
	/var/log/*.log
	/usr/share/genkernel/pkg/x86/*.bz2
