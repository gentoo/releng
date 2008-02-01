#!/bin/bash
# This is where we will put any release-specific fsscript code

if [[ -e /etc/conf.d/clock ]]
then
	sed -i -e 's/#TIMEZONE="Factory"/TIMEZONE="UTC"/' /etc/conf.d/clock
fi

case `uname -m` in
	i?86|x86_64)
		sed -i 's/DRIVER fbdev/DRIVER vesa/' /usr/share/hwdata/Cards
		sed -e 's/CONSOLEFONT="default8x16"/CONSOLEFONT="lat1-16"/' \
			-e '/^#CONSOLETRANSLATION="8859-1_to_uni"/ s/^#//' \
			-i /etc/conf.d/consolefont
	;;
esac

