from time import sleep
from picamera2 import Picamera2, Preview
import TrueRandom.cameraHandler
from TrueRandom.Seed import Seed

class TrueRandom:
    def __init__(self, cameraHandler):
        self.cameraHandler = cameraHandler
        self.seed = Seed(cameraHandler)
        
    def random(self, maxTime, factor=None, minValue=0, maxValue=100):
        if factor is None:
            return minValue + (self.seed.generateValue(maxTime=maxTime, method=Seed.Method.MT)) % (maxValue - minValue + 1)
        return minValue + (self.seed.generateValue(factor, maxTime, Seed.Method.LCG)) % (maxValue - minValue + 1)