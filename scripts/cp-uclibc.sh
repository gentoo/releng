#!/bin/bash

CATDIR="/release/buildroot/alt-dev/builds/uclibc"
SERVER="amd64@dipper:~/uclibc"
LIST=$(find $CATDIR -maxdepth 3 -iname 'stage3*amd64*' -type l)
COMMAND="rsync"
for f in $LIST; do
	$COMMAND $(realpath $f)             $SERVER
	$COMMAND $(realpath $f).CONTENTS.gz $SERVER
	$COMMAND $(realpath $f).DIGESTS     $SERVER
done

SERVER="x86@dipper:~/uclibc"
LIST=$(find $CATDIR -maxdepth 3 -iname 'stage3*i686*' -type l)
for f in $LIST; do
	$COMMAND $(realpath $f)             $SERVER
	$COMMAND $(realpath $f).CONTENTS.gz $SERVER
	$COMMAND $(realpath $f).DIGESTS     $SERVER
done
