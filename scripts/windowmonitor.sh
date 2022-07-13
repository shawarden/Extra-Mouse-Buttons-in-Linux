#!/usr/bin/env bash
#####
# Monitor active window.
# If active window changes, output window properties.
#####

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
		echo "-------------"
		echo "${windowData}" | grep -E '^(WM_CLASS|WM_CLIENT_LEADER|WM_NAME)' | sort
		oldWindow=${curWindow}
	fi
done
