#!/bin/bash

PID=$$

profile=
version_stamp=
subarch=
stage1_seed=
snapshot=
config=/etc/catalyst/catalyst.conf
email_from="catalyst@localhost"
email_to="root@localhost"
verbose=0

usage() {
  msg=$1

  if [ -n "${msg}" ]; then
    echo -e "${msg}\n";
  fi

  cat <<EOH
Usage:
  stage_build [-p|--profile <profile>] [-v|--version-stamp <stamp>]
              [-a|--arch <arch>] [-s|--stage1-seed <seed>] [--verbose]
              [-f|--email-from <from>] [-t|--email-to <to>] [-h|--help]

Options:
  -p|--profile        Sets the portage profile (required)
  -v|--version-stamp  Sets the version stamp (required)
  -a|--arch           Sets the 'subarch' in the spec (required)
  -s|--stage1-seed    Sets the seed for the stage1 (required)
  -S|--snapshot       Sets the snapshot name (if not given defaults to today's
                      date)
  -c|--config         catalyst config to use, defaults to catalyst default
  --verbose           Send output of commands to console as well as log
  -f|--email-from     Sets the 'From' on emails sent from this script (defaults
                      to catalyst@localhost)
  -t|--email-to       Sets the 'To' on emails sent from this script (defaults
                      to root@localhost)
  -h|--help           Show this message and quit

Example:
  stage_build -p default-linux/x86/2006.1 -v 2007.0_pre -a i686 -s default/stage3-i686-2006.1
EOH
}

send_email() {
  subject="[${subarch}] $1"
  body=$2

  echo -e "From: ${email_from}\r\nTo: ${email_to}\r\nSubject: ${subject}\r\n\r\nArch: ${subarch}\r\nProfile: ${profile}\r\nVersion stamp: ${version_stamp}\r\nStage1 seed: ${stage1_seed}\r\nSnapshot: ${snapshot}\r\n\r\n${body}\r\n" | /usr/sbin/sendmail -f ${email_from} ${email_to}
}

run_cmd() {
  cmd=$1
  logfile=$2

  if [ $verbose = 1 ]; then
    ${cmd} 2>&1 | tee ${logfile}
  else
    ${cmd} &> ${logfile}
  fi
}

# Parse args
params=${#}
while [ ${#} -gt 0 ]
do
  a=${1}
  shift
  case "${a}" in
    -h|--help)
      usage
      exit 0
      ;;
    -p|--profile)
      profile=$1
      shift
      ;;
    -v|--version-stamp)
      version_stamp=$1
      shift
      ;;
    -a|--arch)
      subarch=$1
      shift
      ;;
    -f|--email-from)
      email_from=$1
      shift
      ;;
    -t|--email-to)
      email_to=$1
      shift
      ;;
    -s|--stage1-seed)
      stage1_seed=$1
      shift
      ;;
    -S|--snapshot)
      snapshot=$1
      shift
      ;;
    -c|--config)
      config=$1
      shift
      ;;
    --verbose)
      verbose=1
      ;;
    -*)
      echo "You have specified an invalid option: ${a}"
      usage
      exit 1
      ;;
    esac
done

# Make sure all required values were specified
if [ -z "${profile}" ]; then
  usage "You must specify a profile."
  exit 1
fi
if [ -z "${version_stamp}" ]; then
  usage "You must specify a version stamp."
  exit 1
fi
if [ -z "${subarch}" ]; then
  usage "You must specify an arch."
  exit 1
fi
if [ -z "${stage1_seed}" ]; then
  usage "You must specify a stage1 seed."
  exit 1
fi
cd /tmp

if [ -z "${snapshot}" ]; then
  snapshot=`date +%Y%m%d`
  run_cmd "catalyst -c ${config} -s '${snapshot}'" "/tmp/catalyst_build_snapshot.${PID}.log"
  if [ $? != 0 ]; then
    send_email "Catalyst build error - snapshot" "$(</tmp/catalyst_build_snapshot.${PID}.log)"
    exit 1
  fi
fi

for i in 1 2 3; do
  echo -e "subarch: ${subarch}\ntarget: stage${i}\nversion_stamp: ${version_stamp}\nrel_type: default\nprofile: ${profile}\nsnapshot: ${snapshot}" > stage${i}.spec
  if [ ${i} = 1 ]; then
    echo "source_subpath: ${stage1_seed}" >> stage${i}.spec
  else 
    echo "source_subpath: default/stage$(expr ${i} - 1)-${subarch}-${version_stamp}" >> stage${i}.spec
  fi
  run_cmd "catalyst -a -c ${config} -f stage${i}.spec" "/tmp/catalyst_build_stage${i}.${PID}.log"
  if [ $? != 0 ]; then
    send_email "Catalyst build error - stage${i}" "$(tail -n 200 /tmp/catalyst_build_stage${i}.${PID}.log)\r\n\r\nFull build log at /tmp/catalyst_build_stage${i}.${PID}.log"
    exit 1
  fi
done

send_email "Catalyst build success" "Everything finished successfully."
