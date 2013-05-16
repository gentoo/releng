#!/bin/bash -l

source /etc/profile
env-update
emerge -1q gcc
emerge -1q uclibc
emerge -1q binutils
