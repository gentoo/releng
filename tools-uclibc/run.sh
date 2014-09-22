#!/bin/bash

source common.sh

prepare_confs() {
  local arch=$1
  local flavor=$2

  for s in 1 2 3; do

    local cstage=stage${s}
    local p=$(( s - 1 ))
    [[ $p == 0 ]] && p=3
    local pstage=stage${p}

    local parch="${arch}"
    [[ "${arch}" == "i686" ]] && parch="x86"

    local tarch="${arch}"
    [[ "${arch}" == "amd64" ]] && tarch="x86_64"

    local profile=${flavor}
    [[ "${flavor}" == "vanilla" ]] && profile="default"

    cat stage-all.conf.template | \
      sed -e "s:\(^version_stamp.*$\):\1-${mydate}:" \
        -e "s:CSTAGE:${cstage}:g" \
        -e "s:PSTAGE:${pstage}:g" \
        -e "s:SARCH:${arch}:g" \
        -e "s:PARCH:${parch}:g" \
        -e "s:TARCH:${tarch}:g" \
        -e "s:FLAVOR:${flavor}:g" \
        -e "s:PROFILE:${profile}:g" \
        -e "s:MYCATALYST:$(pwd):g" \
        >  stage${s}-${arch}-uclibc-${flavor}.conf
  done

  sed -i "/^chost/d" stage3-${arch}-uclibc-${flavor}.conf
}


main() {
  >zzz.log

  undo_grsec

  catalyst -s current | tee -a zzz.log >snapshot.log 2>snapshot.err

  for arch in amd64 i686; do
    for flavor in hardened vanilla; do
      prepare_confs ${arch} ${flavor}
    done
  done

  # The parallelization `( do_stages ... ) &` doesn't work here
  # if catalyst is using snapcache, bug #519656
  for arch in amd64 i686; do
    for flavor in hardened vanilla; do
      (
        do_stages ${arch} ${flavor}
        [[ $? == 1 ]] && echo "FAILURE at ${arch} ${flavor} " | tee zzz.log
      ) &
    done
  done
}

main $1 &
