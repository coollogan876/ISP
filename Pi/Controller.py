'''
LED Controller
Raspberry Pi reference: https://gpiozero.readthedocs.io
Circuit Design: https://crcit.net/c/d0e7eb11211740389b50099ff14f1bc9
'''

from gpiozero import LED, Button
import signal
import threading
import time

#LEDs
led1 = LED(17, initial_value=False)
led2 = LED(27, initial_value=False)
led3 = LED(22, initial_value=False)
led4 = LED(10, initial_value=False)

#Buttons
button1 = Button(18, pull_up=True)
button2 = Button(23, pull_up=True)
button3 = Button(24, pull_up=True)
button4 = Button(25, pull_up=True)

def Light(led):
    led.on()
    time.sleep(1)
    led.off()


def Pressed1():
    print("Button 1 pressed\n")
    threading.Thread(target=Light, args=(led1,)).start()

def Pressed2():
    print("Button 2 pressed\n")
    threading.Thread(target=Light, args=(led2,)).start()

def Pressed3():
    print("Button 3 pressed\n")
    threading.Thread(target=Light, args=(led3,)).start()

def Pressed4():
    print("Button 4 pressed\n")
    threading.Thread(target=Light, args=(led4,)).start()

button1.when_activated = Pressed1
button2.when_activated = Pressed2
button3.when_activated = Pressed3
button4.when_activated = Pressed4

signal.pause()