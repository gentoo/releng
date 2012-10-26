#!/bin/bash

# This just fixes up the symbolic links
# to the latest stage{1,2,3} tarballs

mydate=$1
mypwd=/var/tmp/catalyst/builds

find ${mypwd} -type f -size 0 -exec rm {} +
find -L  ${mypwd} -type l -exec rm {} +

for arch in amd64 i686; do
  for flavor in hardened vanilla; do
    for s in 1 2 3; do
      file=stage${s}-${arch}-uclibc-${flavor}-${mydate}.tar.bz2
      link=stage${s}-${arch}-uclibc-${flavor}.tar.bz2
      cd "${mypwd}/${flavor}/${arch}"
      if [[ -f ${file} ]]; then
        ln -sf ${file} ${link}
      else
        echo "!!! ${file} doesn't exist!"
        echo "!!! make sure \${mydate} is right!"
        exit 1
      fi
    done
  done
done

tree ${mypwd}
