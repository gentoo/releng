#!/bin/bash -l

source /etc/profile
env-update
#hacky - for some reason cairo fails to rebuild
#unless binutils is rebuilt first.
emerge -q binutils
emerge -uvNDq world
