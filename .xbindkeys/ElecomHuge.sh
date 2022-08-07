#!/bin/bash
DEBUG=yes
button="${1}"
action="${2}"

function log {
	[ "${DEBUG}" != "" ] && echo "${*}" >> ~/.xbindkeys/log.txt
}

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
winRole=$(
	xprop -id ${winID} | \
	awk '/^WM_CLASS/{print $NF}' | \
	sed -e 's/^\s//g' -e 's/\s$//g' -e 's/^"//g' -e 's/"$//g'
)

# Log window and button combo
log "${button} ${action} @ ${winRole} | ${winTitle}"

# Different windows
case ${winRole} in
	firefox|Geany)	# Web, documents, etc
		case ${button} in
			fn1)
				[ "${action}" == "up" ] && xdotool key --clearmodifiers Control_L+Page_Up
				;;
			fn2)
				[ "${action}" == "up" ] && xdotool key --clearmodifiers Control_L+Page_Down
				;;
			fn3)
				[ "${action}" == "up" ] && xdotool key --clearmodifiers Control_L+w
				;;
			*) ;;
		esac
		;;
	yakuake)	# Quake terminals
		case ${button} in
			fn1)
				[ "${action}" == "up" ] && \
				xdotool key --clearmodifiers shift+Left
				;;
			fn2)
				[ "${action}" == "up" ] && \
				xdotool key --clearmodifiers shift+Right
				;;
			fn3)
				[ "${action}" == "up" ] && \
				xdotool key --clearmodifiers ctrl+shift+w
				;;
			*) ;;
		esac
		;;
	steam_app_4920)	# Natural Selection 2 Game. All dames?
		case ${button} in
			fn1)
				[ "${action}" == "down" ] && \
				xdotool key --clearmodifiers '4' || \
				xdotool key --clearmodifiers '1'
				;;
			fn2)
				[ "${action}" == "down" ] && \
				xdotool key --clearmodifiers '2' || \
				xdotool key --clearmodifiers '1'
				;;
			fn3)
				[ "${action}" == "down" ] && \
				xdotool key --clearmodifiers '3' || \
				xdotool key --clearmodifiers '1'
				;;
			*) ;;
		esac
		;;
	*) ;;
esac
