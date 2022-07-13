import os
from pynput.keyboard import Controller

keyboard_actual = Controller()

if not store.has_key("pulling"):
    store.set_value("pulling",0)

if store.get_value("pulling") == 0:
    store.set_value("pulling",1)
    keyboard_actual.press('2')
    os.system('~/.config/autokey/keyrelease.sh 87')
    store.set_value("pulling",0)
    keyboard_actual.release('2')

    

