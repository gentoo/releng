#!/bin/bash

# Where artifacts are uploaded by builders.
INCOMING_BASE="/release/weekly/builds"
# Where artifacts are moved to so they can be uploaded to mirrors.
OUTGOING_BASE="/release/distfiles/weekly"
# Scratch space used when moving files from incoming to outgoing.
TMPDIR_BASE="/release/distfiles/tmp/buildsync/partial"

ARCHES=(
	alpha
	amd64
	arm
	hppa
	ia64
	#mips
	ppc
	s390
	sh
	sparc
	x86
)
RSYNC_OPTS=(
	-aO
	--delay-updates
)
# Command line for `find` to figure out what files are release artifacts.
EXTENSIONS=(
	'('
	-name '*.tar.xz' -o
	-name '*.tar.bz2' -o
	-name '*.tar.gz' -o
	-name '*.tar' -o
	-name '*.sfs'
	')'
)

OUT_STAGE3="latest-stage3.txt"
OUT_ISO="latest-iso.txt"

# Nothing to edit beyond this point

DEBUGP=
VERBOSEP=

usage() {
	cat <<EOF
Usage: $0 [options]

Move releases from the incoming upload directory to the outgoing release
directory so they can be pushed out to mirrors.
Also update the "latest" links/files so people can easily find the current
version for any particular arch/release.

Options:
  -v, --verbose    Run in verbose mode
  -d, --debug      Run in debug mode
EOF
	exit ${1:-1}
}

# Copy artifacts for an arch to the outgoing directory.
copy_arch_to_outgoing() {
	local ARCH=$1 indir=$2 outdir=$3 tmpdir=$4
	local i t rc

	if [[ ! -d ${indir} ]]; then
		# Nothing to do for this arch.
		return
	fi

	# Copying
	for i in $(find ${indir} -type f | egrep -- '-20[0123][0-9]{5}(([0-9]{6})|(T[0-9]{6}Z))?' | sed -e 's:^.*-\(20[^.]\+\).*$:\1:' | sort -ur); do
		#echo "Doing $i"
		t="${outdir}/${i}"
		mkdir -p ${t} 2>/dev/null
		rsync "${RSYNC_OPTS[@]}" --temp-dir=${tmpdir} --partial-dir=${tmpdir} ${indir}/ --filter "S *${i}*" --filter 'S **/' --filter 'H *' ${t}
		rc=$?
		if [ $rc -eq 0 ]; then
			find ${indir} -type f -name "*${i}*" -print0 | xargs -0 --no-run-if-empty $DEBUGP rm $VERBOSEP -f
		else
			echo "Not deleting ${indir}/*${i}*, rsync failed!" 1>&2
			fail=1
		fi
	done
	find "${outdir}" \
		-depth -mindepth 1 -type d \
		-exec rmdir --ignore-fail-on-non-empty {} +
}

