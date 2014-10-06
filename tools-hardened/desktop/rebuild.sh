#!/bin/bash -l

kernel_dir="/usr/src/linux-tinhat"

source /etc/profile
env-update
KERNEL_DIR="${kernel_dir}" emerge -evq --keep-going --with-bdeps=y world
