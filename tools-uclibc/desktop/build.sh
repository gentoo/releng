# These are just notes for now.  A cleaner script is coming.

mkdir desktop-amd64-uclibc-hardened
tar -x -C desktop-amd64-uclibc-hardened -f /var/tmp/catalyst/builds/hardened/amd64/stage3-amd64-uclibc-hardened.tar.bz2

mkdir desktop-amd64-uclibc-hardened/usr/portage/
mount --bind /usr/portage/ desktop-amd64-uclibc-hardened/usr/portage/
mount --bind /proc/ desktop-amd64-uclibc-hardened/proc/
mount --bind /dev/ desktop-amd64-uclibc-hardened/dev/
mount --bind /dev/pts desktop-amd64-uclibc-hardened/dev/pts/
mount --bind /sys/ desktop-amd64-uclibc-hardened/sys/

layman -S
mkdir desktop-amd64-uclibc-hardened/var/lib/layman
cp -a /var/lib/layman/hardened-development/ desktop-amd64-uclibc-hardened/var/lib/layman

cp -f fstab desktop-amd64-uclibc-hardened/etc/fstab 
cp -f lilo.conf desktop-amd64-uclibc-hardened/etc/lilo.conf

rm -f desktop-amd64-uclibc-hardened/etc/portage/make.conf.catalyst
cp -f portage/make.conf.1 desktop-amd64-uclibc-hardened/etc/portage/make.conf

for d in env package.accept_keywords package.mask package.use; do
	[[ "$(ls portage/${d})" != "" ]] && cp -f portage/${d}/* desktop-amd64-uclibc-hardened/etc/portage/${d}/
done
cp portage/package.env desktop-amd64-uclibc-hardened/etc/portage/

cp -f toolchain.sh desktop-amd64-uclibc-hardened/tmp/
chroot desktop-amd64-uclibc-hardened/ /tmp/toolchain.sh
rm -f desktop-amd64-uclibc-hardened/tmp/toolchain.sh


cp -f portage/make.conf.2 desktop-amd64-uclibc-hardened/etc/portage/make.conf
cp -f world desktop-amd64-uclibc-hardened/var/lib/portage/world
cp -f rebuild.sh desktop-amd64-uclibc-hardened/tmp/
chroot desktop-amd64-uclibc-hardened/ /tmp/rebuild.sh
rm -f desktop-amd64-uclibc-hardened/tmp/rebuild.sh


cp -f portage/make.conf.3 desktop-amd64-uclibc-hardened/etc/portage/make.conf
cp -f update.sh desktop-amd64-uclibc-hardened/tmp/
chroot desktop-amd64-uclibc-hardened/ /tmp/update.sh
rm -f desktop-amd64-uclibc-hardened/tmp/update.sh


genkernel \
	--kernel-config=config \
	--makeopts=-j9 \
	--symlink \
	--no-mountboot \
	--kerneldir=/usr/src/linux-lilblue \
	--bootdir=/root/lilblue/desktop-amd64-uclibc-hardened/boot/ \
	--module-prefix=/root/lilblue/desktop-amd64-uclibc-hardened/ \
	--modprobedir=/root/lilblue/desktop-amd64-uclibc-hardened/etc/modprobe.d \
	all

ln -sf net.lo desktop-amd64-uclibc-hardened/etc/init.d/net.eth0
chroot desktop-amd64-uclibc-hardened/ rc-update add alsasound default
chroot desktop-amd64-uclibc-hardened/ rc-update add cupsd default
chroot desktop-amd64-uclibc-hardened/ rc-update add fcron default
chroot desktop-amd64-uclibc-hardened/ rc-update add net.eth0 default
chroot desktop-amd64-uclibc-hardened/ rc-update add postfix default
chroot desktop-amd64-uclibc-hardened/ rc-update add sshd default
chroot desktop-amd64-uclibc-hardened/ rc-update add xdm default
chroot desktop-amd64-uclibc-hardened/ rc-update add avahi-daemon default
chroot desktop-amd64-uclibc-hardened/ rc-update add dbus default
chroot desktop-amd64-uclibc-hardened/ rc-update add samba default
chroot desktop-amd64-uclibc-hardened/ rc-update add syslog-ng default

cp -f passwd.sh desktop-amd64-uclibc-hardened/tmp/
chroot  desktop-amd64-uclibc-hardened/ /tmp/passwd.sh
rm -f desktop-amd64-uclibc-hardened/tmp/passwd.sh

rm -rf desktop-amd64-uclibc-hardened/home/gentoo
cp -a gentoo desktop-amd64-uclibc-hardened/home/

sed -i 's/^\(DISPLAYMANAGER="\)xdm/\1slim/' desktop-amd64-uclibc-hardened/etc/conf.d/xdm
sed -i 's/^\(login.*\)/# \1/' desktop-amd64-uclibc-hardened/etc/slim.conf
sed -i '/# login_cmd.*Xsession/ a\login_cmd exec /bin/bash -login ~/.xinitrc' desktop-amd64-uclibc-hardened/etc/slim.conf
wget -O desktop-amd64-uclibc-hardened/usr/share/slim/themes/default/background.jpg http://www.gentoo.org/images/backgrounds/gentoo1600x1200.jpg

sed -i '/^SYNC/d' desktop-amd64-uclibc-hardened/etc/portage/make.conf
sed -i '/^GENTOO_MIRRORS/d' desktop-amd64-uclibc-hardened/etc/portage/make.conf
sed -i 's/^MAKEOPTS/#MAKEOPTS/' desktop-amd64-uclibc-hardened/etc/portage/make.conf

rm -rf desktop-amd64-uclibc-hardened/tmp/*
rm -rf desktop-amd64-uclibc-hardened/var/log/*
rm -rf desktop-amd64-uclibc-hardened/var/tmp/*

umount desktop-amd64-uclibc-hardened/sys/
umount desktop-amd64-uclibc-hardened/dev/pts/
umount desktop-amd64-uclibc-hardened/dev/
umount desktop-amd64-uclibc-hardened/proc/
umount desktop-amd64-uclibc-hardened/usr/portage/
