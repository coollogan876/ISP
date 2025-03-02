'''
VEX competition switch wiring: https://static.rapidonline.com/downloads/vex/Make-Competition-Switch.pdf
'''
from gpiozero import LED, Button
from pygame import *
import pygame
from time import sleep
mixer.init()
pygame.init()
enable = LED(14)
driver = LED(15)

start = Button(20, pull_up=True)
auton = Button(21, pull_up=True)

startSound = mixer.Sound("Pi/Comp switch/Start.wav")
stopSound = mixer.Sound("Pi/Comp switch/Stop.wav")
pauseSound = mixer.Sound("Pi/Comp switch/Pause.wav")
warningSound = mixer.Sound("Pi/Comp switch/Warning.wav")
abortSound = mixer.Sound("Pi/Comp switch/Abort.wav")

screen = display.set_mode((1920, 1080))
display.set_caption("VEX Match Timer")
font = font.Font(None, 50)


def update_display(time_left, mode):
    screen.fill((13, 17, 23))  
    text = font.render(f"{mode}: {time_left}s", True, (255, 255, 255))
    screen.blit(text, (50, 80))
    display.flip()

update_display(0, "Waiting...")
time_left = 0
running = True

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

    while not start.is_active:
        pass  
    
    if auton.is_active:
        time_left = 15
        mode = "Autonomous"
        startSound.play()
        enable.on()
        driver.off()
    else:
        time_left = 105
        mode = "Driver"
        startSound.play()
        enable.on()
        driver.on()
    
    while time_left > 0:
        if start.is_active:
            abortSound.play()
            enable.off()
            driver.off()
            update_display(0, "Match is paused")
            sleep(2)
            break
        
        if time_left == 30:
            warningSound.play()
        
        update_display(time_left, mode)
        time_left -= 1
        sleep(1)
    
    enable.off()
    driver.off()
    if mode == "Driver":
        stopSound.play()
    else:
        pauseSound.play()
    update_display(0, "Match Over")
    sleep(2) 