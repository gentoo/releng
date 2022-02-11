#!/bin/bash

echo Running LiveGUI stage2 fsscript ...

source /etc/profile
env-update
source /tmp/envscript

# No we don't want to run xdm...
sed -e '/^DISPLAYMANAGER=/s/.*/DISPLAYMANAGER="sddm"/' -i /etc/conf.d/display-manager
