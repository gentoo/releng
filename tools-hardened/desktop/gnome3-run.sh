#!/bin/bash

ARCH=${ARCH:-"amd64"}
ROOTFS="th-${ARCH}-gnome"

PWD="$(pwd)"
STAGE3="/var/tmp/catalyst/builds/hardened/${ARCH}/stage3-${ARCH}-hardened-latest.tar.bz2"
LAYMAN="/var/lib/layman"
KERNEL_SOURCE="/usr/src/linux-tinhat"

BASE="gnome"
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
	mkdir -p "${ROOTFS}"/etc/skel/{Desktop,Documents,Downloads,Music,Pictures,Public,Templates,Videos,.ssh,.cache/dconf,.config/dconf}
	chmod 700 "${ROOTFS}"/etc/skel/.ssh
	wget -O "${ROOTFS}"/etc/skel/.config/dconf/user "${DCONF_LOCAL}"
	wget -O "${ROOTFS}"/etc/skel/.cache/dconf/user "${DCONF_LOCAL}"

	rm -rf "${ROOTFS}"/home/thuser
	cp -a thuser "${ROOTFS}"/home/thuser
	cp -a files/{Encrypt,Save,Utilities} "${ROOTFS}"/home/thuser
	rm -rf "${ROOTFS}"/home/thuser/Utilities/post_xfce4_install.sh
	mkdir -p "${ROOTFS}"/home/thuser/{Desktop,Documents,Downloads,Music,Pictures,Public,Templates,Videos,.ssh,.cache/dconf,.config/dconf}
	chmod 700 "${ROOTFS}"/home/thuser/.ssh
	wget -O "${ROOTFS}"/home/thuser/.config/dconf/user "${DCONF_LOCAL}"
	wget -O "${ROOTFS}"/home/thuser/.cache/dconf/user "${DCONF_LOCAL}"

	chroot "${ROOTFS}"/ chown -R thuser:thuser /home/thuser
	sed -i 's/# \(%wheel.*NOPASSWD\)/\1/' "${ROOTFS}"/etc/sudoers
}

setup_confs() {
	local IMAGE="http://dev.gentoo.org/~blueness/lilblue/gentoo1600x1200.jpg"

	sed -i 's/^\(DISPLAYMANAGER="\)xdm/\1gdm/' "${ROOTFS}"/etc/conf.d/xdm

	wget -O "${ROOTFS}"/usr/share/backgrounds/background.jpg "${IMAGE}"

	sed -i '/^SYNC/d' "${ROOTFS}"/etc/portage/make.conf
	sed -i '/^GENTOO_MIRRORS/d' "${ROOTFS}"/etc/portage/make.conf
	sed -i 's/^MAKEOPTS/#MAKEOPTS/' "${ROOTFS}"/etc/portage/make.conf
	sed -i 's/^exec \/sbin\/*.*/exec \/sbin\/switch_root \/mnt\/tmpfs \/usr\/lib\/systemd\/systemd/' configs/init
        sed -i 's/^clock=\"*.*\"$/clock=\"local\"/' "${ROOTFS}"/etc/conf.d/hwclock

        cp -a files/locale/locale.gen "${ROOTFS}"/etc/
        chroot "${ROOTFS}"/ locale-gen

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
	setup_systemd
	setup_usergroups
	setup_confs
	cleanup_dirs
	unmount_dirs
	make_iso
}

main > gnome3-"${ARCH}"-build.log 2>&1 &
