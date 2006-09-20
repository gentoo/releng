# Copyright 1999-2006 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2
# $Header: /var/cvsroot/gentoo/src/releng/overlays/portage/sys-apps/gli/gli-0.3.1.ebuild,v 1.1 2006-09-20 14:23:54 wolf31o2 Exp $

inherit python eutils

DESCRIPTION="Gentoo Linux Installer"
HOMEPAGE="http://www.gentoo.org/proj/en/releng/installer/"
#SRC_URI="http://dev.gentoo.org/~agaffney/gli/snapshots/installer-${PV}.tar.bz2"
SRC_URI="http://dev.gentoo.org/~agaffney/${PN}/releases/installer-${PV}.tar.bz2"

LICENSE="GPL-2"
SLOT="0"
KEYWORDS="~amd64 ~x86"
IUSE="gtk"

RDEPEND=">=dev-python/pyparted-1.6.6
	gtk? ( >=dev-python/pygtk-2.4.0 )
	=dev-python/pythondialog-2.7*
	sys-fs/e2fsprogs
	sys-fs/hfsutils
	sys-fs/ntfsprogs
	sys-fs/reiserfsprogs
	sys-fs/dosfstools"

S=${WORKDIR}/installer/src

dir=/opt/installer
Ddir=${D}/${dir}

src_install() {
	dodir ${dir}
	exeinto ${dir}/bin
	use !gtk && rm -rf ${S}/fe/gtk
	cp -a ${S}/* ${Ddir}
	doexe ${FILESDIR}/installer-dialog ${FILESDIR}/installer \
		|| die "copying dialog/installer scripts"
	chown -R root:0 ${Ddir}
	dodir /usr/bin
	if use gtk; then
		doexe ${FILESDIR}/installer-gtk || die "copying gtk script"
		make_wrapper installer-gtk ./installer-gtk ${dir}/bin
	fi
	make_wrapper installer-dialog ./installer-dialog ${dir}/bin
	make_wrapper installer ./installer ${dir}/bin
	doicon ${FILESDIR}/gli.png ${FILESDIR}/gli-dialog.png
	domenu ${FILESDIR}/installer-gtk.desktop \
		${FILESDIR}/installer-dialog.desktop
}

pkg_postinst() {
	python_mod_optimize ${dir}
	einfo "The Gentoo Linux Installer is currently only usable for two situations."
	einfo "The first is for building an install profile."
	einfo "The second is for installing using official Gentoo release media."
	echo
	ewarn "If you are trying to use the installer for anything else, please"
	ewarn "file patches with any bugs."
	echo
}
