'''
7 Segment Display
Raspberry Pi reference: https://gpiozero.readthedocs.io
'''

from gpiozero import LED
import time

topLeft = LED(15, initial_value=False)
top = LED(18, initial_value=False)
topRight = LED(23, initial_value=False)

middle = LED(14, initial_value=False)

bottomLeft = LED(24, initial_value=False)
bottom = LED(25, initial_value=False)
bottomRight = LED(8, initial_value=False)

dp = LED(7, initial_value=False)

LEDs = [topLeft, top, topRight, middle, bottomLeft, bottom, bottomRight]

def Clear():
    for led in LEDs:
        led.off()

def Zero():
    Clear()
    topLeft.on()
    top.on()
    topRight.on()
    bottomLeft.on()
    bottom.on()
    bottomRight.on()

def One():
    Clear()
    topRight.on()
    bottomRight.on()

def Two():
    Clear()
    top.on()
    topRight.on()
    middle.on()
    bottomLeft.on()
    bottom.on()

def Three():
    Clear()
    top.on()
    topRight.on()
    middle.on()
    bottomRight.on()
    bottom.on()

def Four():
    Clear()
    topLeft.on()
    middle.on()
    topRight.on()
    bottomRight.on()

def Five():
    Clear()
    top.on()
    topLeft.on()
    middle.on()
    bottomRight.on()
    bottom.on()

def Six():
    Clear()
    top.on()
    topLeft.on()
    bottomLeft.on()
    bottom.on()
    bottomRight.on()
    middle.on()

def Seven():
    Clear()
    top.on()
    topRight.on()
    bottomRight.on()

def Eight():
    Clear()
    for led in LEDs:
        led.on()

def Nine():
    Clear()
    middle.on()
    topLeft.on()
    top.on()
    topRight.on()
    bottomRight.on()
