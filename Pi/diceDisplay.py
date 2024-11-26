'''
Display Dice
pygame sound reference: https://www.pygame.org/docs/ref/mixer.html
'''

from Display import *
import time
from gpiozero import Button
import random
import signal
from pygame import mixer

mixer.init()
ratchet = mixer.Sound("ratchet.wav")
button = Button(18, pull_up=True)
prevNumber = 10

def randomNumber():
    global prevNumber
    leftDisplay = Display(LED(27, initial_value=True), LED(22, initial_value=True), LED(10, initial_value=True), LED(17, initial_value=True), LED(9, initial_value=True), LED(11, initial_value=True), bottomRight = LED(5, initial_value=True))
    # rightDisplay = Display(LED(14, initial_value=True), LED(15, initial_value=True), LED(18, initial_value=True), LED(23, initial_value=True), LED(24, initial_value=True), LED(25, initial_value=True), LED(8, initial_value=True))
    numbers = [leftDisplay.Zero, leftDisplay.One, leftDisplay.Two, leftDisplay.Three, leftDisplay.Four, leftDisplay.Five, leftDisplay.Six, leftDisplay.Seven, leftDisplay.Eight, leftDisplay.Nine]    

    number = random.randint(0, 9)
    while number == prevNumber:
        number = random.randint(0, 9)
    prevNumber = number
    return numbers[number]()

while True:
    while not button.is_active:
        pass
    secs = random.uniform(.5, 8.0)
    amount = random.randint(3, 40)
    interval = secs / amount
    print(f'secs: {secs}\namount: {amount}\ninterval: {interval}\n')
    x = 0
    while x < amount:   
        ratchet.play()     
        ratchet.fadeout(150)
        print(f'{randomNumber()}')
        time.sleep(interval)
        x += 1
        
    ratchet.play()
    ratchet.fadeout(150)
    print(f'{randomNumber()}')
