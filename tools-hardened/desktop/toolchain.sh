#!/bin/bash -l

source /etc/profile
env-update
emerge -1q binutils
source /etc/profile
env-update
emerge -1q gcc
source /etc/profile
env-update
emerge -1q glibc
