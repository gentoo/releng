#!/bin/bash

CATDIR="/release/buildroot/alt-dev/builds/musl"
SERVER="amd64@dipper:~/musl"
LIST=$(find $CATDIR -maxdepth 3 -iname 'stage3*amd64*' -type l)
#COMMAND="rsync -e ssh -i /root/.ssh/id_rsa -o UserKnownHostsFile=/dev/null -o VerifyHostKeyDNS=yes -o StrictHostKeyChecking=no -a --omit-dir-times --delay-updates "
COMMAND="rsync"
for f in $LIST; do
	$COMMAND $(realpath $f)             $SERVER
	$COMMAND $(realpath $f).CONTENTS.gz $SERVER
	$COMMAND $(realpath $f).DIGESTS     $SERVER
done

#SERVER="/release/weekly/builds/x86/musl"
SERVER="x86@dipper:~/musl"
LIST=$(find $CATDIR -maxdepth 3 -iname 'stage3*i686*' -type l)
for f in $LIST; do
	$COMMAND $(realpath $f)             $SERVER
	$COMMAND $(realpath $f).CONTENTS.gz $SERVER
	$COMMAND $(realpath $f).DIGESTS     $SERVER
done
