# Copyright 1999-2006 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2
# $Header: /var/cvsroot/gentoo/src/releng/overlays/portage/sys-kernel/vanilla-sources/vanilla-sources-2.4.21.ebuild,v 1.1 2006-09-20 14:23:54 wolf31o2 Exp $

ETYPE="sources"
K_NOUSENAME="yes"
K_NOSETEXTRAVERSION="yes"
inherit kernel-2
detect_version

DESCRIPTION="Full sources for the Linux kernel"
HOMEPAGE="http://www.kernel.org"
SRC_URI="${KERNEL_URI}"
KEYWORDS="~s390"
