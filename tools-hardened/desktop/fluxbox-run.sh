#!/bin/bash

ARCH=${ARCH:-"amd64"}
ROOTFS="th-${ARCH}-fluxbox"

PWD="$(pwd)"
STAGE3="/var/tmp/catalyst/builds/hardened/${ARCH}/stage3-${ARCH}-hardened-latest.tar.bz2"
LAYMAN="/var/lib/layman"
KERNEL_SOURCE="/usr/src/linux-tinhat"


unpack_stage3() {
	mkdir "${ROOTFS}"
	tar -x -C "${ROOTFS}" -f "${STAGE3}"
}

mount_dirs() {
	mkdir "${ROOTFS}"/usr/portage/
	mount --bind /usr/portage/ "${ROOTFS}"/usr/portage/
	mount --bind /proc/ "${ROOTFS}"/proc/
	mount --bind /dev/ "${ROOTFS}"/dev/
	mount --bind /dev/pts "${ROOTFS}"/dev/pts/
	mount -t tmpfs shm "${ROOTFS}"/dev/shm
	mount --bind /sys/ "${ROOTFS}"/sys/
}

populate_etc() {
	cp -f files/fstab "${ROOTFS}"/etc/fstab
	cp -f files/resolv.conf "${ROOTFS}"/etc/resolv.conf

	rm -f "${ROOTFS}"/etc/portage/make.conf.catalyst
	cp -f files/portage/make.xfce4.1 "${ROOTFS}"/etc/portage/make.conf
	cp -f files/portage/package.gnome.accept_keywords "${ROOTFS}"/etc/portage/package.accept_keywords
	cp -f files/portage/package.xfce4.use "${ROOTFS}"/etc/portage/package.use
	cp -af files/portage/profile "${ROOTFS}"/etc/portage/profile
	cp -af files/portage/repos.conf "${ROOTFS}"/etc/portage/repos.conf
}

rebuild_toolchain() {
	cp -f toolchain.sh "${ROOTFS}"/tmp/
	chroot "${ROOTFS}"/ /tmp/toolchain.sh
	rm -f "${ROOTFS}"/tmp/toolchain.sh
}

rebuild_world() {
	cp -f files/portage/make.xfce4.1 "${ROOTFS}"/etc/portage/make.conf
	cp -f files/fluxbox-world "${ROOTFS}"/var/lib/portage/world
	cp -f rebuild.sh "${ROOTFS}"/tmp/
	chroot "${ROOTFS}"/ /tmp/rebuild.sh
	rm -f "${ROOTFS}"/tmp/rebuild.sh
}


update_world() {
	cp -f files/portage/make.xfce4.2 "${ROOTFS}"/etc/portage/make.conf
	cp -f update.sh "${ROOTFS}"/tmp/
	chroot "${ROOTFS}"/ /tmp/update.sh
	rm -f "${ROOTFS}"/tmp/update.sh
}

build_kernel() {
    local TH_BOOT="http://dev.gentoo.org/~twitch153/tinhat/th-boot.tar.gz"
	mkdir -p "${ROOTFS}"/boot

	genkernel \
		--kernel-config=files/kernel-config \
		--makeopts=-j9 \
		--static \
		--symlink \
		--no-mountboot \
		--kerneldir="${KERNEL_SOURCE}" \
		--bootdir="${PWD}"/"${ROOTFS}"/boot/ \
		all

	#for i in $(find "${PWD}"/"${ROOTFS}"/lib/modules -iname *ko); do
	#   objcopy --strip-unneeded $i
	#done
	rm -rf "${PWD}"/"${ROOTFS}"/boot/initramfs*
    wget -O "${PWD}"/th-boot.tar.gz "${TH_BOOT}"
    tar -x -C "${PWD}"/files -f th-boot.tar.gz
	cp -Rf files/th-boot/grub "${ROOTFS}"/boot
    rm -f "${PWD}"/th-boot.tar.gz
}

setup_initrc() {
	ln -sf net.lo "${ROOTFS}"/etc/init.d/net.eth0
	chroot "${ROOTFS}"/ rc-update add acpid boot
	chroot "${ROOTFS}"/ rc-update add alsasound boot
	chroot "${ROOTFS}"/ rc-update add cpufrequtils boot
	chroot "${ROOTFS}"/ rc-update add device-mapper boot
	chroot "${ROOTFS}"/ rc-update add lvm boot
	chroot "${ROOTFS}"/ rc-update add udev boot
	chroot "${ROOTFS}"/ rc-update add cupsd default
	chroot "${ROOTFS}"/ rc-update add cronie default
	chroot "${ROOTFS}"/ rc-update add net.eth0 default
	chroot "${ROOTFS}"/ rc-update add postfix default
	chroot "${ROOTFS}"/ rc-update add sshd default
	chroot "${ROOTFS}"/ rc-update add xdm default
	chroot "${ROOTFS}"/ rc-update add avahi-daemon default
	chroot "${ROOTFS}"/ rc-update add dbus default
	chroot "${ROOTFS}"/ rc-update add samba default
	chroot "${ROOTFS}"/ rc-update add syslog-ng default
	chroot "${ROOTFS}"/ rc-update add udev-postmount default
	chroot "${ROOTFS}"/ rc-update add kmod-static-nodes sysinit
	chroot "${ROOTFS}"/ rc-update add udev-mount sysinit
}

setup_usergroups() {
	local DCONF_LOCAL="http://dev.gentoo.org/~blueness/lilblue/user"

	cp -f passwd.sh "${ROOTFS}"/tmp/
	chroot  "${ROOTFS}"/ /tmp/passwd.sh
	rm -f "${ROOTFS}"/tmp/passwd.sh

	rm -rf "${ROOTFS}"/etc/skel
	cp -a thuser "${ROOTFS}"/etc/skel

	cp -f files/usermenu "${ROOTFS}"/usr/share/fluxbox/
	sed -i 's/^\/usr\/*.*/\/usr\/bin\/fluxbox/' "${ROOTFS}"/etc/skel/.xinitrc
	mkdir -p "${ROOTFS}"/etc/skel/{Desktop,Documents,Downloads,Music,Pictures,Public,Templates,Videos,.ssh,.cache/dconf,.config/dconf}
	chmod 700 "${ROOTFS}"/etc/skel/.ssh
	wget -O "${ROOTFS}"/etc/skel/.config/dconf/user "${DCONF_LOCAL}"
	wget -O "${ROOTFS}"/etc/skel/.cache/dconf/user "${DCONF_LOCAL}"

	rm -rf "${ROOTFS}"/home/thuser
	cp -a thuser "${ROOTFS}"/home/thuser
    sed -i -e 's/^\/usr\/*.*/\/usr\/bin\/fluxbox/' "${ROOTFS}"/home/thuser/.xinitrc
    cp -f files/usermenu "${ROOTFS}"/home/thuser/.fluxbox/my-menu
	cp -a files/{Encrypt,Save,Utilities} "${ROOTFS}"/home/thuser
	rm -rf "${ROOTFS}"/home/thuser/Utilities/post_gnome3_install.sh
	mkdir -p "${ROOTFS}"/home/thuser/{Desktop,Documents,Downloads,Music,Pictures,Public,Templates,Videos,.ssh,.cache/dconf,.config/dconf}
	chmod 700 "${ROOTFS}"/home/thuser/.ssh
	wget -O "${ROOTFS}"/home/thuser/.config/dconf/user "${DCONF_LOCAL}"
	wget -O "${ROOTFS}"/home/thuser/.cache/dconf/user "${DCONF_LOCAL}"

	chroot "${ROOTFS}"/ chown -R thuser:thuser /home/thuser
	sed -i 's/# \(%wheel.*NOPASSWD\)/\1/' "${ROOTFS}"/etc/sudoers
	sed -i 's/^\/usr\/*.*/\/usr\/bin\/fluxbox/' "${ROOTFS}"/etc/skel/.xinitrc
}

setup_confs() {
	local IMAGE="http://dev.gentoo.org/~blueness/lilblue/gentoo1600x1200.jpg"
    
	sed -i 's/^\(DISPLAYMANAGER="\)xdm/\1slim/' "${ROOTFS}"/etc/conf.d/xdm
	sed -i 's/^\(login.*\)/# \1/' "${ROOTFS}"/etc/slim.conf
	sed -i '/# login_cmd.*Xsession/ a\login_cmd exec /bin/bash -login ~/.xinitrc' "${ROOTFS}"/etc/slim.conf
	sed -i 's/^\(sessiondir.*\)/# \1/' "${ROOTFS}"/etc/slim.conf
	sed -i '/# sessiondir.*/ a\sessiondir /etc/X11/Sessions' "${ROOTFS}"/etc/slim.conf
	sed -i 's/^session\.menuFile.*./session\.menuFile:  \~\/.fluxbox\/my-menu/' "${ROOTFS}"/usr/share/fluxbox/init
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
	# NOTE: Current TinHat kernel uses kernel-3.7.5-hardened-r1
	#sed -i 's/^#\(disallow-other-stacks=\)no/\1yes/g' "${ROOTFS}"/etc/avahi/avahi-daemon.conf
}

cleanup_dirs() {
	rm -rf "${ROOTFS}"/tmp/*
	rm -rf "${ROOTFS}"/var/cache/*
	rm -rf "${ROOTFS}"/var/log/*
	rm -rf "${ROOTFS}"/var/tmp/*
	rm -rf "${ROOTFS}"/etc/resolv.conf
	rm -rf "${ROOTFS}"/etc/ssh/*key*
	rm -rf "${ROOTFS}"/root/.viminfo
	for i in ${ROOTFS}/root/.bash_history ; do >$i; done
	find ${ROOTFS}*/var/log -size +1c -type f -exec rm {} +
}

unmount_dirs() {
	umount "${ROOTFS}"/sys/
	umount "${ROOTFS}"/dev/shm
	umount "${ROOTFS}"/dev/pts/
	umount "${ROOTFS}"/dev/
	umount "${ROOTFS}"/proc/
	umount "${ROOTFS}"/usr/portage/

	mkdir "${ROOTFS}"/usr/portage/profiles/
	echo "gentoo" >> "${ROOTFS}"/usr/portage/profiles/repo_name
}

make_iso() {
    MYROOT="${ROOTFS}" ./make.sh
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

main > fluxbox-${ARCH}-build.log 2>&1 &
