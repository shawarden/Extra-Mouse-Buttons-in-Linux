# No env since it's run within AutoKey

from os import system
from pynput.keyboard import Controller
from keystates import waitForKeyRelease

bindKey='1'
outputKey='2'
isNumpad=False
storeVal='isPressed'

keyboard_actual = Controller()

if not store.has_key(storeVal):
    store.set_value(storeVal,False)

if not store.get_value(storeVal):
    print('---- PRESS ----')
    store.set_value(storeVal,True)
    keyboard_actual.press(outputKey)
    system('~/.config/autokey/scripts/keyrelease.sh 87')
    #waitForKeyRelease(bindKey,isNumpad)
    store.set_value(storeVal,False)
    keyboard_actual.release(outputKey)
    print('---- RELEASE ----')
else:111
    print('---- SPAM ----')
