subarch: i686
version_stamp: 10.0
target: livecd-stage2
rel_type: default
profile: default/linux/x86/10.0/desktop
snapshot: 20090806
source_subpath: default/livecd-stage1-i686-installer-10.0

livecd/bootargs: dokeymap
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/isolinux-elilo-memtest86+-cdtar.tar.bz2
#livecd/fsscript: /home/agaffney/release/10.0/scripts/livecd.sh
livecd/fstype: squashfs
livecd/gk_mainargs: --lvm --dmraid --evms --mdadm --makeopts=-j8
livecd/iso: /var/tmp/catalyst/builds/default/livecd-i686-installer-10.0.iso
livecd/type: gentoo-release-livecd
livecd/volid: Gentoo Linux 10.0 x86 LiveCD
livecd/xdm: gdm
livecd/xsession: xfce

#livecd/overlay: /home/agaffney/release/10.0/overlays/common/overlay/livecd
#livecd/root_overlay: /home/agaffney/release/10.0/overlays/common/root_overlay

boot/kernel: gentoo

boot/kernel/gentoo/sources: gentoo-sources
boot/kernel/gentoo/config: /var/svnroot/releng/trunk/releases/10.0/kconfig/x86/installcd-2.6.28.config
boot/kernel/gentoo/use:
	atm
	fbcondecor
	mng
	png
	portaudio
	truetype
	usb
boot/kernel/gentoo/packages:
# new packages
	app-accessibility/espeakup
	net-dialup/ppp
	net-dialup/pppconfig
	net-dialup/rp-pppoe
	net-dialup/speedtouch-usb
	net-firewall/iptables
	net-wireless/ndiswrapper
	sys-apps/lm_sensors
# failed
#	sys-apps/pcmcia-cs
	sys-fs/sshfs-fuse
# end new packages	
	media-libs/alsa-oss
	media-sound/alsa-utils
#	net-dialup/fcdsl
#	net-dialup/fritzcapi
	net-dialup/globespan-adsl
	net-dialup/slmodem
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