process_arch() {
	local ARCH=$1

	fail=0

	indir="${INCOMING_BASE}/${ARCH}"
	outdir="${OUTGOING_BASE}/${ARCH}"
	tmpdir="${TMPDIR_BASE}/${ARCH}"

	mkdir -p ${tmpdir} 2>/dev/null

	# Sync incoming->outgoing first.
	copy_arch_to_outgoing "${ARCH}" "${indir}" "${outdir}" "${tmpdir}"

	# ================================================================
	# Build data for revealing latest:
	# *.iso
	# stage3*bz2
	cd "${outdir}"
	# %T@

	iso_list="$(find 20* -name '*.iso' -printf '%h %f %h/%f\n' 2>/dev/null |grep -v hardened | sort -n)"
	stage3_list=$(find 20* -name "stage3*" -a "${EXTENSIONS[@]}" -printf '%h %f %h/%f\n' 2>/dev/null| grep -v hardened | sort -n)
	latest_iso_date="$(echo -e "${iso_list}" |awk '{print $1}' |cut -d/ -f1 | tail -n1)"
	latest_stage3_date="$(echo -e "${stage3_list}" |awk '{print $1}' |cut -d/ -f1 | tail -n1)"
	header="$(echo -e "# Latest as of $(date -uR)\n# ts=$(date -u +%s)")"

	# Do not remove this
	[ -z "${latest_iso_date}" ] && latest_iso_date="NONE-FOUND"
	[ -z "${latest_stage3_date}" ] && latest_stage3_date="NONE-FOUND"

	if [ -n "${iso_list}" ]; then
		echo -e "${header}" >"${OUT_ISO}"
		# Some arches produce more than one type of iso.
		# Only apply the current-iso link logic to them.
		# TODO: Should make this dynamic based on the iso list.
		case ${ARCH} in
		amd64|x86)
			rm -f current-iso
			;;
		*)
			echo -e "${iso_list}" |awk '{print $3}' | grep "$latest_iso_date" >>${OUT_ISO}
			ln -sfT "$latest_iso_date" current-iso
			;;
		esac
	fi
	if [ -n "${stage3_list}" ]; then
		echo -e "${header}" >"${OUT_STAGE3}"

		# In the new variant preserve code there is a better way to do this
		#echo -e "${stage3_list}" |awk '{print $3}' |grep "$latest_stage3_date" >>${OUT_STAGE3}

		# The "latest stage3" concept works for only a few arches -- ones that
		# do not have more than one stage3 target per arch (i.e. multilib, etc...).
		case ${ARCH} in
		amd64|arm|hppa|ppc|s390|sh|x86)
			rm -f current-stage3
			;;
		*)
			ln -sfT "$latest_stage3_date" current-stage3
			;;
		esac
	fi

	# New variant preserve code
	find_variants=( '(' -iname '*.iso' -o -name 'netboot-*' -o "${EXTENSIONS[@]}" ')' )
	variants=$(find 20* "${find_variants[@]}" -printf '%f\n' 2>/dev/null | sed -e 's,-20[012][0-9]\{5\}.*,,g' -r | sort -u)
	echo -n '' >"${tmpdir}"/.keep.${ARCH}.txt
	for v in $variants ; do
		variant_path=$(find 20* -iname "${v}-20*" "${find_variants[@]}" -print 2>/dev/null | sed -e "s,.*/$a/autobuilds/,,g" | sort -k1,1 -t/ | tail -n1 )
		if [ -z "${variant_path}" -o ! -e "${variant_path}" ]; then
			echo "$ARCH: Variant ${v} is missing" 1>&2
			continue
		fi
		size=$(stat --format=%s ${variant_path})
		f="latest-${v}.txt"
		echo -e "${header}" >"${f}"
		echo -e "${variant_path} ${size}" >>${f}
		[[ ${variant_path} =~ tar.*$ ]] && echo -e "${variant_path} ${size}" >>${OUT_STAGE3}
		[[ ${variant_path} =~ iso$ ]] && echo -e "${variant_path} ${size}" >>${OUT_ISO}
		rm -f "current-$v"
		ln -sf "${variant_path%/*}" "current-$v"
		echo "${variant_path}" | sed -e 's,/.*,,g' -e 's,^,/,g' -e 's,$,$,g' >>"${tmpdir}"/.keep.${ARCH}.txt
	done

	# ================================================================
	# Cleanup
	if [ $fail -eq 0 ]; then

		# Clean up all but latest 4 from mirror dir
		cd "${outdir}"
		for i in $(find -regextype posix-basic -mindepth 1 -maxdepth 1 -type d -regex '.*20[012][0-9]\{5\}.*' \
				| sed -e 's:^.*-\(20[^.]\+\).*$:\1:' \
				| sort -ur \
				| egrep -v "/${latest_iso_date}\$|/${latest_stage3_date}\$" \
				| egrep -v -f "${tmpdir}"/.keep.${ARCH}.txt \
				| tail -n +5); do

			$DEBUGP rm $VERBOSEP -rf $(pwd)/${i}
		done

		$DEBUGP rm $VERBOSEP -rf ${tmpdir}

	else
		echo "There was some failure for $ARCH during the weekly sync. Not doing cleanup for fear of dataloss." 1>&2
	fi
}

main() {
	# Process all the command line options first.
	while [[ $# -ne 0 ]]; do
		case $1 in
		-d|--debug)
			DEBUGP="echo"
			RSYNC_OPTS+=( -n )
			;;
		-v|--verbose)
			VERBOSEP="-v"
			RSYNC_OPTS+=( -v )
			;;
		-h|--help)
			usage 0
			;;
		*)
			usage 1
			;;
		esac
		shift
	done

	# Process all the architectures.
	local arch
	for arch in "${ARCHES[@]}"; do
		process_arch "${arch}"
	done
}
main "$@"

# vim:ts=2 sw=2 noet ft=sh:
