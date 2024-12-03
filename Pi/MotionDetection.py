'''
Movement Detection
Camera reference: https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf
Image processing reference: https://scikit-image.org/docs/stable/api/api.html
Pyvessync Library: https://github.com/webdjoe/pyvesync
'''

from picamera2 import Picamera2, Preview
import picamera2.encoders as encoders
from time import sleep
import numpy as np
import skimage
import os
from skimage.metrics import structural_similarity as ssim
import cv2
from pyvesync import VeSync
import json

camera = Picamera2()
camera.configure(camera.create_preview_configuration())
camera.start()
logininfo = open('vesync.json', 'r')
logininfo = json.loads(logininfo.read())
manager = VeSync(logininfo["email"], logininfo["password"], "America/Chicago")

manager.login()
manager.update()

plug = manager.outlets[0]
plug.turn_off()

while True:
    sleep(.25)
    camera.capture_file("initial.png")
    prevImageFile = 'initial.png'
    sleep(.1)
    camera.capture_file("current.png")
    currentImageFile =  "current.png"
    prevImage = cv2.imread(prevImageFile, cv2.IMREAD_GRAYSCALE)
    currentImage = cv2.imread(currentImageFile, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('current', currentImage)
    difference, diffMap = ssim(prevImage, currentImage, full=True)
    difference = (diffMap * 255).astype("uint8") 

    #Account for noise
    if difference.all() < .15:
        print("Motion detected!\n")
        plug.turn_on()
        sleep(10)
        plug.turn_off()
        #Light turning off will trigger it
        sleep(.35)

