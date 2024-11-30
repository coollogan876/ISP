'''
Display Dice
pygame sound reference: https://www.pygame.org/docs/ref/mixer.html
'''

from Display import *
import time
from gpiozero import Button
import random
<<<<<<< Updated upstream
import signal
=======
>>>>>>> Stashed changes
from pygame import mixer

mixer.init()
ratchet = mixer.Sound("ratchet.wav")
<<<<<<< Updated upstream
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
=======
button = Button(7, pull_up=True)
prevNumber = -1
leftDisplay = Display(LED(27, initial_value=True), LED(22, initial_value=True), LED(10, initial_value=True), LED(17, initial_value=True), LED(9, initial_value=True), LED(11, initial_value=True), bottomRight = LED(5, initial_value=True))
rightDisplay = Display(LED(14, initial_value=True), LED(15, initial_value=True), LED(18, initial_value=True), LED(23, initial_value=True), LED(24, initial_value=True), LED(25, initial_value=True), LED(8, initial_value=True))

leftDisplay.Clear()
rightDisplay.Clear()

def randomNumber():
    global prevNumber
    
    leftNumbers = [leftDisplay.Zero, leftDisplay.One, leftDisplay.Two, leftDisplay.Three, leftDisplay.Four, leftDisplay.Five, leftDisplay.Six, leftDisplay.Seven, leftDisplay.Eight, leftDisplay.Nine]    
    rightNumbers = [rightDisplay.Zero, rightDisplay.One, rightDisplay.Two, rightDisplay.Three, rightDisplay.Four, rightDisplay.Five, rightDisplay.Six, rightDisplay.Seven, rightDisplay.Eight, rightDisplay.Nine]
     
    number = random.randint(0, 12)
    while number == prevNumber:
        number = random.randint(0, 12)
    prevNumber = number
    if number > 9:
        firstDigit = int(str(number).index(0, 0))
        secondDigit = int((str(number).index(1)))
        return f'{leftNumbers[firstDigit]()}{rightNumbers[secondDigit]()}'
    return f'{leftNumbers[0]()}{rightNumbers[number]()}'


while True:
    while not button.is_active:
        time.sleep(.1)
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
    print(f'{randomNumber()}')
=======
    print(f'{randomNumber()}')
>>>>>>> Stashed changes
