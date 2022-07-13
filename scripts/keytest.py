#!/usr/bin/env python3

from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
import logging, sys, subprocess

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
					level=logging.DEBUG,
					stream=sys.stderr)

def get_active_window():
	cmd		= "xprop -id $(xdotool getactivewindow)"
	ps		= subprocess.Popen(
				cmd,
				shell=True,
				stdout=subprocess.PIPE,
				stderr=subprocess.STDOUT)
	output	= ps.communicate()[0].decode("utf-8").split('\n')
	for line in output:
		if "WM_CLASS(STRING)" in line:
			winClass = line.split('=')[1].split(',')[0].lstrip().strip('"')
			break
	return winClass

def on_press(key):
	if hasattr(key, 'vk'):
		logging.info("Key {0} ({1}) pressed on {2}".format(key, key.vk, get_active_window()))
	else:
		logging.info("Key {0} pressed on {2}".format(key, get_active_window()))

def on_release(key):
	if hasattr(key, 'vk'):
		logging.info("Key {0} ({1}) released on {2}".format(key, key.vk, get_active_window()))
	else:
		logging.info("Key {0} released on {2}".format(key, get_active_window()))

def on_move(x, y):
	global oldWindow
	currentWindow = get_active_window()
	if oldWindow != currentWindow:
		oldWindow = currentWindow
		logging.info("Mouse moved to ({0}, {1}) over {2}".format(x, y, currentWindow))

def on_click(x, y, button, pressed):
	if pressed:
		logging.info('Mouse {0} clicked at ({1}, {2}) on {3}'.format(button, x, y, get_active_window()))
	else:
		logging.info('Mouse {0} released at ({1}, {2}) on {3}'.format(button, x, y, get_active_window()))

def on_scroll(x, y, dx, dy):
	logging.info('Mouse scrolled at ({0}, {1})({2}, {3}) on {4}'.format(x, y, dx, dy, get_active_window()))

oldWindow = get_active_window()

# Setup the listener threads
keyboard_listener = KeyboardListener(on_press=on_press, on_release=on_release)
mouse_listener = MouseListener(on_click=on_click, on_scroll=on_scroll)

# Start the threads and join them so the script doesn't end early
keyboard_listener.start()
mouse_listener.start()
keyboard_listener.join()
mouse_listener.join()

