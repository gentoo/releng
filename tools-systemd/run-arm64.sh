#!/bin/bash

source common.sh

prepare_confs() {
  local arch=$1

  for s in 1 2 3; do

    local cstage=stage${s}
    local p=$(( s - 1 ))
    [[ $p == 0 ]] && p=3
    local pstage=stage${p}
    local repo_dir="$( dirname $(pwd) )"
    local template="stage-all.conf.template"
    local parch="${arch}"

    cat ${template} | \
      sed -e "s:\(^version_stamp.*$\):\1-${mydate}:" \
        -e "s:CSTAGE:${cstage}:g" \
        -e "s:PSTAGE:${pstage}:g" \
        -e "s:SARCH:${arch}:g" \
        -e "s:PARCH:${parch}:g" \
        -e "s:@REPO_DIR@:${repo_dir}:g" \
        -e "s:MYCATALYST:$(pwd):g" \
        >  stage${s}-${arch}-systemd.conf
  done
}


main() {
  >zzz.log

  catalyst -s current | tee -a zzz.log >snapshot.log 2>snapshot.err

  for arch in arm64; do
    prepare_confs ${arch}
  done

  for arch in arm64; do
    do_stages ${arch}
    [[ $? == 1 ]] && echo "FAILURE at ${arch}" | tee zzz.log
  done
}

main $1 &
