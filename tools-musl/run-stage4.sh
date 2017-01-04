#!/bin/bash

set -eu

source /etc/catalyst/catalyst.conf

MUSL_DIR="$( cd "$( dirname ${BASH_SOURCE[0]} )" && pwd )"
MY_DATE="$(date +%Y%m%d)"

# munge specfile for this run
cp "${MUSL_DIR}"/stage4-hardened-amd64.spec "${MUSL_DIR}"/stage4-hardened-amd64-configured.spec
sed -i "s|@REPO_DIR@|${MUSL_DIR}|g" "${MUSL_DIR}"/stage4-hardened-amd64-configured.spec
sed -i "s|MY_DATE|${MY_DATE}|g" "${MUSL_DIR}"/stage4-hardened-amd64-configured.spec

# catalyst stuff
catalyst -f "${MUSL_DIR}"/stage4-hardened-amd64-configured.spec | tee -a "${MUSL_DIR}"/zzz.log

# update link, rm -f returns 0 if file isn't there yet
rm -f "${storedir}/builds/musl/hardened/amd64/stage4-amd64-musl-hardened.tar.bz2"
ln -s "${storedir}/builds/musl/hardened/amd64/stage4-amd64-musl-hardened-${MY_DATE}.tar.bz2" "${storedir}/builds/musl/hardened/amd64/stage4-amd64-musl-hardened.tar.bz2"

# remove old specfile
rm "${MUSL_DIR}"/stage4-hardened-amd64-configured.spec
