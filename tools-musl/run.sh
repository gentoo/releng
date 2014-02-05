#!/bin/bash

MYARCH=${1:-"amd64"}

if [[ "$MYARCH" != "amd64" && "$MYARCH" != "i686" ]]; then
	echo "Unsupported arch $MYARCH"
	exit
fi

[[ "$MYARCH" == "amd64" ]] && ALTARCH="x86_64"
[[ "$MYARCH" == "i686" ]] && ALTARCH="i386"

ROOTFS="stage4-${MYARCH}-musl-vanilla"
PWD="$(pwd)"

prepare_etc () {
	mkdir -p "${ROOTFS}"/etc
	cp -a "${PWD}"/portage/ "${ROOTFS}"/etc/

	if [[ "$MYARCH" == "amd64" ]]; then
		sed -i "s/ALTARCH/${ALTARCH}/" "${ROOTFS}"/etc/make.conf
	elif [[ "$MYARCH" == "i686" ]]; then
		sed -i "s/ALTARCH/${MYARCH}/" "${ROOTFS}"/etc/make.conf
	fi
}

prepare_usr_etc() {
	mkdir -p "${ROOTFS}"/usr/etc

	cat <<-EOF > "${ROOTFS}"/usr/etc/ld-musl-${ALTARCH}.path
	/lib
	/usr/lib
	/usr/lib/gcc/${ALTARCH}-gentoo-linux-musl/4.7.3
	/usr/${ALTARCH}-gentoo-linux-musl/lib
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
