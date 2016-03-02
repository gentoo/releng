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
cat << EOF | tee -a zzz.log > stage$1-$2-systemd.log

************************************************************************
*    stage$1-$2-systemd
************************************************************************"

EOF
}


do_stages() {
  local arch=$1

  for s in 1 2 3; do
    local tgpath="${storedir}/builds/systemd/${arch}"
    local target="stage${s}-${arch}-systemd-${mydate}.tar.bz2"
    local tglink="stage${s}-${arch}-systemd.tar.bz2"

    if [[ ! -f "${tgpath}/${tglink}" ]]; then
       touch stage${s}-${arch}-systemd.log
       echo "!!! ${tglink} at ${tgpath} doesn't exist" \
         | tee -a zzz.log \
         > stage${s}-${arch}-systemd.err
       return 1
    fi

    banner ${s} ${arch}
    catalyst -f stage${s}-${arch}-systemd.conf \
      | tee -a zzz.log \
      > stage${s}-${arch}-systemd.log \
      2> stage${s}-${arch}-systemd.err

    if [[ -f "${tgpath}/${target}" ]]; then
      rm -f "${tgpath}/${tglink}"
      ln -s ${target} "${tgpath}/${tglink}"
    else
      echo "!!! ${target} was not generated" \
        | tee -a zzz.log \
        >stage${s}-${arch}-systemd.err
      return 1
    fi
  done

  return 0
}
