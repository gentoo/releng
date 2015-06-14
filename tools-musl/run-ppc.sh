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

    local tarch="${arch}"
    [[ "${arch}" == "ppc" ]] && tarch="powerpc"

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

    portage_confdir=$(grep portage_confdir stage${s}-${arch}-musl-${flavor}.conf \
      | sed -e 's/^.*:[ \t]*//')
    [[ ! -e ${portage_confdir} ]] && sed -i -e '/^portage_confdir/d' \
      stage${s}-${arch}-musl-${flavor}.conf
  done

  sed -i "/^chost/d" stage3-${arch}-musl-${flavor}.conf
}


main() {
  >zzz.log

  catalyst -s current | tee -a zzz.log >snapshot.log 2>snapshot.err

  for arch in ppc; do
    for flavor in vanilla; do
      prepare_confs ${arch} ${flavor}
    done
  done

  # No parallelization
  for arch in ppc; do
    for flavor in vanilla; do
      do_stages ${arch} ${flavor}
      [[ $? == 1 ]] && echo "FAILURE at ${arch} ${flavor} " | tee zzz.log
    done
  done
}

main $1 &
