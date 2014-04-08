#!/bin/bash

ARCH=${ARCH:-"amd64"}
ROOTFS="th-${ARCH}-xfce4"

PWD="$(pwd)"
STAGE3="/var/tmp/catalyst/builds/hardened/${ARCH}/stage3-${ARCH}-hardened-latest.tar.bz2"
LAYMAN="/var/lib/layman"
KERNEL_SOURCE="/usr/src/linux-tinhat"

BASE="xfce4"
MAKE_BASE="${BASE}"
KEYWORDS_BASE="${BASE}"
USE_BASE="${BASE}"
WORLD_BASE="${BASE}"

source run-base.sh

setup_usergroups() {
	local DCONF_LOCAL="http://dev.gentoo.org/~blueness/lilblue/user"

	cp -f passwd.sh "${ROOTFS}"/tmp/
	chroot  "${ROOTFS}"/ /tmp/passwd.sh
	rm -f "${ROOTFS}"/tmp/passwd.sh

	rm -rf "${ROOTFS}"/etc/skel
	cp -a thuser "${ROOTFS}"/etc/skel
	sed -i 's/^\/usr\/*.*/\/usr\/bin\/startxfce4/' "${ROOTFS}"/etc/skel/.xinitrc
	mkdir -p "${ROOTFS}"/etc/skel/{Desktop,Documents,Downloads,Music,Pictures,Public,Templates,Videos,.ssh,.cache/dconf,.config/dconf}
	chmod 700 "${ROOTFS}"/etc/skel/.ssh
	wget -O "${ROOTFS}"/etc/skel/.config/dconf/user "${DCONF_LOCAL}"
	wget -O "${ROOTFS}"/etc/skel/.cache/dconf/user "${DCONF_LOCAL}"

	rm -rf "${ROOTFS}"/home/thuser
	cp -a thuser "${ROOTFS}"/home/thuser
    sed -i -e 's/^\/usr\/*.*/\/usr\/bin\/startxfce4/' "${ROOTFS}"/home/thuser//.xinitrc
	cp -a files/{Encrypt,Save,Utilities} "${ROOTFS}"/home/thuser
	rm -rf "${ROOTFS}"/home/thuser/Utilities/post_gnome3_install.sh
	mkdir -p "${ROOTFS}"/home/thuser/{Desktop,Documents,Downloads,Music,Pictures,Public,Templates,Videos,.ssh,.cache/dconf,.config/dconf}
	chmod 700 "${ROOTFS}"/home/thuser/.ssh
	wget -O "${ROOTFS}"/home/thuser/.config/dconf/user "${DCONF_LOCAL}"
	wget -O "${ROOTFS}"/home/thuser/.cache/dconf/user "${DCONF_LOCAL}"

	chroot "${ROOTFS}"/ chown -R thuser:thuser /home/thuser
	sed -i 's/# \(%wheel.*NOPASSWD\)/\1/' "${ROOTFS}"/etc/sudoers
	sed -i 's/^\/usr\/*.*/\/usr\/bin\/startxfce4/' "${ROOTFS}"/etc/skel/.xinitrc
}

setup_confs() {
	local IMAGE="http://dev.gentoo.org/~blueness/lilblue/gentoo1600x1200.jpg"
    
	sed -i 's/^\(DISPLAYMANAGER="\)xdm/\1slim/' "${ROOTFS}"/etc/conf.d/xdm
	sed -i 's/^\(login.*\)/# \1/' "${ROOTFS}"/etc/slim.conf
	sed -i '/# login_cmd.*Xsession/ a\login_cmd exec /bin/bash -login ~/.xinitrc' "${ROOTFS}"/etc/slim.conf
	sed -i 's/^\(sessiondir.*\)/# \1/' "${ROOTFS}"/etc/slim.conf
	sed -i '/# sessiondir.*/ a\sessiondir /etc/X11/Sessions' "${ROOTFS}"/etc/slim.conf

	wget -O "${ROOTFS}"/usr/share/backgrounds/background.jpg "${IMAGE}"

	sed -i '/^SYNC/d' "${ROOTFS}"/etc/portage/make.conf
	sed -i '/^GENTOO_MIRRORS/d' "${ROOTFS}"/etc/portage/make.conf
	sed -i 's/^MAKEOPTS/#MAKEOPTS/' "${ROOTFS}"/etc/portage/make.conf
	sed -i 's/^exec \/sbin\/*.*/exec \/sbin\/switch_root \/mnt\/tmpfs \/sbin\/init/' configs/init
	sed -i 's/^clock=\"*.*\"$/clock=\"local\"/' "${ROOTFS}"/etc/conf.d/hwclock

	cp -a files/locale/locale.gen "${ROOTFS}"/etc/
	chroot "${ROOTFS}"/ locale-gen
	chroot "${ROOTFS}"/ eselect locale set 3
	cp -a files/locale/02locale "${ROOTFS}"/etc/conf.d/
	# In kernels 3.9 and above, we must disallow-other-stacks because of SO_REUSEPORT 
	sed -i 's/^#\(disallow-other-stacks=\)no/\1yes/g' "${ROOTFS}"/etc/avahi/avahi-daemon.conf
}

main() {
	unpack_stage3
	mount_dirs
	populate_etc
	rebuild_toolchain
	rebuild_world
	update_world
	build_kernel
	setup_initrc
	setup_usergroups
	setup_confs
	cleanup_dirs
	unmount_dirs
	make_iso
}

main > xfce4-"${ARCH}"-build.log 2>&1 &
