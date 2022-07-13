from os import system
from pynput import keyboard

keyboard_actual = keyboard.Controller()

def waitForKeyRelease(realKey,bNumpadOnly=False):
    print('Key?', realKey, 'Numpad?', bNumpadOnly)
    def isNumberPad(key):
        if hasattr(key, 'vk'):
            if key.vk is None:
                return True
            return False
        return False

    def on_release(key):
        nonlocal realKey
        nonlocal bNumpadOnly
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
    #system('~/.config/autokey/keyrelease.sh 87')

    waitForKeyRelease('1',True)

    print(' --- releasing ---')

    # Release keypress from store
    store.set_value("isPressed",True)
    # Release keypress
    keyboard_actual.release('2')
else:
    print(' --- spam ---')



    

