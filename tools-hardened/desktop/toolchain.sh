#!/bin/bash -l

kernel_dir="/usr/src/linux-tinhat"

source /etc/profile
env-update
KERNEL_DIR="${kernel_dir}" emerge -1q binutils
source /etc/profile
env-update
KERNEL_DIR="${kernel_dir}" emerge -1q gcc
source /etc/profile
env-update
KERNEL_DIR="${kernel_dir}" emerge -1q glibc
