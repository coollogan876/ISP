from time import sleep
from picamera2 import Picamera2, Preview
import TrueRandom.cameraHander
from TrueRandom.Seed import Seed

class TrueRandom:
    def __init__(self, cameraHandler):
        self.cameraHandler = cameraHandler
        self.seed = Seed(cameraHandler)
        

    def random(self, factor, maxTime, minValue=0, maxValue=100):
        return minValue + (self.seed.generateValue(factor, maxTime, Seed.Method.LCG)) % (maxValue - minValue + 1)

    def random(self, maxTime, minValue=0, maxValue=100):
        return minValue + (self.seed.generateValue(maxTime=maxTime, method=Seed.Method.MT)) % (maxValue - minValue + 1)