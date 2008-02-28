subarch: ppc64
version_stamp: 32ul-2008.0
target: livecd-stage2
rel_type: default
profile: default/linux/powerpc/ppc64/2008.0/32bit-userland/desktop
snapshot: 2008.0
source_subpath: default/livecd-stage1-ppc64-installer-32ul-2008.0

livecd/fstype: squashfs
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/yaboot-1.3.13-cdtar.tar.bz2
livecd/iso: /var/tmp/catalyst/builds/default/livecd-ppc64-32ul-2008.0.iso
livecd/xdm: gdm
livecd/xsession: xfce
livecd/fsscript: /var/cvsroot/gentoo/src/releng/scripts/2008.0/livecd.sh

livecd/type: gentoo-release-livecd
livecd/users: xfce
livecd/volid: Gentoo Linux 2008.0 PPC LiveCD

livecd/overlay: /var/cvsroot/gentoo/src/releng/overlays/livecd/2008.0/common/overlay/livecd
livecd/root_overlay: /var/cvsroot/gentoo/src/releng/overlays/2008.0/common/root_overlay

#livecd/bootargs: dokeymap
livecd/gk_mainargs: --utils-arch=ppc --arch-override=ppc --makeopts=-j8 --lvm --dmraid --evms

livecd/rcadd: pbbuttonsd|default

boot/kernel: ibm ppc32 G5

boot/kernel/ibm/sources: sys-kernel/gentoo-sources
boot/kernel/ibm/use: atm extlib fbcondecor mng png truetype usb -qt3 -qt4 -X
boot/kernel/ibm/config: /home/ranger/2008.0/svn/releng/trunk/releases/2008.0/kconfig/powerpc/installcd-ibm-2.6.23.config
boot/kernel/ibm/console: ttyS0,9600 hvc0 hvsi0
boot/kernel/ibm/machine_type: ibm
boot/kernel/ibm/extraversion: ibm
boot/kernel/ibm/gk_kernargs: --kernel-cross-compile=powerpc64-unknown-linux-gnu-

boot/kernel/ppc32/config: /home/ranger/2008.0/svn/releng/trunk/releases/2008.0/kconfig/powerpc/installcd-ppc32apple-2.6.23.config
boot/kernel/ppc32/sources: gentoo-sources
boot/kernel/ppc32/extraversion: ppc32
boot/kernel/ppc32/use: atm fbcondecor mng png truetype usb -qt3 -qt4 -X
boot/kernel/ppc32/packages:
	sys-apps/pcmciautils
	net-misc/br2684ctl
	media-libs/alsa-lib
	media-libs/alsa-oss
	media-sound/alsa-utils
	app-laptop/pbbuttonsd

boot/kernel/G5/sources: sys-kernel/gentoo-sources
boot/kernel/G5/use: atm extlib fbcondecor mng png truetype usb -qt3 -qt4 -X
boot/kernel/G5/config: /home/ranger/2008.0/svn/releng/trunk/releases/2008.0/kconfig/powerpc/installcd-ppc64apple-2.6.23.config
boot/kernel/G5/console: ttyS0,57600
boot/kernel/G5/extraversion: ppc64
boot/kernel/G5/gk_kernargs: --kernel-cross-compile=powerpc64-unknown-linux-gnu-


#boot/kernel/pegasos/config: /var/cvsroot/gentoo/src/releng/kconfig/releases/2008.0/powerpc/ppc32/installcd-2.6.20-pegasos.config
#boot/kernel/pegasos/sources: sys-kernel/gentoo-sources
#boot/kernel/pegasos/use: atm fbcondecor mng png truetype usb -qt3 -qt4 -X
#boot/kernel/pegasos/extraversion: pegasos
#boot/kernel/pegasos/gk_kernargs: --no-initrdmodules --genzimage --kernel-cross-compile=powerpc-unknown-linux-gnu-
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
