#!/usr/bin/env python3

from pynput import keyboard

def waitForKeyRelease(realKey,bNumpadOnly=False):
    """Waits for the desired key to be released"""

    def isNumberPad(key):
        """Checks if key is on the numberpad"""

        # Does key have virtual key attribute?
        if hasattr(key, 'vk'):
            # Is that virtual key None
            if key.vk is None:
                # It's on the numberpad? Or just the mouse?
                return True
            # It's not a numberbad/mapped mouse?
            return False
        # It doesn't have a virtual key attribute
        return False

    def on_release(key):
        """Exits listener on key release"""

        # What Key was it?
        nonlocal realKey
        # Numpad only?
        nonlocal bNumpadOnly

        # Is this a char key?
        # What if it's a special key?
        # FIX ME!
        if hasattr(key, 'char'):
            # Does our key match?
            if key.char == realKey:
                # Are we after a numberpad/mouse map?
                if bNumpadOnly:
                    # Is this key a numberpad/mouse map?
                    if isNumberPad(key):
                        # Exit listener
                        return False
                    # else: don't exit
                else:
                    # Exit listener
                    return False

    # Watch for key release trigger
    with keyboard.Listener(
        on_release=on_release
    ) as listener:
        listener.join()
