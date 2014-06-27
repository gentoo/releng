#!/bin/bash

source /etc/catalyst/catalyst.conf

mydate=`date +%Y%m%d`

undo_grsec() {
  [[ -d /proc/sys/kernel/grsecurity ]] || return
  for i in /proc/sys/kernel/grsecurity/chroot_* ; do
    echo 0 > $i
  done
}

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

banner() {
cat << EOF | tee -a zzz.log > stage$1-$2-musl-$3.log

************************************************************************
*    stage$1-$2-musl-$3
************************************************************************"

EOF
}


do_stages() {
  local arch=$1
  local flavor=$2

  for s in 1 2 3; do
    local tgpath="${storedir}/builds/musl/${flavor}/${arch}"
    local target="stage${s}-${arch}-musl-${flavor}-${mydate}.tar.bz2"
    local tglink="stage${s}-${arch}-musl-${flavor}.tar.bz2"

    if [[ ! -f "${tgpath}/${tglink}" ]]; then
       touch stage${s}-${arch}-musl-${flavor}.log
       echo "!!! ${tglink} at ${tgpath} doesn't exist" \
         | tee -a zzz.log \
         > stage${s}-${arch}-musl-${flavor}.err
       return 1
    fi

    banner ${s} ${arch} ${flavor}
    catalyst -f stage${s}-${arch}-musl-${flavor}.conf \
      | tee -a zzz.log \
      > stage${s}-${arch}-musl-${flavor}.log \
      2> stage${s}-${arch}-musl-${flavor}.err

    if [[ -f "${tgpath}/${target}" ]]; then
      rm -f "${tgpath}/${tglink}"
      ln -s ${target} "${tgpath}/${tglink}"
    else
      echo "!!! ${target} was not generated" \
        | tee -a zzz.log \
        >stage${s}-${arch}-musl-${flavor}.err
      return 1
    fi
  done

  return 0
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
         echo "FAILURE at ${arch} ${flavor}" | tee zzz.log
         return 1
      fi
    done
  done
}

main $1 &
