from pynput.keyboard import Controller
from os import system as run
keyboard_actual = Controller()
keyboard_actual.press('i')
keyboard_actual.release('i')
run('wmctrl -a Exanima')