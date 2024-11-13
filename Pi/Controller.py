'''
LED Controller
Raspberry Pi reference: https://gpiozero.readthedocs.io
'''

from gpiozero import LED, Button
import time

#LEDs
LEDs = [LED(11), LED(13), LED(15), LED(19)]

#Buttons
buttons = [Button(12, pull_up = True), Button(16, pull_up = True), Button(18, pull_up = True), Button(22, pull_up = True)]

while True:
    x = 0
    while x < 4:
        if buttons[x].is_held:
            print('Button: ' + str(buttons[x]) + ' has been pressed\n')
            LEDs[x].on
            time.sleep(1)
            LEDs[x].off
        time.sleep(.025)