#!/bin/bash


rm -rf /root/.ssh
rm -f  /root/.bash_history /root/.lesshst /root/.recently-used.xbel /root/.recently-used.xbel /root/.viminfo

rm -f /etc/ssh/ssh_host_*

rm -f /etc/udev/rules.d/70-persistent-cd.rules  /etc/udev/rules.d/70-persistent-net.rules

rm -f /var/lib/dhcpcd-eth*
rm -f /var/lib/dhcpcd/*


>/var/log/everything/current
rm -f /var/log/everything/log*

>/var/log/critical/current
rm -f /var/log/critical/log*

>/var/log/cron/current
rm -f /var/log/cron/log*

>/var/log/mail/current
rm -f /var/log/mail/log*

>/var/log/pm-powersave.log
rm -f /var/log/pm-powersave/log*

>/var/log/pwdfail/current
rm -f /var/log/pwdfail/log*

>/var/log/tallylog

>/var/log/sshd/current
rm -f /var/log/sshd/log*

>/var/log/kernel/current
rm -f /var/log/kernel/log*

>/var/log/gdm/:0.log
rm -f /var/log/gdm/:0.log.*

>/var/log/Xorg.0.log
rm -f /var/log/Xorg.0.log.old

>/var/log/dmesg
>/var/log/emerge.log
>/var/log/emerge-fetch.log
>/var/log/faillog
>/var/log/genkernel.log
>/var/log/lastlog
>/var/log/wtmp
>/var/log/portage/elog/summary.log
>/var/log/ConsoleKit/history

find /var/log/ -size +1c -type f

