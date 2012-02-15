#!/bin/sh

. common.sh
check_cookie
write_header "inetd Setup"

CONFF=/etc/inetd.conf

#debug

cat<<-EOF
	<form action="/cgi-bin/inetd_proc.cgi" method="post">
	<table><tr>
	<td><strong> Service </strong></td>
	<td align=center><strong> Enable </strong></td>
	<td></td>
	</tr>
EOF

# FIXME: add service description
ssrv="rsync ssh telnet ftp http printer swat"
if test -f /usr/sbin/saned; then ssrv="$ssrv sane"; fi
for i in $ssrv; do
	chkf=""
	if $(grep -q -e "^$i" $CONFF); then
		chkf="checked"
	fi
	
	if test -f $PWD/${i}.cgi; then
		conf="<td><input type="submit" name=$i value="Configure"></td>"
	else
		conf="<td></td>"
	fi

	cat<<-EOF
		<tr><td> $i </td>
		<td align=center><input type=checkbox $chkf name=$i value=enable></td>
		$conf
		</tr>
	EOF
done

cat<<-EOF
	<tr><td></td><td><input type="submit" name="$ssrv" value="Submit"></td>
	<td>$(back_button)</td></tr>	
	</table></form></body></html>
EOF

#enddebug

