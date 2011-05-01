subarch: i686
version_stamp: 11.0
target: livecd-stage2
rel_type: default
profile: default/linux/x86/10.0/desktop
snapshot: 20111003
source_subpath: default/livecd-stage1-i686-11.0

livecd/root_overlay: /var/svnroot/releng/trunk/releases/10.2/livecd/root_overlay
livecd/bootargs: dokeymap
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/isolinux-elilo-memtest86+-cdtar.tar.bz2
#livecd/fsscript: /var/svnroot/releng/trunk/releases/10.2/scripts/livecd.sh
livecd/fstype: squashfs
livecd/gk_mainargs: --lvm --dmraid --evms --mdadm --makeopts=-j8
livecd/iso: /chroot/livedvd-x86-multilib-11.0.iso
livecd/type: gentoo-release-livedvd
livecd/volid: Gentoo Linux 11.0 x86 Live(DVD/USB)
livecd/xsession: default
#livecd/splash_theme: livecd-2007.0
livecd/xdm: kdm
livecd/rcadd:
	dbus|default
	wicd|default
	avahi-daemon|default

livecd/root_overlay: /var/svnroot/releng/trunk/releases/10.2/livecd/root_overlay
boot/kernel: gentoo
boot/kernel/gentoo/sources: gentoo-sources
boot/kernel/gentoo/config:  /var/svnroot/releng/trunk/releases/10.2/kconfig/x86/installcd-2.6.37.config
boot/kernel/gentoo/use:
        atm       
        fbcondecor
        mng
        png      
        portaudio
        truetype   
        usb           
        -x264
        -mp3
	-mp4
        -mpeg2
        -mpeg4pt2
        -xvid
        -a52
        -real
        -dvdnav
        -faac
        -amr
        nautilus
        exif
        cdda
        avahi
boot/kernel/gentoo/packages:
        app-accessibility/brltty
        app-accessibility/espeak
        app-accessibility/espeakup
        app-emulation/virtualbox-guest-additions
        net-dialup/globespan-adsl
        net-dialup/mingetty
        net-dialup/minicom
        net-dialup/pppconfig
        net-dialup/pptpclient
        net-dialup/rp-pppoe
        net-firewall/iptables
        net-misc/bridge-utils
        net-misc/curl
        net-misc/dhcpcd
        net-misc/networkmanager
        net-misc/ntp
        net-misc/openswan
        net-misc/openvpn
        net-misc/putty
        net-misc/rdate
        net-misc/rdesktop
        net-misc/telnet-bsd
        net-misc/tightvnc
        net-misc/udpcast
        net-misc/vconfig
        net-misc/vpnc
        net-misc/whois
        net-misc/wicd
        net-misc/wput
        net-wireless/aircrack-ng
        net-wireless/gnome-bluetooth
        net-wireless/hostap-utils
        net-wireless/ipw2100-firmware
        net-wireless/ipw2200-firmware
        net-wireless/kismet
        net-wireless/prism54-firmware
        net-wireless/rtl8192se
        net-wireless/wepattack
        net-wireless/wireless-tools
        net-wireless/wpa_supplicant
        net-wireless/zd1201-firmware
        net-wireless/zd1211-firmware
        sys-apps/lm_sensors
        sys-block/aoetools
        sys-block/disktype
        sys-block/gpart
        sys-block/gparted
        sys-block/mbuffer
        sys-block/mpt-status
        sys-block/ms-sys
        sys-block/mtx
        sys-block/nbd
        sys-block/partimage
        sys-block/partitionmanager
        sys-fs/aufs2
        sys-fs/dd-rescue
        sys-fs/ddrescue
        sys-fs/dmraid
        sys-fs/dosfstools
        sys-fs/evms
        sys-fs/fuse
        sys-fs/hfsutils
        sys-fs/jfsutils
        sys-fs/lsscsi
        sys-fs/lvm2
        sys-fs/mac-fdisk
        sys-fs/mdadm
        sys-fs/ntfs3g
        sys-fs/ntfsprogs
        sys-fs/quota
        sys-fs/reiserfsprogs
        sys-fs/sshfs-fuse
        sys-fs/xfsdump
        sys-fs/xfsprogs
        sys-kernel/linux-firmware
        sys-kernel/module-rebuild
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
	/usr/share/autostart/kalarm.autostart.desktop
	/usr/share/autostart/nepomukserver.desktop
	/etc/*-
	/etc/*.old
	/root/.viminfo
	/var/log/*.log
	/usr/share/genkernel/pkg/x86/*.bz2
	/usr/share/xsessions/{e16-gnome.desktop,e16-kde.desktop,openbox-gnome.desktop,openbox-kde.desktop}
