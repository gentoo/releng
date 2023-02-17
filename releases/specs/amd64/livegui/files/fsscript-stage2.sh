#!/bin/bash

echo Running LiveGUI stage2 fsscript ...

source /etc/profile
env-update
source /tmp/envscript

# No we don't want to run xdm...
sed -e '/^DISPLAYMANAGER=/s/.*/DISPLAYMANAGER="sddm"/' -i /etc/conf.d/display-manager

# Don't let NM change hostname (this breaks xauth)
echo "[main]
plugins=keyfile 
hostname-mode=none" > /etc/NetworkManager/NetworkManager.conf

# Autologin via sddm to plasma
echo "[Autologin]
User=gentoo
Session=plasma.desktop
Relogin=true" > /etc/sddm.conf

# Set up gentoo user
pushd /home/gentoo
mkdir -pv .config Desktop

# Disable screen lock
echo "[Daemon]
Autolock=false" > .config/kscreenlockerrc

# Firefox as default browser
echo \
"[Added Associations]
inode/directory=org.kde.dolphin.desktop;
x-scheme-handler/http=firefox-esr.desktop;chromium-browser-chromium.desktop;
x-scheme-handler/https=firefox-esr.desktop;chromium-browser-chromium.desktop;

[Default Applications]
inode/directory=org.kde.dolphin.desktop;
x-scheme-handler/http=firefox-esr.desktop;
x-scheme-handler/https=firefox-esr.desktop;" \
 > .config/mimeapps.list

# Customize taskbar pinned apps
wget "https://dev.gentoo.org/~bkohler/livegui/plasma-org.kde.plasma.desktop-appletsrc" -O \
	.config/plasma-org.kde.plasma.desktop-appletsrc

# User face image
wget "https://dev.gentoo.org/~bkohler/livegui/face.icon.png" -O .face.icon

# Desktop icon setups
#DESKTOP_APPS=( org.kde.konsole firefox org.kde.dolphin )
#for i in "${APPS[@]}"; do
#	ln -sv /usr/share/applications/${i}.desktop Desktop/
#done

# Autostart keyboard layout module
mkdir -p .config/autostart
echo "[Desktop Entry]
Version=1.0
Name=Keyboard settings
Icon=preferences-system
Type=Application
SingleMainWindow=true
Exec=systemsettings5 kcm_keyboard
Terminal=false
" > .config/autostart/systemsettings-keyboard.desktop

popd
# Clean up perms
chown -R gentoo:users /home/gentoo

# Let some tools run as root
echo 'polkit.addRule(function(action, subject) {
    if (action.id == "org.gnome.gparted") {
        return polkit.Result.YES;
    }
});

polkit.addRule(function(action, subject) {
    if (action.id == "org.kde.kpmcore.externalcommand.init") {
        return polkit.Result.YES;
    }
});

polkit.addRule(function(action, subject) {
    if (action.id == "org.freedesktop.udisks2.filesystem-mount-system") {
        return polkit.Result.YES;
    }
});' > /etc/polkit-1/rules.d/livegui-root-tools.rules
