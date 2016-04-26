subarch: i686
version_stamp: latest
target: livecd-stage2
rel_type: default
profile: default/linux/x86/13.0/desktop
snapshot: latest
source_subpath: default/livecd-stage1-i686-installer-latest

livecd/bootargs: dokeymap
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/isolinux-elilo-memtest86+-cdtar.tar.bz2
livecd/fsscript: @REPO_DIR@/releases/latest/scripts/livecd.sh
livecd/fstype: squashfs
livecd/gk_mainargs: --lvm --dmraid --mdadm --makeopts=-j8
livecd/iso: livedvd-i686-installer-latest.iso
livecd/type: gentoo-release-livecd
livecd/volid: Gentoo Linux latest x86 LiveDVD
livecd/xdm: gdm
livecd/xsession: xfce

livecd/overlay: @REPO_DIR@/releases/latest/overlays/common/overlay/livedvd
livecd/root_overlay: @REPO_DIR@/releases/latest/overlays/common/root_overlay

boot/kernel: gentoo

boot/kernel/gentoo/sources: gentoo-sources
boot/kernel/gentoo/config: @REPO_DIR@/releases/latest/kconfig/livecd-2.6.24.config
boot/kernel/gentoo/use: atm fbcondecor mng png truetype usb
boot/kernel/gentoo/packages:
	app-laptop/laptop-mode-tools
	media-libs/alsa-lib
	media-sound/alsa-utils
#	net-dialup/fcdsl
#	net-dialup/fritzcapi
	net-dialup/globespan-adsl
### Compile failure w/ 2.6.24
#	net-dialup/slmodem
	net-misc/br2684ctl
### Compile failure
#	net-wireless/acx
	net-wireless/hostap-utils
	net-wireless/kismet
### In-kernel
#	net-wireless/ipw3945
#	net-wireless/madwifi-ng-tools
### Compile failure and in-kernel
#	net-wireless/rt2500
#	net-wireless/rtl8187

	sys-apps/pcmciautils

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
	/usr/share/genkernel/pkg/x86/cpio

livecd/rm:
	/etc/*-
	/etc/*.old
	/root/.viminfo
	/var/log/*.log
	/usr/share/genkernel/pkg/x86/*.bz2
