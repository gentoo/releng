#!/bin/bash

ROOTFS="desktop-amd64-uclibc-hardened"

PWD="$(pwd)"
STAGE3="/var/tmp/catalyst/builds/hardened/amd64/stage3-amd64-uclibc-hardened.tar.bz2"
LAYMAN="/var/lib/layman"
KERNEL_SOURCE="/usr/src/linux-lilblue"


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
	mount --bind /sys/ "${ROOTFS}"/sys/
}

add_overlay() {
	layman -S
	mkdir "${ROOTFS}"/"${LAYMAN}"
	cp -a "${LAYMAN}"/hardened-development/ "${ROOTFS}"/"${LAYMAN}"
	cp installed.xml "${ROOTFS}"/"${LAYMAN}"/installed.xml
	cp make.conf.layman "${ROOTFS}"/"${LAYMAN}"/make.conf
}

populate_etc() {
	cp -f fstab "${ROOTFS}"/etc/fstab 
	cp -f lilo.conf "${ROOTFS}"/etc/lilo.conf

	rm -f "${ROOTFS}"/etc/portage/make.conf.catalyst
	cp -f portage/make.conf.1 "${ROOTFS}"/etc/portage/make.conf

	for d in env package.accept_keywords package.mask package.use profile; do
		[[ -a portage/"${d}" ]] && cp -af portage/${d} "${ROOTFS}"/etc/portage
	done
	cp -af portage/package.env "${ROOTFS}"/etc/portage
}

rebuild_toolchain() {
	cp -f toolchain.sh "${ROOTFS}"/tmp/
	chroot "${ROOTFS}"/ /tmp/toolchain.sh
	rm -f "${ROOTFS}"/tmp/toolchain.sh
}

rebuild_world() {
	cp -f portage/make.conf.2 "${ROOTFS}"/etc/portage/make.conf
	cp -f world "${ROOTFS}"/var/lib/portage/world
	cp -f rebuild.sh "${ROOTFS}"/tmp/
	chroot "${ROOTFS}"/ /tmp/rebuild.sh
	rm -f "${ROOTFS}"/tmp/rebuild.sh
}


update_world() {
	cp -f portage/make.conf.3 "${ROOTFS}"/etc/portage/make.conf
	cp -f update.sh "${ROOTFS}"/tmp/
	chroot "${ROOTFS}"/ /tmp/update.sh
	rm -f "${ROOTFS}"/tmp/update.sh
}

build_kernel() {
	mkdir -p "${ROOTFS}"/boot

	genkernel \
		--kernel-config=config \
		--makeopts=-j9 \
		--symlink \
		--no-mountboot \
		--kerneldir="${KERNEL_SOURCE}" \
		--bootdir="${PWD}"/"${ROOTFS}"/boot/ \
		--module-prefix="${PWD}"/"${ROOTFS}"/ \
		--modprobedir="${PWD}"/"${ROOTFS}"/etc/modprobe.d \
		all

	for i in $(find "${PWD}"/"${ROOTFS}"/lib/modules -iname *ko); do
		objcopy --strip-unneeded $i
	done
}

setup_initrc() {
	ln -sf net.lo "${ROOTFS}"/etc/init.d/net.eth0
	chroot "${ROOTFS}"/ rc-update add alsasound default
	chroot "${ROOTFS}"/ rc-update add cupsd default
	chroot "${ROOTFS}"/ rc-update add fcron default
	chroot "${ROOTFS}"/ rc-update add net.eth0 default
	chroot "${ROOTFS}"/ rc-update add postfix default
	chroot "${ROOTFS}"/ rc-update add sshd default
	chroot "${ROOTFS}"/ rc-update add xdm default
	chroot "${ROOTFS}"/ rc-update add avahi-daemon default
	chroot "${ROOTFS}"/ rc-update add dbus default
	chroot "${ROOTFS}"/ rc-update add samba default
	chroot "${ROOTFS}"/ rc-update add syslog-ng default
}

setup_usergroups() {
	cp -f passwd.sh "${ROOTFS}"/tmp/
	chroot  "${ROOTFS}"/ /tmp/passwd.sh
	rm -f "${ROOTFS}"/tmp/passwd.sh

	rm -rf "${ROOTFS}"/home/gentoo
	cp -a gentoo "${ROOTFS}"/home/
	mkdir "${ROOTFS}"/home/gentoo/{Desktop,Documents,Downloads,Music,Pictures,Public,Templates,Videos}
	chroot "${ROOTFS}"/ chown -R gentoo:gentoo /home/gentoo
	sed -i 's/# \(%wheel.*NOPASSWD\)/\1/' "${ROOTFS}"/etc/sudoers
}

setup_confs() {
	sed -i 's/^\(DISPLAYMANAGER="\)xdm/\1slim/' "${ROOTFS}"/etc/conf.d/xdm
	sed -i 's/^\(login.*\)/# \1/' "${ROOTFS}"/etc/slim.conf
	sed -i '/# login_cmd.*Xsession/ a\login_cmd exec /bin/bash -login ~/.xinitrc' "${ROOTFS}"/etc/slim.conf
	wget -O "${ROOTFS}"/usr/share/slim/themes/default/background.jpg http://www.gentoo.org/images/backgrounds/gentoo1600x1200.jpg

	sed -i '/^SYNC/d' "${ROOTFS}"/etc/portage/make.conf
	sed -i '/^GENTOO_MIRRORS/d' "${ROOTFS}"/etc/portage/make.conf
	sed -i 's/^MAKEOPTS/#MAKEOPTS/' "${ROOTFS}"/etc/portage/make.conf
}

cleanup_dirs() {
	rm -rf "${ROOTFS}"/tmp/*
	rm -rf "${ROOTFS}"/var/log/*
	rm -rf "${ROOTFS}"/var/tmp/*
}

unmount_dirs() {
	umount "${ROOTFS}"/sys/
	umount "${ROOTFS}"/dev/pts/
	umount "${ROOTFS}"/dev/
	umount "${ROOTFS}"/proc/
	umount "${ROOTFS}"/usr/portage/
}

bundle_it() {
	local DATE=$(date +%Y%m%d)
	local NAME="${ROOTFS}"-"${DATE}".tar.bz2
	local DIGESTS="${NAME}".DIGESTS

	cd "${ROOTFS}"
	tar -j -c -f ../"${NAME}" .

	cd ..
	>"${DIGESTS}"

	echo "# MD5 HASH" >> "${DIGESTS}"
	md5sum "${NAME}" >> "${DIGESTS}"

	echo "# SHA1 HASH" >> "${DIGESTS}"
	sha1sum "${NAME}" >> "${DIGESTS}"

	echo "# SHA512 HASH" >> "${DIGESTS}"
	sha512sum "${NAME}" >> "${DIGESTS}"

	echo "# WHIRLPOOL HASH" >> "${DIGESTS}"
	whirlpooldeep "${NAME}" >> "${DIGESTS}"
}

main() {
	unpack_stage3
	mount_dirs
	add_overlay
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
	bundle_it
}

main > zzz.log 2>&1 &
