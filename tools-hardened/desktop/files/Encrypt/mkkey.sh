#!/bin/bash
eval 'gpg-agent --daemon --use-standard-socket'
head -c 2925 /dev/random | uuencode -m - | head -n 66 | tail -n 65  | gpg --symmetric -a > key.gpg

