subarch: amd64
target: livecd-stage2
version_stamp: uclibc-hardened-20121016
rel_type: hardened/amd64
profile: hardened/linux/uclibc/amd64
snapshot: current
source_subpath: hardened/amd64/livecd-stage2-amd64-uclibc-hardened


livecd/fstype: squashfs
livecd/fsops:
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/isolinux-3.72-cdtar.tar.bz2
livecd/iso: installcd-amd64-uclibc-minimal.iso
livecd/fsscript:
livecd/splash_theme:
livecd/bootargs:
livecd/gk_mainargs:
livecd/linuxrc:
livecd/type: generic-livecd
livecd/readme:
livecd/motd:
livecd/modblacklist:
livecd/rcadd:
livecd/rcdel:
livecd/overlay:
livecd/root_overlay:
livecd/xinitrc:
livecd/xdm:
livecd/xsession:
livecd/users: gentoo
livecd/volid:

boot/kernel: gentoo
#boot/kernel/gentoo/sources: hardened-sources
boot/kernel/gentoo/config: /tmp/hardened.config
boot/kernel/gentoo/gk_kernargs:
boot/kernel/gentoo/use:
boot/kernel/gentoo/extraversion:
boot/kernel/gentoo/packages:

livecd/unmerge:

livecd/empty: /var/tmp /var/cache /var/db /var/empty /var/lock /var/log /var/run /var/spool /var/state /tmp /usr/portage /usr/src /etc/cron.daily /etc/cron.hourly /etc/cron.monthly /etc/cron.weekly /etc/logrotate.d /etc/rsync /usr/local 

livecd/rm:
