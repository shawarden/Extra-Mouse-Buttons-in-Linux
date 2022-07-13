#!/usr/bin/env python3

from pynput import keyboard
import logging, sys, subprocess

logging.basicConfig(
    format='%(asctime)s %(levelname)s %(message)s',
	level=logging.DEBUG,
	stream=sys.stderr
)

def waitForKeyRelease(realKey,bNumpadOnly=False):
    logging.info("Wait for the desired key to be released")

    def isNumberPad(key):
        logging.info("Check if key is numpad/mapped")

        logging.info("Does key have virtual key attribute?")
        if hasattr(key, 'vk'):
            logging.info("YES! Is that virtual key empty/None?")
            if key.vk is None:
                logging.info("YES! It's numpad/mapped")
                return True
            logging.info("NO! It's not a numpad/mapped")
            return False
        logging.info("NO!")
        return False

    def on_release(key):
        logging.info("Exits listener on key release")

        nonlocal realKey
        logging.info("Target key: "+realKey)
        nonlocal bNumpadOnly
        logging.info("Numpad/mapped key? "+bNumpadOnly)

        logging.info("Is this a char key?")
        if hasattr(key, 'char'):
            logging.info("YES! Does our key match?")
            if key.char == realKey:
                logging.info("YES! Are we after numpad/mapped?")
                if bNumpadOnly:
                    logging.info("YES! Is this key numpad/mapped?")
                    if isNumberPad(key):
                        logging.info("YES! Exit listener")
                        return False
                    else:
                        logging.info("NO! Not numbpad/mapped.")
                else:
                    logging.info("NO! Exit listener")
                    return False
            else:
                logging.info("NO! Keep waiting.")
        else:
            logging.info("NO! Need to handle other keys!")

    logging.info("Watch for key release trigger")
    with keyboard.Listener(
        on_release=on_release
    ) as listener:
        listener.join()
    logging.info("Key released!"
