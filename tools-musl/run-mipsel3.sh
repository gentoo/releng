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
    local tarch="${arch%3}"
    local parch="mips/${tarch}"

    cat stage-all.conf.template | \
      sed -e "s:\(^version_stamp.*$\):\1-${mydate}:" \
        -e "s:CSTAGE:${cstage}:g" \
        -e "s:PSTAGE:${pstage}:g" \
        -e "s:SARCH:${arch}:g" \
        -e "s:PARCH:${parch}:g" \
        -e "s:TARCH:${tarch}:g" \
        -e "s:FLAVOR:${flavor}:g" \
        -e "s:MYCATALYST:$(pwd):g" \
        -e "s|^cflags:.*|cflags: -O2 -march=mips3 -mplt -Wa,-mfix-loongson2f-nop -pipe|" \
        -e "s|^cxxflags:.*|cxxflags: -O2 -march=mips3 -mplt -Wa,-mfix-loongson2f-nop -pipe|" \
        >  stage${s}-${arch}-musl-${flavor}.conf
  done

  sed -i "/^chost/d" stage3-${arch}-musl-${flavor}.conf
}



main() {
  >zzz.log

  catalyst -s current | tee -a zzz.log >snapshot.log 2>snapshot.err

  for arch in mipsel3; do
    for flavor in vanilla; do
      prepare_confs ${arch} ${flavor}
    done
  done
  
  for arch in mipsel3; do
    for flavor in vanilla; do
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
