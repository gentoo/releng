#!/bin/bash

source /etc/catalyst/catalyst.conf

mydate=`date +%Y%m%d`

prepare_confs() {
  local arch=$1
  local flavor=$2

  for s in 1 2 3; do
    cat stage${s}-${arch}_hardfp-${flavor}.conf.template | \
      sed -e "s/\(^version_stamp.*$\)/\1-${mydate}/" >  stage${s}-${arch}_hardfp-${flavor}.conf
  done
}

banner() {
cat << EOF | tee -a zzz.log > stage$1-$2_hardfp-$3.log

************************************************************************
*    stage$1-$2_hardfp-$3
************************************************************************"

EOF
}


do_stages() {
  local arch=$1
  local flavor=$2

  for s in 1 2 3; do
    local tgpath="${storedir}/builds/${flavor}/${arch}"
    local target="stage${s}-${arch}_hardfp-${flavor}-${mydate}.tar.bz2"
    local tglink="stage${s}-${arch}_hardfp-${flavor}.tar.bz2"

    if [[ ! -f "${tgpath}/${tglink}" ]]; then
       touch stage${s}-${arch}_hardfp-${flavor}.log
       echo "!!! ${target} at ${tgpath} doesn't exit" \
         | tee -a zzz.log \
         > stage${s}-${arch}_hardfp-${flavor}.err
       return 1
    fi

    banner ${s} ${arch} ${flavor}
    catalyst -f stage${s}-${arch}_hardfp-${flavor}.conf \
      | tee -a zzz.log \
      > stage${s}-${arch}_hardfp-${flavor}.log \
      2> stage${s}-${arch}_hardfp-${flavor}.err

    if [[ -f "${tgpath}/${target}" ]]; then
      rm -f "${tgpath}/${tglink}"
      ln -s ${target} "${tgpath}/${tglink}"
    else
      echo "!!! ${target} was not generated" \
        | tee -a zzz.log \
        >stage${s}-${arch}_hardfp-${flavor}.err
      return 1
    fi
  done

  return 0
}


#
# approximate timings:
#
# catalyst -s current	3 minutes
# catalyst -f stage1  130 minutes
#

main() {
  >zzz.log

  catalyst -s current | tee -a zzz.log >snapshot.log 2>snapshot.err

  for arch in armv7a; do
    for flavor in hardened; do
      prepare_confs ${arch} ${flavor}
    done
  done
  
  for arch in armv7a; do
    for flavor in hardened; do
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
