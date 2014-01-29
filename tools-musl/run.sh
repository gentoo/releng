#!/bin/bash

ROOTFS="stage4-amd64-musl-vanilla"
PWD="$(pwd)"

prepare_etc () {
	mkdir -p "${ROOTFS}"/etc
	cp -a "${PWD}"/portage/ "${ROOTFS}"/etc/
}

prepare_usr_etc() {
	mkdir -p "${ROOTFS}"/usr/etc

	cat <<-EOF > "${ROOTFS}"/usr/etc/ld-musl-x86_64.path
	/lib
	/usr/lib
	/usr/lib/gcc/x86_64-gentoo-linux-musl/4.7.3
	/usr/x86_64-gentoo-linux-musl/lib
	EOF

	ln -sf ld-musl-x86_64.path "${ROOTFS}"/usr/etc/ld-musl.path
}

prepare_overlay() {
	# This is intensely ugly, but for now ...
	mkdir -p "${ROOTFS}"/var/lib/layman/
	cp -a /var/lib/layman/* "${ROOTFS}"/var/lib/layman/
}

emerge_system() {
	ROOT="${ROOTFS}" emerge --keep-going --with-bdeps=y -uvq @system 
}

mk_top_level_dirs() {
	mkdir "${ROOTFS}"/{boot,dev,home,media,mnt,opt,proc,root,sys}
}

setup_configs() {
	sed -i '/^SYNC/d' "${ROOTFS}"/etc/portage/make.conf
	sed -i '/^GENTOO_MIRRORS/d' "${ROOTFS}"/etc/portage/make.conf
	sed -i 's/^MAKEOPTS/#MAKEOPTS/' "${ROOTFS}"/etc/portage/make.conf
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

main (){
	prepare_etc
	prepare_usr_etc
	prepare_overlay
	emerge_system
	mk_top_level_dirs
	setup_configs
	bundle_it
}

main > zzz.log 2>&1 &
