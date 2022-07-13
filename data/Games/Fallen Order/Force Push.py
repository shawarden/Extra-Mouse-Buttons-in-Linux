# No env since it's run within AutoKey

from os import system
from pynput import keyboard
from keystats import waitForKeyRelease

keyboard_actual = keyboard.Controller()

# Does store exist?
if not store.has_key("isPressed"):
    # Create store.
    store.set_value("isPressed",False)

# Are we pressing?
if not store.get_value("isPressed"):
    # Not pressing.

    print(' --- pressing ---')

    # Set keypress to store
    store.set_value("isPressed",True)
    # Press the key
    keyboard_actual.press('2')

    # Wait for key release.
    #system('~/.config/autokey/scripts/keyrelease.sh 87')

    waitForKeyRelease('1',True)

    print(' --- releasing ---')

    # Release keypress from store
    store.set_value("isPressed",True)
    # Release keypress
    keyboard_actual.release('2')
else:
    print(' --- spam ---')





