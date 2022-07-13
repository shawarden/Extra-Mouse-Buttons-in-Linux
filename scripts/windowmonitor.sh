#!/usr/bin/env bash

while :;
do
	windowData=$(
		xprop -id $(
			xprop -root 32x '\t$0' _NET_ACTIVE_WINDOW | \
			cut -f 2
		)
	)
	curWindow=$(
		echo "${windowData}" | \
		grep "WM_CLIENT_LEADER(WINDOW): window id #" | \
		awk -F' # ' '{print $2}'
	)
	if [ "${curWindow}" != "${oldWindow}" ]
	then
		echo "${windowData}"
		oldWindow=${curWindow}
	fi
done
