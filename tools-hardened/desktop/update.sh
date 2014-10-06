#!/bin/bash -l

kernel_dir="/usr/src/linux-tinhat"
#Right now we're commenting out the cairo
#rebuild to see if it works in glibc.
#hacky - for some reason cairo fails to rebuild
#unless binutils is rebuilt first.  It fails to
#find libibirty.
source /etc/profile
env-update
#emerge -q binutils
#source /etc/profile
#env-update
#emerge -1q x11-libs/cairo

KERNEL_DIR="${kernel_dir}" emerge -uvNDq --keep-going --with-bdeps=y world
