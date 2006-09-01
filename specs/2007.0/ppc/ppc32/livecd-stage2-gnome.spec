subarch: ppc
version_stamp: 2007.0
target: livecd-stage2
rel_type: default
profile: default-linux/ppc/ppc32/2007.0
snapshot: 2007.0
portage_overlay: /root/livecd/overlays/portage
source_subpath: default/livecd-stage1-ppc-installer-2007.0

livecd/fstype: squashfs
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/yaboot-1.3.13-cdtar.tar.bz2
livecd/iso: /var/tmp/catalyst/builds/default/livecd-ppc-installer-2007.0.iso
#livecd/splash_type: gensplash
#livecd/splash_theme: livecd-2007.0
livecd/xdm: gdm
livecd/xsession: gnome
livecd/fsscript: /root/livecd/scripts/2007.0/livecd.sh

livecd/type: gentoo-release-livecd
livecd/users: gentoo
livecd/volid: Gentoo Linux 2007.0 PPC LiveCD

livecd/overlay: /root/livecd/overlays/livecd/2007.0
livecd/root_overlay: /root/livecd/overlays/root-livecd

#livecd/bootargs: dokeymap
livecd/gk_mainargs: --makeopts=-j4 --lvm2 --dmraid --evms2
#--unionfs-dev

livecd/rcadd: pbbuttonsd|default

boot/kernel: ppc32 pegasos
boot/kernel/ppc32/config: /root/livecd/kconfig/releases/2007.0/ppc/ppc32/livecd-2.6.17-ppc32.config
boot/kernel/ppc32/sources: gentoo-sources
boot/kernel/ppc32/extraversion: ppc32
boot/kernel/ppc32/use: pcmcia usb oss atm truetype -qt -qt3 -qt4
boot/kernel/ppc32/packages:
#	media-gfx/splashutils
#	media-gfx/splash-themes-livecd
	sys-apps/pcmciautils
#	net-dialup/speedtouch
#	net-dialup/slmodem
#	net-dialup/globespan-adsl
#	net-wireless/hostap-utils
#	net-dialup/fritzcapi
#	net-dialup/fcdsl
	sys-fs/cryptsetup-luks
#	net-wireless/at76c503a
#	net-wireless/rt2500
#	net-wireless/rtl8180
#	net-wireless/adm8211
#	net-wireless/acx
	media-libs/alsa-lib
	media-libs/alsa-oss
	media-sound/alsa-utils
	app-laptop/pbbuttonsd

boot/kernel/pegasos/config: /root/livecd/kconfig/releases/2007.0/ppc/ppc32/installcd-2.6.17-pegasos.config
boot/kernel/pegasos/sources: sys-kernel/gentoo-sources
boot/kernel/pegasos/use: usb -X png truetype
boot/kernel/pegasos/extraversion: pegasos
boot/kernel/pegasos/gk_kernargs: --no-initrdmodules --genzimage
#boot/kernel/pegasos/packages:
#	net-dialup/slmodem
#	net-dialup/globespan-adsl
#	net-dialup/fritzcapi
#	net-dialup/fcdsl

livecd/unmerge:
	gentoo-sources

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
