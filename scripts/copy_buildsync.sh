#!/bin/bash

ARCHES="alpha amd64 arm hppa ia64      ppc s390 sh sparc x86"
       #alpha amd64 arm hppa ia64 mips ppc s390 sh sparc x86
#ARCHES="s390"
RSYNC_OPTS="-aO --delay-updates"
DEBUG=
VERBOSE=

OUT_STAGE3="latest-stage3.txt"
OUT_ISO="latest-iso.txt"

# Nothing to edit beyond this point

DEBUGP=
VERBOSEP=
[ -n "$DEBUG" ] && DEBUGP=echo
[ -n "$DEBUG" ] && RSYNC_OPTS="${RSYNC_OPTS} -n"
[ -n "$VERBOSE" ] && RSYNC_OPTS="${RSYNC_OPTS} -v"
[ -n "$VERBOSEP" ] && VERBOSEP="-v"

for ARCH in $ARCHES; do
	rc=0
	fail=0

	indir=/release/weekly/builds/${ARCH}
	outdir=/release/distfiles/weekly/${ARCH}
	tmpdir=/release/distfiles/tmp/buildsync/partial/${ARCH}

	mkdir -p ${tmpdir} 2>/dev/null
	# Copying
	if [ -d "${indir}" ]; then
		for i in $(find ${indir} -type f | grep -- '-20[0123][0-9]\{5\}' | sed -e 's:^.*-\(20[^.]\+\).*$:\1:' | sort -ur); do
			#echo "Doing $i"
			t="${outdir}/${i}"
			mkdir -p ${t} 2>/dev/null
			rsync ${RSYNC_OPTS} --temp-dir=${tmpdir} --partial-dir=${tmpdir} ${indir}/ --filter "S *${i}*" --filter 'S **/' --filter 'H *' ${t}
			rc=$?
			if [ $rc -eq 0 ]; then
				find ${indir} -type f -name "*${i}*" -print0 | xargs -0 --no-run-if-empty $DEBUGP rm $VERBOSEP -f
			else
				echo "Not deleting ${indir}/*${i}*, rsync failed!" 1>&2
				fail=1
			fi
		done
		find ${outdir} -mindepth 1 -type d \
			| egrep -v current \
			| sort -r \
			| tr '\n' '\0' \
			|xargs -0 --no-run-if-empty rmdir --ignore-fail-on-non-empty
	fi

	# ================================================================
	# Build data for revealing latest:
	# *.iso
	# stage3*bz2
	cd "${outdir}"
	# %T@

	iso_list="$(find 20* -name '*.iso' -printf '%h %f %h/%f\n' |grep -v hardened | sort -n)"
	stage3_list="$(find 20* -name 'stage3*bz2' -printf '%h %f %h/%f\n' |grep -v hardened | sort -n)"
	latest_iso_date="$(echo -e "${iso_list}" |awk '{print $1}' |cut -d/ -f1 | tail -n1)"
	latest_stage3_date="$(echo -e "${stage3_list}" |awk '{print $1}' |cut -d/ -f1 | tail -n1)"
	header="$(echo -e "# Latest as of $(date -uR)\n# ts=$(date -u +%s)")"

	# Do not remove this
	[ -z "${latest_iso_date}" ] && latest_iso_date="NONE-FOUND"
	[ -z "${latest_stage3_date}" ] && latest_stage3_date="NONE-FOUND"

	if [ -n "${iso_list}" ]; then
		echo -e "${header}" >"${OUT_ISO}"
		if [[ ! $(echo ${iso_list} | egrep "amd64|x86") ]]; then
			echo -e "${iso_list}" |awk '{print $3}' | grep "$latest_iso_date" >>${OUT_ISO}
			rm -f current-iso
			ln -sf "$latest_iso_date" current-iso
		fi
	fi
	if [ -n "${stage3_list}" ]; then
		echo -e "${header}" >"${OUT_STAGE3}"
		# In the new variant preserve code there is a better way to do this
		#echo -e "${stage3_list}" |awk '{print $3}' |grep "$latest_stage3_date" >>${OUT_STAGE3}
		rm -f current-stage3
		# The "latest stage3" concept doesn't apply to the arm/hppa/s390/sh variants
		# that are pushed on different days of the week.
		# Disable it for amd64/x86 as well as any failures cause confusion to users
		if [[ ! $(echo ${outdir} | egrep 'amd64|arm|hppa|ppc|s390|sh|x86') ]]; then
			ln -sf "$latest_stage3_date" current-stage3
		fi
	fi

	# new variant preserve code
	variants="$(find 20* \( -iname '*.iso' -o -iname '*.tar.bz2' \) -printf '%f\n' |sed  -e 's,-20[012][0-9]\{5\}.*,,g' -r | sort | uniq)"
	echo -n '' >"${tmpdir}"/.keep.${ARCH}.txt
	for v in $variants ; do
		variant_path=$(find 20* -iname "${v}-20*" \( -name '*.tar.bz2' -o -iname '*.iso' \) -print | sed -e "s,.*/$a/autobuilds/,,g" | sort -k1,1 -t/ | tail -n1 )
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
	#echo "$date_variant" \
	#| sort | uniq | sed -e 's,^,/,g' -e 's,$,$,g' >"${tmpdir}"/.keep.${ARCH}.txt

	# ================================================================
	# Cleanup
	if [ $fail -eq 0 ]; then
		# Clean up all but latest 4 from mirror dir
		cd "${outdir}"
		#echo regex "/${latest_iso_date}\$|/${latest_stage3_date}\$"
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

done

# vim:ts=2 sw=2 noet ft=sh:
