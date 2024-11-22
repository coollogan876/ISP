'''
7 Segment Display
'''

from gpiozero import LED
import time
import signal

topLeft = LED(27, initial_value=False)
top = LED(22, initial_value=False)
topRight = LED(10, initial_value=False)

middle = LED(17, initial_value=False)

bottomLeft = LED(9, initial_value=False)
bottom = LED(11, initial_value=False)
bottomRight = LED(5, initial_value=False)

dp = LED(6, initial_value=False)

LEDs = [topLeft, top, topRight, middle, bottomLeft, bottom, bottomRight]

def Clear():
    for led in LEDs:
        led.on()

def Zero():
    Clear()
    topLeft.off()
    top.off()
    topRight.off()
    bottomLeft.off()
    bottom.off()
    bottomRight.off()
    return 0

def One():
    Clear()
    topRight.off()
    bottomRight.off()
    return 1

def Two():
    Clear()
    top.off()
    topRight.off()
    middle.off()
    bottomLeft.off()
    bottom.off()
    return 2

def Three():
    Clear()
    top.off()
    topRight.off()
    middle.off()
    bottomRight.off()
    bottom.off()
    return 3

def Four():
    Clear()
    topLeft.off()
    middle.off()
    topRight.off()
    bottomRight.off()
    return 4

def Five():
    Clear()
    top.off()
    topLeft.off()
    middle.off()
    bottomRight.off()
    bottom.off()
    return 5

def Six():
    Clear()
    top.off()
    topLeft.off()
    bottomLeft.off()
    bottom.off()
    bottomRight.off()
    middle.off()
    return 6

def Seven():
    Clear()
    top.off()
    topRight.off()
    bottomRight.off()
    return 7

def Eight():
    Clear()
    for led in LEDs:
        led.off()
    return 8

def Nine():
    Clear()
    middle.off()
    topLeft.off()
    top.off()
    topRight.off()
    bottomRight.off()
    return 9

dp.on()

signal.pause()