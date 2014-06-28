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

    cat stage-all.conf.template | \
      sed -e "s:\(^version_stamp.*$\):\1-${mydate}:" \
        -e "s:CSTAGE:${cstage}:g" \
        -e "s:PSTAGE:${pstage}:g" \
        -e "s:SARCH:${arch}:g" \
        -e "s:PARCH:${parch}:g" \
        -e "s:TARCH:${tarch}:g" \
        -e "s:FLAVOR:${flavor}:g" \
        -e "s:MYCATALYST:$(pwd):g" \
        >  stage${s}-${arch}-musl-${flavor}.conf
  done

  sed -i "/^chost/d" stage3-${arch}-musl-${flavor}.conf
}


main() {
  >zzz.log

  undo_grsec

  catalyst -s current | tee -a zzz.log >snapshot.log 2>snapshot.err

  for arch in amd64 i686; do
    for flavor in vanilla hardened; do
      prepare_confs ${arch} ${flavor}
    done
  done
  
  for arch in amd64 i686; do
    for flavor in vanilla hardened; do
      do_stages ${arch} ${flavor}
      ret=$?
      if [[ $? == 1 ]]; then
         echo "FAILURE at ${arch} ${flavor} " | tee zzz.log
         return 1
      fi
    done
  done
}

main $1 &
