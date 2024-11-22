'''
Camera Test
Camera reference: https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf
'''

from picamera2 import Picamera2, Preview
import picamera2.encoders as encoders
import signal
import numpy as np
import time

camera = Picamera2()
camera.configure(camera.create_video_configuration())
camera.set_controls({"AwbEnable": True, "Contrast": 0.4, "Saturation" : 0.75})
camera.start_preview(Preview.QTGL)
camera.start()

#encoder = encoders.H264Encoder()

#camera.start_recording(encoder, 'lava.h264', quality=encoders.Quality.VERY_HIGH)
#time.sleep(10)
#camera.stop_recording()

signal.pause()