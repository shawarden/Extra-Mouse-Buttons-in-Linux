#!/usr/bin/env python3

from pynput import keyboard

def waitForKeyRelease(realKey,bNumpadOnly=False):
    def isNumberPad(key):
        if hasattr(key, 'vk'):
            if key.vk is None:
                return True
            else:
                return False
        else:
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

    with keyboard.Listener(
        on_release=on_release
    ) as listener:
        listener.join()
