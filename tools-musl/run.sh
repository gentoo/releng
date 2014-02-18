#!/bin/bash

TEST_ARCH=$(file -b /usr/lib/libc.so | sed -e 's/^.*shared object, //' -e 's/,.*$//')

if [[ "${TEST_ARCH}" == "Intel 80386" ]]; then
	MY_ARCH="i686"
	ALTARCH="i386"
elif [[ "${TEST_ARCH}" == "x86-64" ]]; then
	MY_ARCH="amd64"
	ALTARCH="x86_64"
else
	echo "Unsupported arch $TEST_ARCH"
	exit
fi

ROOTFS="stage4-${MY_ARCH}-musl-vanilla"
PWD="$(pwd)"

prepare_etc () {
	mkdir -p "${ROOTFS}"/etc
	cp -a "${PWD}"/portage/ "${ROOTFS}"/etc/

	if [[ "$MY_ARCH" == "amd64" ]]; then
		sed -i "s/ALTARCH/${ALTARCH}/" "${ROOTFS}"/etc/portage/make.conf
		ln -sf ../../usr/portage/profiles/hardened/linux/musl/amd64 "${ROOTFS}"/etc/portage/make.profile
	elif [[ "$MY_ARCH" == "i686" ]]; then
		sed -i "s/ALTARCH/${MY_ARCH}/" "${ROOTFS}"/etc/portage/make.conf
		ln -sf ../../usr/portage/profiles/hardened/linux/musl/x86 "${ROOTFS}"/etc/portage/make.profile
	fi
}

prepare_usr_etc() {
	mkdir -p "${ROOTFS}"/usr/etc

	local PATH_ARCH

	[[ "$MY_ARCH" == "amd64" ]] && PATH_ARCH="x86_64"
	[[ "$MY_ARCH" == "i686" ]] && PATH_ARCH="i686"

	cat <<-EOF > "${ROOTFS}"/usr/etc/ld-musl-${ALTARCH}.path
	/lib
	/usr/lib
	/usr/lib/gcc/${PATH_ARCH}-gentoo-linux-musl/4.7.3
	/usr/${PATH_ARCH}-gentoo-linux-musl/lib
	EOF

	ln -sf ld-musl-${ALTARCH}.path "${ROOTFS}"/usr/etc/ld-musl.path
}

prepare_overlay() {
	# This is intensely ugly, but for now ...
	mkdir -p "${ROOTFS}"/var/lib/layman/
	cp -a /var/lib/layman/* "${ROOTFS}"/var/lib/layman/
}

emerge_system() {
	ROOT="${ROOTFS}" emerge --keep-going --with-bdeps=y -uvq @system 
	ROOT="${ROOTFS}" emerge --keep-going --with-bdeps=y -uvq sandbox
}

mk_top_level_dirs() {
	mkdir "${ROOTFS}"/{boot,dev,home,media,mnt,opt,proc,root,sys}
}

setup_configs() {
	sed -i '/^SYNC/d' "${ROOTFS}"/etc/portage/make.conf
	sed -i '/^GENTOO_MIRRORS/d' "${ROOTFS}"/etc/portage/make.conf
	sed -i 's/^MAKEOPTS/#MAKEOPTS/' "${ROOTFS}"/etc/portage/make.conf

	# There are some issue with python3, so let's select python2
	# which so far is option 1 in elesect python.
	chroot "${ROOTFS}" eselect python set 1
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
