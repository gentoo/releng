#!/bin/bash

echo Running LiveGUI stage2 fsscript ...

source /etc/profile
env-update
source /tmp/envscript

# No we don't want to run xdm...
sed -e '/^DISPLAYMANAGER=/s/.*/DISPLAYMANAGER="sddm"/' -i /etc/conf.d/display-manager

# Autologin via sddm to plasma
echo "[Autologin]
User=gentoo
Session=plasma.desktop
Relogin=yes" > /etc/sddm.conf

# set up gentoo user
echo "** useradd gentoo **"
useradd -G users,wheel,audio,plugdev,games,cdrom -g users -c "Gentoo LiveGUI user" -m gentoo
mkdir /home/gentoo/.config

# Disable screen lock
echo "[Daemon]
Autolock=false" > /home/gentoo/.config/kscreenlockerrc

# Firefox as default browser
echo "[Default Applications]
text/html=firefox.desktop" > /home/gentoo/.config/mimeapps.list

# Clean up perms
chown -R gentoo:users /home/gentoo
