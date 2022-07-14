# No env since it's run within AutoKey

from os import system
from pynput.keyboard import Controller
from keystates import waitForKeyRelease
import logging, sys, subprocess

bindKey='m'
outputKey='2'
isNumpad=False
storeVal='isPressed'

logging.basicConfig(
    format='%(asctime)s %(levelname)s %(message)s',
    level=logging.DEBUG,
    stream=sys.stdout
)

keyboard_actual = Controller()

if not store.has_key(storeVal):
    logging.debug("AK - Store {0} doesn't exist.".format(storeVal))
    store.set_value(storeVal,False)
else:
    logging.debug("AK - Store {0} already exists.".format(storeVal))

if not store.get_value(storeVal):
    logging.debug("AK - Store {0} says we're not pressing!".format(storeVal))

    logging.debug("AK - Store pressed to {0}.".format(storeVal))
    store.set_value(storeVal,True)
    logging.debug("AK - Press Key {0}".format(outputKey))
    keyboard_actual.press(outputKey)

    logging.debug("AK - Wait for Key {0} release.".format(bindKey))
    #system('~/.config/autokey/scripts/keyrelease.sh 87')
    waitForKeyRelease(bindKey,isNumpad)

    logging.debug("AK - Store release to {0}".format(storeVal))
    store.set_value(storeVal,False)
    logging.debug("AK - Release key {0}".format(outputKey))
    keyboard_actual.release(outputKey)
else:
    logging.debug("AK - Key {0} is already down. STOP SPAMMING!".format(bindKey))





