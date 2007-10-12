subarch: ppc64
version_stamp: 32ul-2007.1
target: livecd-stage2
rel_type: default
profile: default-linux/ppc/ppc64/2007.1/32bit-userland/desktop
snapshot: 2007.1
source_subpath: default/livecd-stage1-ppc64-installer-32ul-2007.1

livecd/fstype: squashfs
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/yaboot-1.3.13-cdtar.tar.bz2
livecd/iso: /var/tmp/catalyst/builds/default/livecd-ppc64-installer-32ul-2007.1.iso
livecd/splash_type: gensplash
livecd/splash_theme: livecd-2007.1
livecd/xdm: gdm
livecd/xsession: gnome
livecd/fsscript: /root/livecd/scripts/2007.1/livecd.sh

livecd/type: gentoo-release-livecd
livecd/users: gentoo
livecd/volid: Gentoo Linux 2007.1 PPC LiveCD

livecd/overlay: /root/livecd/overlays/livecd/2007.1/common/overlay/livecd
livecd/root_overlay: /root/livecd/overlays/2007.1/common/root_overlay

#livecd/bootargs: dokeymap
livecd/gk_mainargs: --kernel-cross-compile=powerpc64-unknown-linux-gnu- --utils-arch=ppc --arch-override=ppc --makeopts=-j8 --lvm --dmraid --emvs --unionfs-dev

livecd/rcadd: pbbuttonsd|default

boot/kernel: ibm ppc32 ppc64 pegasos

boot/kernel/ibm/sources: sys-kernel/gentoo-sources
boot/kernel/ibm/use: extlib usb oss atm truetype -qt -qt3 -qt4
boot/kernel/ibm/config: /root/livecd/kconfig/releases/2007.1/ppc/ppc64/livecd-2.6.20-ibm.config
boot/kernel/ibm/console: ttyS0,9600 hvc0 hvsi0
boot/kernel/ibm/machine_type: ibm
boot/kernel/ibm/extraversion: ibm

boot/kernel/ppc32/config: /root/livecd/kconfig/releases/2007.1/ppc/ppc32/livecd-2.6.20-ppc32.config
boot/kernel/ppc32/sources: gentoo-sources
boot/kernel/ppc32/extraversion: ppc32
boot/kernel/ppc32/use: pcmcia usb oss atm truetype -qt -qt3 -qt4
boot/kernel/ppc32/packages:
	media-gfx/splashutils
	media-gfx/splash-themes-livecd
	sys-apps/pcmciautils
#	net-dialup/speedtouch
#	net-dialup/slmodem
#	net-dialup/globespan-adsl
#	net-wireless/hostap-utils
#	net-dialup/fritzcapi
#	net-dialup/fcdsl
	sys-fs/cryptsetup-luks
#	net-wireless/rt2500
#	net-wireless/rtl8180
#	net-wireless/adm8211
#	net-wireless/acx
	media-libs/alsa-lib
	media-libs/alsa-oss
	media-sound/alsa-utils
	app-laptop/pbbuttonsd

boot/kernel/ppc64/sources: sys-kernel/gentoo-sources
boot/kernel/ppc64/use: extlib usb oss atm truetype -qt -qt3 -qt4
boot/kernel/ppc64/config: /root/livecd/kconfig/releases/2007.1/ppc/ppc64/livecd-2.6.20-ppc64.config
boot/kernel/ppc64/console: ttyS0,57600
boot/kernel/ppc64/extraversion: ppc64

boot/kernel/pegasos/config: /root/livecd/kconfig/releases/2007.1/ppc/ppc32/installcd-2.6.20-pegasos.config
boot/kernel/pegasos/sources: sys-kernel/gentoo-sources
boot/kernel/pegasos/use: usb -X png truetype
boot/kernel/pegasos/extraversion: pegasos
boot/kernel/pegasos/gk_kernargs: --no-initrdmodules --genzimage --kernel-cross-compile=powerpc-unknown-linux-gnu-
#boot/kernel/pegasos/packages:
#	net-dialup/slmodem
#	net-dialup/globespan-adsl
#	net-dialup/fritzcapi
#	net-dialup/fcdsl

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
