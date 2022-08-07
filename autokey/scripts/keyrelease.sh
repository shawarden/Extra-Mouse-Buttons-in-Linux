#!/bin/bash

# What key to watch for
keyNum=$1

# Loop until there are no $keyNum in the down state.
#	Get list of all xinput devices.
#		Skip pointers and master.
#		Strip everything before the id=
#		Strip everything after the id number.
#	Why oh why can't we just poll the root/master keyboard?
#	This wont work on wayland cuz no xinput
while for id in $(
		xinput list | \
		grep -v "pointer\|master" | \
		awk -F'id=' '{print $2}' | \
		awk '{print $1}'
		)
	do
		# Dump device state
		#	Pull out first instance of target key down
		xinput query-state $id | grep -P "key\[${keyNum}?\]=down" && break
	done | grep "down" &>/dev/null
do
		# As long as there's an active 'down' state, twiddle your thumbs.
		continue
done

# No down states found.
# Target key must be up.
