'''
7 Segment Display
'''

from gpiozero import LED
import time
import signal

class Display:
    def __init__(self, topLeft, top, topRight, middle, bottomLeft, bottom, bottomRight):
        self.topLeft = topLeft
        self.top = top
        self.topRight = topRight
        self.middle = middle
        self.bottomLeft = bottomLeft
        self.bottom = bottom
        self.bottomRight = bottomRight
        self.LEDs = [topLeft, top, topRight, middle, bottomLeft, bottom, bottomRight]

    def Clear(self):
        for led in self.LEDs:
            led.on()

    def Zero(self):
        self.Clear()
        self.topLeft.off()
        self.top.off()
        self.topRight.off()
        self.bottomLeft.off()
        self.bottom.off()
        self.bottomRight.off()
        return 0

    def One(self):
        self.Clear()
        self.topRight.off()
        self.bottomRight.off()
        return 1

    def Two(self):
        self.Clear()
        self.top.off()
        self.topRight.off()
        self.middle.off()
        self.bottomLeft.off()
        self.bottom.off()
        return 2

    def Three(self):
        self.Clear()
        self.top.off()
        self.topRight.off()
        self.middle.off()
        self.bottomRight.off()
        self.bottom.off()
        return 3

    def Four(self):
        self.Clear()
        self.topLeft.off()
        self.middle.off()
        self.topRight.off()
        self.bottomRight.off()
        return 4

    def Five(self):
        self.Clear()
        self.top.off()
        self.topLeft.off()
        self.middle.off()
        self.bottomRight.off()
        self.bottom.off()
        return 5

    def Six(self):
        self.Clear()
        self.top.off()
        self.topLeft.off()
        self.bottomLeft.off()
        self.bottom.off()
        self.bottomRight.off()
        self.middle.off()
        return 6

    def Seven(self):
        self.Clear()
        self.top.off()
        self.topRight.off()
        self.bottomRight.off()
        return 7

    def Eight(self):
        self.Clear()
        for led in self.LEDs:
            led.off()
        return 8

    def Nine(self):
        self.Clear()
        self.middle.off()
        self.topLeft.off()
        self.top.off()
        self.topRight.off()
        self.bottomRight.off()
        return 9
