subarch: ppc
version_stamp: 20040926
target: livecd-stage2
rel_type: default
rel_version: 2004.3
profile: default-linux/ppc/2004.3
snapshot: 20040926
source_subpath: default/stage3-ppc-2004.3

livecd/cdfstype: squashfs
livecd/archscript: livecd/runscript/ppc-archscript.sh
livecd/runscript: livecd/runscript/default-runscript.sh
livecd/cdtar: livecd/cdtar/yaboot-1.3.11-cdtar.tar.bz2

boot/kernel: G4 G5
boot/kernel/G4/sources: sys-kernel/gentoo-dev-sources
boot/kernel/G4/config: /usr/src/configs/G4-SMP
boot/kernel/G4/use: extlib
boot/kernel/G4/extraversion: G4-SMP
boot/kernel/G5/sources: sys-kernel/gentoo-dev-sources
boot/kernel/G5/use: extlib
boot/kernel/G5/config: /usr/src/configs/G5-SMP
boot/kernel/G5/extraversion: G5-SMP

livecd/iso:
	gentoo.iso

livecd/unmerge:
	autoconf automake binutils libtool m4 bison ccache distcc make perl patch linux-headers man-pages
	sash bison flex gettext sys-apps/texinfo ccache addpatches man groff lib-compat gcc python miscfiles
	
livecd/empty:
	/var/tmp
	/var/cache
	/var/db
	/var/empty
	/var/cache
	/var/lock
	/tmp
	/usr/portage
	/usr/share/man
	/usr/share/info
	/usr/share/unimaps
	/usr/include
	/usr/share/zoneinfo
	/usr/share/dict
	/usr/share/doc
	/usr/share/ss
	/usr/share/state
	/usr/share/texinfo
	/usr/lib/python2.2
	/usr/lib/portage
	/usr/share/gettext
	/usr/share/i18n
	/usr/share/rfc
	/usr/X11R6/man
	/usr/X11R6/lib/X11/doc
	/usr/src
	/usr/share/doc
	/usr/share/man
	/root/.ccache
	
livecd/rm:
	/lib/*.a
	/usr/lib/*.pyc
	/usr/lib/*.pyo
	/usr/lib/*.a
	/usr/lib/gcc-lib/*/*/libgcj*
	/usr/X11R6/lib/*.a
