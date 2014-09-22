#!/bin/bash

source /etc/catalyst/catalyst.conf

mydate=`date +%Y%m%d`


undo_grsec() {
  [[ -d /proc/sys/kernel/grsecurity ]] || return
  for i in /proc/sys/kernel/grsecurity/chroot_* ; do
    echo 0 > $i
  done
}


banner() {
cat << EOF | tee -a zzz.log > stage$1-$2-uclibc-$3.log

************************************************************************
*    stage$1-$2-uclibc-$3
************************************************************************"

EOF
}


do_stages() {
  local arch=$1
  local flavor=$2

  for s in 1 2 3; do
    local tgpath="${storedir}/builds/uclibc/${flavor}/${arch}"
    local target="stage${s}-${arch}-uclibc-${flavor}-${mydate}.tar.bz2"
    local tglink="stage${s}-${arch}-uclibc-${flavor}.tar.bz2"

    if [[ ! -f "${tgpath}/${tglink}" ]]; then
       touch stage${s}-${arch}-uclibc-${flavor}.log
       echo "!!! ${tglink} at ${tgpath} doesn't exist" \
         | tee -a zzz.log \
         > stage${s}-${arch}-uclibc-${flavor}.err
       return 1
    fi

    banner ${s} ${arch} ${flavor}
    catalyst -f stage${s}-${arch}-uclibc-${flavor}.conf \
      | tee -a zzz.log \
      > stage${s}-${arch}-uclibc-${flavor}.log \
      2> stage${s}-${arch}-uclibc-${flavor}.err

    if [[ -f "${tgpath}/${target}" ]]; then
      rm -f "${tgpath}/${tglink}"
      ln -s ${target} "${tgpath}/${tglink}"
    else
      echo "!!! ${target} was not generated" \
        | tee -a zzz.log \
        >stage${s}-${arch}-uclibc-${flavor}.err
      return 1
    fi
  done

  return 0
}
