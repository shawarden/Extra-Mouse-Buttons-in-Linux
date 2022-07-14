#!/usr/bin/env python3

from pynput import keyboard
import logging, sys, subprocess

logging.basicConfig(
    format='%(asctime)s %(levelname)s %(message)s',
	level=logging.DEBUG,
	stream=sys.stdout
)

def waitForKeyRelease(realKey,bNumpadOnly=False):
    """Wait for the desired key to be released"""

    def isNumberPad(key):
        """Check if key is numpad/mapped"""

        if hasattr(key, 'vk'):
            logging.info("KS - Key {0} has vk!".format(key))
            if key.vk is None:
                logging.info("KS - KEy {0}s vk is {1}".format(key.vk))
                return True
            else:
                logging.info("KS - Key {0} is not a numpad/mapped".format(key))
                return False
        else:
            logging.info("KS - Key {0} does not have vk".format(key))
            return False

    def on_release(key):
        """Exits listener on key release"""

        nonlocal realKey
        nonlocal bNumpadOnly
        logging.info("KS - Targets: Key {0}, Numpad/mapped: {1}".format(realKey, bNumpadOnly))

        if hasattr(key, 'char'):
            logging.info("KS - Key {0} is char key {1}.".format(key, key.char))
            if key.char == realKey:
                logging.info("KS - Key {0} is target Key {1}".format(key.char,realKey))
                if bNumpadOnly:
                    logging.info("KS - We want numpad/mapped key!")
                    if isNumberPad(key):
                        logging.info("KS - Key {0} is numpad/mapped!".format(key))
                        return False
                    else:
                        logging.info("KS - Key {0} is NOT numpad/mapped!".format(key))
                else:
                    logging.info("KS - Don't care if {0} is numpad/mapped!".format(key))
                    return False
            else:
                logging.info("KS - Key {0} is not target key {1}!".format(key,realKey))
        else:
            logging.info("KS - Key {0} does not have vk attribute!".format(key))

    logging.info("KS - Watch for key {0}:{1} release trigger!".format(realKey,bNumpadOnly))
    with keyboard.Listener(
        on_release=on_release
    ) as listener:
        listener.join(2)
    logging.info("KS - Key {0}:{1} released!".format(realKey,bNumpadOnly))
