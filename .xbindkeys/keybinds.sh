#!/bin/bash
DEBUG=yes
button="${1}"
action="${2}"
device="${3}"

store=/dev/shm/${USER}-${button}-$(echo ${0}${button} | md5sum | awk '{print $1}')

function is_blocking() {
	if [ -f ${store} ]
	then
		return 0
	else
		return 1
	fi
}

function block() {
	touch ${store}
}

function unblock() {
	[ -f ${store} ] && rm ${store}
}

function log() {
	if [ "${DEBUG}" != "" ]
	then
		echo "$(date +%Y/%m/%d-%H:%M:%S.%N) ${*}" >> ~/.xbindkeys/log.txt
	fi
}

function is_down() {
	if [ "${action}" == "down" ]
	then
		return 0
	else
		return 1
	fi
}

function is_up() {
	if [ "${action}" == "up" ]
	then
		return 0
	else
		return 1
	fi
}

function isKeyUp() {
	key=${1}
	if getKeyStates ${key} | grep down &>/dev/null
	then
		return 0
	else
		return 1
	fi
}

function isKeyDown() {
	key=${1}
	if getKeyStates ${key} | grep down &>/dev/null
	then
		return 0
	else
		return 1
	fi

}

function getKeyStates() {
	key=$1
	for id in $(
		xinput list | \
		grep -v "pointer\|master" | \
		grep keyboard | \
		awk -F'id=' '{print $2}' | \
		awk '{print $1}'
		)
	do
		xinput query-state $id | grep -P "key\[${key}?\]="
	done
}

function waitForKeyRelease() {
	while is_down ${key}
	do
		continue
	done
}

function getActiveWindow() {
	# Clear window role.
	winRole=""

	# Get window ID
	winID=$(xdotool getactivewindow)

	# Get window title based on window id.
	winTitle=$(
		xprop -id ${winID} | \
		awk -F'=' '/^WM_NAME/{print $2}' | \
		sed -e 's/^\s//g' -e 's/\s$//g' -e 's/^"//g' -e 's/"$//g'
	)

	# Get window class
	echo $(
		xprop -id ${winID} | \
		awk '/^WM_CLASS/{print $NF}' | \
		sed -e 's/^\s//g' -e 's/\s$//g' -e 's/^"//g' -e 's/"$//g'
	)
}

winRole=$(getActiveWindow)

# Log window and button combo
log "${button} ${action} @ ${winRole} | ${store}"

# Different windows
case ${winRole} in
	firefox|Geany|Guake|Nemo)	# Web, documents, etc
		case ${button} in
			LeftEdgeFront)	is_up && xdotool key --clearmodifiers Control_L+Page_Up ;;
			LeftEdgeBack)	is_up && xdotool key --clearmodifiers Control_L+Page_Down ;;
			RightEdge)		is_up && xdotool key --clearmodifiers Control_L+w ;;
			*) ;;
		esac ;;
	steam_app_1172380) # STAR WARS Jedi: Fallen Order
		case ${button} in
			LeftEdgeFront)
				if is_down && ! is_blocking
				then
					block
#					python3 -c "from pynput.keyboard import Controller;keyboard = Controller();keyboard.press('2')"
  					xdotool getactivewindow keydown --clearmodifiers 2
				else
#					python3 -c "from pynput.keyboard import Controller;keyboard = Controller();keyboard.release('2')"
 					xdotool getactivewindow keyup --clearmodifiers 2
					unblock
				fi ;;
			LeftEdgeBack)	xdotool key${action} --clearmodifiers 3 ;;
			*) ;;
		esac ;;
	yakuake)	# Quake terminals
		case ${button} in
			LeftEdgeFront)	is_up && xdotool key --clearmodifiers shift+Left ;;
			LeftEdgeBack)	is_up && xdotool key --clearmodifiers shift+Right ;;
			*) ;;
		esac ;;
	*) ;;
esac
