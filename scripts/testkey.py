#!/usr/bin/env python3

from pynput import keyboard

realKey = '1'
bNumpadOnly = True

def isNumberPad(key):
	if hasattr(key, 'vk'):
		if key.vk is None:
			return True
		return False
	return False

def on_release(key):
	global realKey
	global bNumpadOnly
	if hasattr(key, 'char'):
		if key.char == realKey:
			if bNumpadOnly:
				if isNumberPad(key):
					return False
			else:
				return False

# wait until key is released
with keyboard.Listener(on_release=on_release) as listener:
	listener.join()
