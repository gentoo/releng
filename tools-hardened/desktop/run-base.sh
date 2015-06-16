#!/bin/bash

unpack_stage3() {
	mkdir "${ROOTFS}"
	tar -x -C "${ROOTFS}" -f "${STAGE3}"
}

mount_dirs() {
	mkdir "${ROOTFS}"/usr/portage/
	mount --rbind /usr/portage/ "${ROOTFS}"/usr/portage/
	mount --rbind /proc/ "${ROOTFS}"/proc/
	mount --rbind /dev/ "${ROOTFS}"/dev/
	mount --rbind /sys/ "${ROOTFS}"/sys/
}

populate_kernel_src() {
	cp -f files/kernel-config "${KERNEL_SOURCE}"
	cp -Rf "${KERNEL_SOURCE}"/ "${ROOTFS}"/usr/src/
}

populate_etc() {
	cp -f files/fstab "${ROOTFS}"/etc/fstab
	cp -f files/resolv.conf "${ROOTFS}"/etc/resolv.conf

	rm -f "${ROOTFS}"/etc/portage/make.conf.catalyst
	cp -f files/portage/make."${MAKE_BASE}".1 "${ROOTFS}"/etc/portage/make.conf
	cp -f files/portage/package."${KEYWORDS_BASE}".accept_keywords "${ROOTFS}"/etc/portage/package.accept_keywords
	cp -f files/portage/package."${USE_BASE}".use.1 "${ROOTFS}"/etc/portage/package.use
	cp -af files/portage/profile "${ROOTFS}"/etc/portage/profile
	cp -af files/portage/repos.conf "${ROOTFS}"/etc/portage/repos.conf
}

rebuild_toolchain() {
	cp -f toolchain.sh "${ROOTFS}"/tmp/
	chroot "${ROOTFS}"/ /tmp/toolchain.sh
	rm -f "${ROOTFS}"/tmp/toolchain.sh
}

rebuild_world() {
	cp -f files/"${WORLD_BASE}"-world "${ROOTFS}"/var/lib/portage/world
	cp -f rebuild.sh "${ROOTFS}"/tmp/
	chroot "${ROOTFS}"/ /tmp/rebuild.sh
	rm -f "${ROOTFS}"/tmp/rebuild.sh
}

update_world() {
	cp -f files/portage/package."${USE_BASE}".use.2 "${ROOTFS}"/etc/portage/package.use
	cp -f files/portage/make."${MAKE_BASE}".2 "${ROOTFS}"/etc/portage/make.conf
	cp -f update.sh "${ROOTFS}"/tmp/
	chroot "${ROOTFS}"/ /tmp/update.sh
	rm -f "${ROOTFS}"/tmp/update.sh

	if [ "${WORLD_BASE}" == "gnome" ];
	then
		gnome_shell_loc=`chroot "${ROOTFS}"/ which gnome-shell`
		chroot "${ROOTFS}"/ paxctl-ng -vm "${gnome_shell_loc}"
		unset gnome_shell_loc
	fi
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
	#	objcopy --strip-unneeded $i
	#done
	rm -rf "${PWD}"/"${ROOTFS}"/boot/initramfs*
	wget -O "${PWD}"/th-boot.tar.gz "${TH_BOOT}"
	tar -x -C "${PWD}"/files -f th-boot.tar.gz
	cp -Rf files/th-boot/grub "${ROOTFS}"/boot/
	rm -f "${PWD}"/th-boot.tar.gz
}

setup_initrc() {
	ln -sf net.lo "${ROOTFS}"/etc/init.d/net.eth0
	chroot "${ROOTFS}"/ rc-update add acpid boot
	chroot "${ROOTFS}"/ rc-update add atd boot
	chroot "${ROOTFS}"/ rc-update add udev sysinit
	chroot "${ROOTFS}"/ rc-update add cronie default
	chroot "${ROOTFS}"/ rc-update add net.eth0 default
	chroot "${ROOTFS}"/ rc-update add postfix default
	chroot "${ROOTFS}"/ rc-update add sshd default
	chroot "${ROOTFS}"/ rc-update add xdm default
	chroot "${ROOTFS}"/ rc-update add dbus default
	chroot "${ROOTFS}"/ rc-update add syslog-ng default
	chroot "${ROOTFS}"/ rc-update add udev-postmount default
	chroot "${ROOTFS}"/ rc-update add kmod-static-nodes sysinit
	chroot "${ROOTFS}"/ rc-update add udev-mount sysinit
}

setup_systemd() {
	ln -sf /proc/self/mounts /etc/mtab
	sed -i -e 's/#GRUB_CMDLINE_LINUX=""/GRUB_CMDLINE_LINUX="init=\/usr\/lib\/systemd\/systemd"/' "${ROOTFS}"/etc/default/grub
	chroot "${ROOTFS}"/ systemctl enable atd.service
	chroot "${ROOTFS}"/ systemctl enable dhcpcd.service
	chroot "${ROOTFS}"/ systemctl enable cronie.service
	chroot "${ROOTFS}"/ systemctl enable metalog.service
	chroot "${ROOTFS}"/ systemctl enable NetworkManager.service
	chroot "${ROOTFS}"/ systemctl enable systemd-resolved
	chroot "${ROOTFS}"/ systemctl enable postfix.service
	chroot "${ROOTFS}"/ systemctl disable gdm
	chroot "${ROOTFS}"/ systemctl enable slim
	chroot "${ROOTFS}"/ systemctl enable sshd.service
	chroot "${ROOTFS}"/ systemctl disable avahi-daemon.service
	chroot "${ROOTFS}"/ systemctl disable bluetooth.serivce
	chroot "${ROOTFS}"/ systemctl disable cups.service
}

cleanup_dirs() {
	rm -rf "${ROOTFS}"/tmp/*
	rm -rf "${ROOTFS}"/usr/src/*
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
	umount -l "${ROOTFS}"/sys/
	umount -l "${ROOTFS}"/dev/
	umount -l "${ROOTFS}"/proc/
	umount -l "${ROOTFS}"/usr/portage/

	mkdir "${ROOTFS}"/usr/portage/profiles/
	echo "gentoo" >> "${ROOTFS}"/usr/portage/profiles/repo_name
}

make_iso() {
	MYROOT="${ROOTFS}" ./make.sh
}
