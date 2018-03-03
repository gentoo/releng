#!/bin/bash

source common.sh

prepare_confs() {
  local arch=$1

  for s in 1 2 3 4; do
    # don't make i686 stage4
    [[ $arch == i686 ]] && [[ $s == 4 ]] && continue

    local cstage=stage${s}
    local p=$(( s - 1 ))
    [[ $p == 0 ]] && p=3
    local pstage=stage${p}
    local repo_dir="$( dirname $(pwd) )"
    local template="stage-all.conf.template"
    # set the template file if stage4
    [[ $s == 4 ]] && template=stage4-amd64.spec

    local parch="${arch}"
    [[ "${arch}" == "i686" ]] && parch="x86"

    cat ${template} | \
      sed -e "s:\(^version_stamp.*$\):\1-${mydate}:" \
        -e "s:CSTAGE:${cstage}:g" \
        -e "s:PSTAGE:${pstage}:g" \
        -e "s:SARCH:${arch}:g" \
        -e "s:PARCH:${parch}:g" \
        -e "s:@REPO_DIR@:${repo_dir}:g" \
        >  stage${s}-${arch}-systemd.conf
  done
}


main() {
  >zzz.log

  undo_grsec

  catalyst -s current | tee -a zzz.log >snapshot.log 2>snapshot.err

  for arch in amd64 i686; do
    prepare_confs ${arch}
  done

  # The parallelization `( do_stages ... ) &` doesn't work here
  # if catalyst is using snapcache, bug #519656
  for arch in amd64 i686; do
    do_stages ${arch}
    [[ $? == 1 ]] && echo "FAILURE at ${arch}" | tee zzz.log
  done

  catalyst -f stage4-amd64-systemd.conf
}

main $1 &
