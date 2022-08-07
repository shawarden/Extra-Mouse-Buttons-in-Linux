222# No env since it's run within AutoKey

from os import system
from pynput.keyboard import Controller
from keystats import waitForKeyRelease
import logging, sys, subprocess

logging.basicConfig(
    format='%(asctime)s %(levelname)s %(message)s',
	level=logging.DEBUG,
	stream=sys.stderr
)

keyboard_actual = Controller()

logging.info("Does store exist?")
if not store.has_key("isPressed"):
    logging.info("Creating store.")
    store.set_value("isPressed",False)

logging.info("Are we pressing?")
if not store.get_value("isPressed"):
    logging.info("Not pressing!")

    logging.info("Set keypress to store")
    store.set_value("isPressed",True)
    logging.info("Press the key")
    keyboard_actual.press('2')

    logging.info("Wait for key release.")
    #system('~/.config/autokey/scripts/keyrelease.sh 87')
    waitForKeyRelease('1',True)

    logging.info("Release keypress from store")
    store.set_value("isPressed",True)
    logging.info("Release keypress")
    keyboard_actual.release('2')
else:
    logging.info("We're spamming again aren't we")





