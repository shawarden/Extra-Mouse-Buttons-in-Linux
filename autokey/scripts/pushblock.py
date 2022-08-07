#!/usr/bin/env python3

import os

# Only do something it we're not already doing it.
if not store.has_key("pushing"):
    store.set_value("pushing",0)

if store.get_value("pushing") == 0:
    # Store state
    store.set_value("pushing",1)
    # Do the thing!
    #keyboard.press_key('2')
    print("pushing!")

    # Wait until we release the trigger key.
    os.system('~/.config/autokey/keyrelease.sh 87')

    # Wipe the value.
    store.set_value("pushing",0)
    # Stop doing the thing.
    #keyboard.release_key('2')
    print("relax!")


