#!/bin/bash

# Set timezone
echo 'UTC' > /etc/timezone

# Set locale
echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen
echo 'en_US ISO-8859-1' >> /etc/locale.gen
locale-gen -q
eselect locale set en_US.utf8

# Some rootfs stuff
grep -v rootfs /proc/mounts > /etc/mtab

# This is set in rackspaces prep, might help us
echo 'net.ipv4.conf.eth0.arp_notify = 1' >> /etc/sysctl.conf
echo 'vm.swappiness = 0' >> /etc/sysctl.conf

# Let's configure our grub
# Access on both regular tty and serial console
mkdir /boot/grub
cat >>/etc/default/grub <<EOF
GRUB_TERMINAL='serial console'
GRUB_CMDLINE_LINUX="console=tty0 console=ttyS0,115200n8"
GRUB_SERIAL_COMMAND="serial --speed=115200 --unit=0 --word=8 --parity=no --stop=1"
EOF
grub-mkconfig -o /boot/grub/grub.cfg
sed -r -i 's/loop[0-9]+p1/LABEL\=cloudimg-rootfs/g' /boot/grub/grub.cfg
sed -i 's/root=.*\ ro/root=LABEL\=cloudimg-rootfs\ ro/' /boot/grub/grub.cfg

# And the fstab
echo 'LABEL=cloudimg-rootfs / ext4 defaults 0 0' > /etc/fstab

# allow the console log
sed -i 's/#s0/s0/g' /etc/inittab

# let ipv6 use normal slaac
sed -i 's/slaac/#slaac/g' /etc/dhcpcd.conf
# don't let dhcpcd set domain name or hostname
sed -i 's/domain_name\,\ domain_search\,\ host_name/domain_search/g' /etc/dhcpcd.conf

# need to do this here because it clobbers an openrc owned file
cat > /etc/conf.d/hostname << "EOL"
# Set to the hostname of this machine
if [ -f /etc/hostname ];then
  hostname=$(cat /etc/hostname 2> /dev/null | cut -d"." -f1 2> /dev/null)
else
  hostname="localhost"
fi
EOL
chmod 0644 /etc/conf.d/hostname
chown root:root /etc/conf.d/hostname

# set a nice default for /etc/resolv.conf
cat > /etc/resolv.conf << EOL
nameserver 8.8.8.8
nameserver 2001:4860:4860::8888
EOL

# let's upgrade (security fixes and otherwise)
USE="-build" emerge -uDNv --with-bdeps=y --jobs=2 @world
USE="-build" emerge --verbose=n --depclean
USE="-build" emerge -v --usepkg=n @preserved-rebuild
etc-update --automode -5

# Clean up portage
emerge --verbose=n --depclean
if [[ -a /usr/bin/eix ]]; then
  eix-update
fi
emaint all -f
eselect news read all
eclean-dist --destructive
sed -i '/^USE=\"\${USE}\ \ build\"$/d' /etc/portage/make.conf
echo 'PORTAGE_GPG_DIR="/var/lib/gentoo/gkeys/keyrings/gentoo/release"' >> /etc/portage/make.conf

# clean up system
passwd -d root
passwd -l root
for i in $(find /var/log -type f); do truncate -s 0 $i; done
# remove foreign manpages
find /usr/share/man/ -mindepth 1  -maxdepth 1 -path "/usr/share/man/man*" -prune -o -exec rm -rf {} \;

# fine if this fails, aka non-hardened
if [[ -x /usr/sbin/migrate-pax ]]; then
  echo 'migraging pax'
  /usr/sbin/migrate-pax -m
fi
