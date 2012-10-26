subarch: amd64
target: livecd-stage1
version_stamp: uclibc-hardened-20121016
rel_type: hardened/amd64
profile: hardened/linux/uclibc/amd64
snapshot: current
source_subpath: hardened/amd64/stage3-amd64-uclibc-hardened

livecd/use: mmx sse sse2 mbox -unicode

livecd/packages: app-admin/sudo app-admin/syslog-ng app-cdr/cdrtools app-editors/nano app-editors/vim app-portage/epm app-portage/gentoolkit app-portage/layman app-text/tree dev-lang/python dev-libs/libevent dev-libs/libiconv dev-util/strace dev-vcs/git mail-client/mailx mail-mta/postfix net-analyzer/iftop net-firewall/iptables net-ftp/lftp net-mail/dovecot net-misc/dhcp net-misc/dhcpcd net-misc/openntpd sys-apps/haveged sys-apps/iproute2 sys-apps/less sys-apps/pciutils sys-boot/grub-static sys-devel/gettext sys-fs/squashfs-tools sys-fs/udev sys-kernel/genkernel sys-kernel/linux-headers sys-libs/argp-standalone sys-libs/e2fsprogs-libs sys-libs/readline sys-process/fcron sys-process/lsof virtual/libiconv
