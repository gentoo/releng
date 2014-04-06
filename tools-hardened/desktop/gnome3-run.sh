#!/bin/bash

ARCH=${ARCH:-"amd64"}
ROOTFS="th-${ARCH}-gnome"

PWD="$(pwd)"
STAGE3="/var/tmp/catalyst/builds/hardened/amd64/stage3-amd64-hardened-latest.tar.bz2"
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
	cp -f files/portage/make.gnome.1 "${ROOTFS}"/etc/portage/make.conf

	cp -f files/portage/package.gnome.accept_keywords "${ROOTFS}"/etc/portage/package.accept_keywords
	cp -f files/portage/package.gnome.use "${ROOTFS}"/etc/portage/package.use
	cp -af files/portage/profile "${ROOTFS}"/etc/portage/profile
	cp -af files/portage/repos.conf "${ROOTFS}"/etc/portage/repos.conf
}

rebuild_toolchain() {
	cp -f toolchain.sh "${ROOTFS}"/tmp/
	chroot "${ROOTFS}"/ /tmp/toolchain.sh
	rm -f "${ROOTFS}"/tmp/toolchain.sh
}

rebuild_world() {
	cp -f files/gnome-world "${ROOTFS}"/var/lib/portage/world
	cp -f rebuild.sh "${ROOTFS}"/tmp/
	chroot "${ROOTFS}"/ /tmp/rebuild.sh
	rm -f "${ROOTFS}"/tmp/rebuild.sh
}


update_world() {
	cp -f files/portage/make.gnome.2 "${ROOTFS}"/etc/portage/make.conf

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
	# done
	rm -rf "${PWD}"/"${ROOTFS}"/boot/initramfs*
    wget -O "${PWD}"/th-boot.tar.gz "${TH_BOOT}"
    tar -x -C "${PWD}"/files -f th-boot.tar.gz
	cp -Rf files/th-boot/grub "${ROOTFS}"/boot/
    rm -f "${PWD}"/th-boot.tar.gz
}

setup_systemd() {
	ln -sf /proc/self/mounts /etc/mtab
	sed -i -e 's/# GRUB_CMDLINE_LINUX=""/GRUB_CMDLINE_LINUX="init=\/usr\/lib\/systemd\/systemd"/' "${ROOTFS}"/etc/default/grub
	chroot "${ROOTFS}"/ systemctl enable avahi-daemon.service
	chroot "${ROOTFS}"/ systemctl enable bluetooth.service
	chroot "${ROOTFS}"/ systemctl enable cups.service
	chroot "${ROOTFS}"/ systemctl enable dhcpcd.service
	chroot "${ROOTFS}"/ systemctl enable cronie.service
	chroot "${ROOTFS}"/ systemctl enable gdm.service
	chroot "${ROOTFS}"/ systemctl enable metalog.service
	chroot "${ROOTFS}"/ systemctl enable NetworkManager.service
	chroot "${ROOTFS}"/ systemctl enable postfix.service
	chroot "${ROOTFS}"/ systemctl enable smbd.service
	chroot "${ROOTFS}"/ systemctl enable sshd.service
	#chroot "${ROOTFS}"/ systemctl enable udev.service
	#chroot "${ROOTFS}"/ systemctl enable udev-settle.service
	#chroot "${ROOTFS}"/ systemctl enable udev-trigger.service
}

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
	# NOTE: Current TinHat kernel uses kernel-3.7.5-hardened-r1
	#sed -i 's/^#\(disallow-other-stacks=\)no/\1yes/g' "${ROOTFS}"/etc/avahi/avahi-daemon.conf
}

cleanup_dirs() {
	rm -rf "${ROOTFS}"/tmp/*
	rm -rf "${ROOTFS}"/var/log/*
	rm -rf "${ROOTFS}"/var/tmp/*
	rm -rf "${ROOTFS}"/etc/resolv.conf
}

unmount_dirs() {
	umount -l "${ROOTFS}"/sys/
	umount -l "${ROOTFS}"/dev/shm
	umount -l "${ROOTFS}"/dev/pts/
	umount -l "${ROOTFS}"/dev/
	umount -l "${ROOTFS}"/proc/
	umount -l "${ROOTFS}"/usr/portage/

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
	setup_systemd
	setup_usergroups
	setup_confs
	cleanup_dirs
	unmount_dirs
	make_iso
}

main > gnome3-"${ARCH}"-build.log 2>&1 &
