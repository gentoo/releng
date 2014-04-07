#!/bin/bash

TEST_ARCH=$(file -b /usr/lib/libc.so | sed -e 's/^.*shared object, //' -e 's/,.*$//')

if [[ "${TEST_ARCH}" == "Intel 80386" ]]; then
	MY_ARCH="i686"
	MY_CHOST="i686-gentoo-linux-musl"
	MY_CFLAGS=""
	MY_PROF="x86"
	MY_PATH="i386"
elif [[ "${TEST_ARCH}" == "x86-64" ]]; then
	MY_ARCH="amd64"
	MY_CHOST="x86_64-gentoo-linux-musl"
	MY_CFLAGS=""
	MY_PROF="amd64"
	MY_PATH="x86_64"
elif [[ "${TEST_ARCH}" == "ARM" ]]; then
	# Need better logic for alternative subarches and hard/softfloat
	MY_ARCH="armv7a_hardfp"
	MY_CHOST="armv7a-hardfloat-linux-musleabi"
	MY_CFLAGS=" -march=armv7-a -mfpu=vfpv3-d16 -mfloat-abi=hard"
	MY_PROF="arm/armv7a"
	MY_PATH="armhf"
elif [[ "${TEST_ARCH}" == "MIPS" ]]; then
	MY_ARCH="MIPS"
	MY_CHOST="mipsel-gentoo-linux-musl"
	MY_CFLAGS=""
	MY_PROF="mips/mipsel"
	MY_PATH="mipsel"
else
	echo "Unsupported arch $TEST_ARCH"
	exit
fi

ROOTFS="stage4-${MY_ARCH}-musl-vanilla"
PWD="$(pwd)"

prepare_etc () {
	mkdir -p "${ROOTFS}"/etc
	if [[ "${MY_ARCH}" == "MIPS" ]]; then
		cp -a "${PWD}"/portage.mips/ "${ROOTFS}"/etc/portage
	else
		cp -a "${PWD}"/portage/ "${ROOTFS}"/etc/
	fi
	sed -i "s/MY_CHOST/${MY_CHOST}/" "${ROOTFS}"/etc/portage/make.conf
	sed -i "s/MY_CFLAGS/${MY_CFLAGS}/" "${ROOTFS}"/etc/portage/make.conf
	ln -sf ../../usr/portage/profiles/hardened/linux/musl/"${MY_PROF}" "${ROOTFS}"/etc/portage/make.profile
}

prepare_usr_etc() {
	mkdir -p "${ROOTFS}"/usr/etc

	cat <<-EOF > "${ROOTFS}"/usr/etc/ld-musl-${MY_PATH}.path
	/lib
	/usr/lib
	/usr/lib/gcc/${MY_CHOST}/4.7.3
	/usr/${MY_CHOST}/lib
	EOF

	# mips-muls needs some tlc upstream
	if [[ "${MY_ARCH}" == "MIPS" ]]; then
		ln -sf ld-musl-${MY_PATH}.path "${ROOTFS}"/etc/ld-musl.path
	else
		ln -sf ld-musl-${MY_PATH}.path "${ROOTFS}"/usr/etc/ld-musl.path
	fi
}

prepare_overlay() {
	# This is intensely ugly, but for now ...
	mkdir -p "${ROOTFS}"/var/lib/layman/
	cp -a /var/lib/layman/* "${ROOTFS}"/var/lib/layman/
}

emerge_system() {
	ROOT="${ROOTFS}" emerge --keep-going --with-bdeps=y -uvq @system
	FEATURES="-sandbox" ROOT="${ROOTFS}" emerge --keep-going --with-bdeps=y -uvq sandbox
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
