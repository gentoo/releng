#!/bin/bash

# This script operates on a new vanilla linux-firmware savedconfig file to create
# an updated pruned file for minimal livecds.  It will directly replace the 
# linux-firwmare file in this directory.
#
# Some firmware types we prune include GPU firmwares, DVB firmwares, and unusually
# large firmwares for enterprise 10G+ NICs.

# Example usage:
#   ./prune_firmwares.sh /etc/portage/savedconfig/sys-kernel/linux-firmware-20230515
#   git add . && git commit -sS

echo "# $(git config user.name) <$(git config user.email)> ($(date +%Y-%m-%d))" > linux-firmware
echo "# Last updated for $(basename ${1})" >> linux-firmware

sed 	-e's/^a300/#a300/' \
	-e 's/^amd/#amd/' \
	-e 's/^airoha/#airoha/' \
	-e 's/^atusb/#atusb/' \
	-e 's/^av7110/#av7110/' \
	-e 's/^cadence/#cadence/' \
	-e 's/^cavium/#cavium/' \
	-e 's/^cmmb/#cmmb/' \
	-e 's/^dabusb/#dabusb/' \
	-e 's/^dsp56k/#dsp56k/' \
	-e 's/^dvb/#dvb/' \
	-e 's/^emi26/#emi26/' \
	-e 's/^ene-/#ene-/' \
	-e 's/^f2255/#f2255/' \
	-e 's/^go7007/#go7007/' \
	-e 's/^hfi1/#hfi1/' \
	-e 's/^i915/#i915/' \
	-e 's%^intel/vsc%#intel/vsc%' \
	-e 's%^intel/ipu%#intel/ipu%' \
	-e 's/^isdbt/#isdbt/' \
	-e 's/^keyspan/#keyspan/' \
	-e 's/^liquidio/#liquidio/' \
	-e 's/^matrox/#matrox/' \
	-e 's/^mellanox/#mellanox/' \
	-e 's/^moxa/#moxa/' \
	-e 's/^mts/#mts/' \
	-e 's/^netronome/#netronome/' \
	-e 's/^nvidia/#nvidia/' \
	-e 's/^qat/#qat/' \
	-e 's/^qed/#qed/' \
	-e 's/^r128/#r128/' \
	-e 's/r8a779x/#r8a779x/' \
	-e 's/^radeon/#radeon/' \
	-e 's/^s5p-mfc/#s5p-mfc/' \
	-e 's/^sms1/#sms1/' \
	-e 's/^sxg/#sxg/' \
	-e 's/^tdmb/#tdmb/' \
	-e 's/^tlg/#tlg/' \
	-e 's/^usbdux/#usbdux/' \
	-e 's/^v4l-/#v4l-/' \
	${1} >> linux-firmware
