#!/bin/bash -l

source /etc/profile
env-update
emerge -evq --keep-going --with-bdeps=y world
