#!/bin/bash

#
# Usage: ./run-armv7a.sh <mode>
# where
# <mode> = "", it will actually do the runs
# <mode> = "test", it will just pretend
#

source /etc/catalyst/catalyst.conf

mydate=`date +%Y%m%d`

prepare_confs() {
  local arch=$1
  local flavor=$2

  for s in 1 2 3; do
    cat stage${s}-${arch}-uclibc-${flavor}.conf.template | \
      sed -e "s/\(^version_stamp.*$\)/\1-${mydate}/" >  stage${s}-${arch}-uclibc-${flavor}.conf
  done
}

banner() {
	echo
	echo "************************************************************************"
	echo "*    $1"
	echo "************************************************************************"
	echo
}


do_stages() {
  local arch=$1
  local flavor=$2
  local pretend=$3

  for s in 1 2 3; do
    local tgpath="${storedir}/builds/${flavor}/${arch}"
    local target="stage${s}-${arch}-uclibc-${flavor}-${mydate}.tar.bz2"
    local tglink="stage${s}-${arch}-uclibc-${flavor}.tar.bz2"

    if [[ ! -f "${tgpath}/${tglink}" ]]; then
       touch stage${s}-${arch}-uclibc-${flavor}.log
       echo "!!! ${target} at ${tgpath} doesn't exit" \
         | tee -a zzz.log \
         > stage${s}-${arch}-uclibc-${flavor}.err
       return 1
    fi

    if [[ "x${pretend}" != "xtest" ]]; then
      banner "stage${s}-${arch}-uclibc-${flavor}"
      catalyst -f stage${s}-${arch}-uclibc-${flavor}.conf \
        | tee -a zzz.log \
        > stage${s}-${arch}-uclibc-${flavor}.log \
        2> stage${s}-${arch}-uclibc-${flavor}.err
    else
      touch stage${s}-${arch}-uclibc-${flavor}.log
      touch stage${s}-${arch}-uclibc-${flavor}.err
      touch "${tgpath}/${target}"
      echo "PRETEND: catalyst -f stage${s}-${arch}-uclibc-${flavor}.conf \ "
      echo "PRETEND:   > stage${s}-${arch}-uclibc-${flavor}.log \ "
      echo "PRETEND:   2> stage${s}-${arch}-uclibc-${flavor}.err"
    fi

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


#
# approximate timings:
#
# catalyst -s current	3 minutes
# catalyst -f stage1  130 minutes
#

main() {
  local pretend=$1

  >zzz.log

  if [[ "x${pretend}" != "xtest" ]]; then
     catalyst -s current | tee -a zzz.log >snapshot.log 2>snapshot.err
  else
     >snapshot.log
     >snapshot.err
     echo "PRETEND: catalyst -s current > snapshot.log 2> snapshot.err"
  fi

  for arch in armv7a; do
    for flavor in hardened vanilla; do
      prepare_confs ${arch} ${flavor}
    done
  done
  
  for arch in armv7a; do
    for flavor in hardened vanilla; do
      do_stages ${arch} ${flavor} ${pretend}
      ret=$?
      if [[ $? == 1 ]]; then
         echo "FAILURE at ${arch} ${flavor} ${pretend} " | tee zzz.log
         return 1
      fi
    done
  done

  if [[ "x${pretend}" == "xtest" ]]; then
    tree /var/tmp/catalyst/builds
    echo
    echo "!!! Run fixup.sh to clean up!"
    echo
  fi
}

main $1 &
