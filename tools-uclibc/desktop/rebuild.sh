#!/bin/bash -l

source /etc/profile
env-update
emerge --keep-going -evq world
