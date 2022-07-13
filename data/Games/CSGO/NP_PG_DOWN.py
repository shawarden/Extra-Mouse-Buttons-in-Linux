import keyboard as keyboard2      # using python's keyboard module
import time                       # sleep function

while True:                       # making a loop
    keyboard.send_keys("1")
    if keyboard2.is_pressed('q'): # if key 'q' is pressed
        break                     # finishing the loop
    else:
        time.sleep(2)             # Not too fast there bucko.
