#!/bin/bash
unset winRole

winID=$(xdotool getactivewindow)

[ "${winRole}" == "" ] && winRole=$(xprop -id ${winID} | awk '/WM_WINDOW_ROLE/{print $3}' | tr -d '"')
[ "${winRole}" == "" ] && winRole=$(xprop -id ${winID} | awk '/WM_CLASS/{print $4}' | tr -d '"')
