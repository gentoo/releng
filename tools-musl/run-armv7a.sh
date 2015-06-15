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
    local tarch="${arch%_hardfp}"
    local parch="arm/${tarch}"
    local float

    [[ "${arch}" == "${tarch}" ]] \
      && float="softfp" \
      || float="hardfloat"

    cat stage-all.conf.template | \
      sed -e "s:\(^version_stamp.*$\):\1-${mydate}:" \
        -e "s:CSTAGE:${cstage}:g" \
        -e "s:PSTAGE:${pstage}:g" \
        -e "s:SARCH:${arch}:g" \
        -e "s:PARCH:${parch}:g" \
        -e "s:TARCH:${tarch}:g" \
        -e "s:gentoo-linux-musl:${float}-linux-musleabi:" \
        -e "s:FLAVOR:${flavor}:g" \
        -e "s:MYCATALYST:$(pwd):g" \
        >  stage${s}-${arch}-musl-${flavor}.conf

    sed -i "/^portage_confdir/s:_hardfp::" \
      stage${s}-${arch}-musl-${flavor}.conf

    echo "cflags: -O2 -pipe -march=armv7-a -mfpu=vfpv3-d16 -mfloat-abi=hard" >> \
      stage${s}-${arch}-musl-${flavor}.conf

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

  for arch in armv7a_hardfp; do
    for flavor in hardened vanilla; do
      prepare_confs ${arch} ${flavor}
    done
  done

  # No parallelization for arm.  Its too hard on the cpu!
  for arch in armv7a_hardfp; do
    for flavor in hardened vanilla; do
      do_stages ${arch} ${flavor}
      [[ $? == 1 ]] && echo "FAILURE at ${arch} ${flavor} " | tee zzz.log
    done
  done
}

main $1 &
