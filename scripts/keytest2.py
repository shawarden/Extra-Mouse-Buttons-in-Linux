#!/usr/bin/env python3

from pynput import keyboard

def on_press(key):
	if hasattr(key, "vk") and key.vk == "None":
		numpad = True
	else:
		numpad = False

	try:
		print('alphanumeric key {0} (NP:{1}) pressed'.format(
			key.char, numpad))
	except AttributeError:
		print('special key {0} pressed'.format(
			key))

def on_release(key):
	print('{0} released'.format(
		key))
	if key == keyboard.Key.esc:
		# Stop listener
		return False

# Collect events until released
with keyboard.Listener(
		on_press=on_press,
		on_release=on_release) as listener:
	listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
	on_press=on_press,
	on_release=on_release)
listener.start()
