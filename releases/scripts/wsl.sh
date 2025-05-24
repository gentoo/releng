mask_systemd_units() {
	local known_bad_units=(
		NetworkManager.service
		systemd-networkd.service
		systemd-networkd.socket
		systemd-resolved.service
		systemd-tmpfiles-clean.service
		systemd-tmpfiles-clean.timer
		systemd-tmpfiles-setup-dev-early.service
		systemd-tmpfiles-setup-dev.service
		systemd-tmpfiles-setup.service
		tmp.mount
	)
	for unit in "${known_bad_units[@]}"; do
		# Mask the unit to prevent it from starting automatically
		# We also do this when the OOBE script runs (in case the user does a DIY install from stage3)
		# but systemd will start when the container starts, so the earlier the better
		systemctl mask "$unit" >/dev/null 2>&1 || true
	done
}

if command -v systemctl >/dev/null 2>&1; then
	mask_systemd_units
elif command -v rc-service >/dev/null 2>&1; then
	rc-update delete systemd-tmpfiles-setup boot
	rc-uptade delete systemd-tmpfiles-setup-dev sysinit
fi

if ! grep -Fqx 'WSLPATH=${PATH}' /etc/profile; then
	# Insert our block before the first line matching the anchor
	tmp=$(mktemp)
	awk 'BEGIN{done=0}
		$0 ~ /^# Load environment settings from profile.env/ && !done {
			print "# 961809: WSL: store any injected Windows PATH components"
			print "if [[ -f /proc/sys/fs/binfmt_misc/WSLInterop && -n \"$PATH\" ]]; then"
			print "\tWSLPATH=${PATH}"
			print "fi"
			print ""
			done=1
		}
		{ print }' /etc/profile > "$tmp" && cat "$tmp" > /etc/profile
	rm -f "$tmp"
fi

if ! grep -Fqx 'if [[ -v WSLPATH ]]; then' /etc/profile; then
	tmp=$(mktemp)
	awk 'BEGIN{done=0}
		$0 ~ /^# You should override/ && !done {
			print "# 961809: suffix WSLPATH to PATH if we stored it"
			print "if [[ -v WSLPATH ]]; then"
			print "\texport PATH=${PATH}:${WSLPATH}"
			print "\tunset WSLPATH"
			print "fi"
			print ""
			done=1
		}
		{ print }' /etc/profile > "$tmp" && cat "$tmp" > /etc/profile
	rm -f "$tmp"
fi
