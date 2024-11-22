'''
Display Dice
'''

from Display import *
import time
from gpiozero import Button
import random
import signal

button = Button(18, pull_up=True)

def randomNumber():
    numbers = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]
    return numbers[random.randint(0, 9)]()

def Roll():
    secs = random.uniform(.5, 8.0)
    amount = random.randint(3, 40)
    interval = secs / amount

    print(f'secs: {secs}\namount: {amount}\ninterval: {interval}\n')

    x = 0
    while x < amount:
        print(x)
        print(f'{randomNumber()}')
        time.sleep(interval)
        x += 1
        
    randomNumber()
    
    time.sleep(.025)


Clear()

button.when_activated = Roll

signal.pause()