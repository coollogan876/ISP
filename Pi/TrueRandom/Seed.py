'''
Linear Congruential Method: http://www.columbia.edu/~ks20/4106-18-Fall/Simulation-LCG.pdf
Python bitwise operators: https://www.geeksforgeeks.org/python-bitwise-operators/
'''
import math
from time import sleep
from skimage import data
from skimage.feature import blob_log
from skimage.color import rgb2gray
import numpy as np
from PIL import Image
import TrueRandom.TrueRandom
import TrueRandom.cameraHander
from enum import Enum

class Seed:
    Method = Enum('Method', [('LCG', 1), ('MT', 2)])
    def __init__(self, cameraHandler):
        self.camera = cameraHandler

    #Linear Congruential Generator
    def __LCG(self, startValue, m, a, c, totalNumbers):
        '''
        Random number generator based on the linear congruential method

        Args: 
            startValue: Seed start value
            m: Modulus value to use
            a: Multiplier value to use
            c: Increment value to use
            totalNumbers: Total numbers to generate to take average of
        '''
        randomNumbers = [0] * totalNumbers
        randomNumbers[0] = startValue
        for x in range(1, totalNumbers):
            randomNumbers[x] = ((randomNumbers[x - 1] * a) + c) % m
        
        sum = 0
        for number in totalNumbers:
            sum += number
        return sum / totalNumbers
    
    def __twist(self, MT, upper_mask, lower_mask, n, a, m):
        for i in range(0, n):
            x = (MT[i] & upper_mask) + (MT[(i+1) % n] & lower_mask)
            xA = x >> 1
            if (x % 2) != 0:
                xA = xA ^ a
            MT[i] = MT[(i + m) % n] ^ xA
        return MT

    def __MT(self, w, n, m, r, seed):
        '''
        Random number generator based on the Mersenne Twister

        Args:
            w: Word size
            n: Degree of recurrence
            m: Middle word
            r: Separation point        
        '''
        a = 0x9908B0DF
        b = 0x9D2C5680
        c = 0xEFC60000
        s = 7        
        t = 15        

        MT = [0 for x in range(n)]
        index = n + 1
        lower_mask = (1 << r) - 1 
        upper_mask = ((1 << w) - 1) & ~lower_mask

        MT[0] = seed
        for x in range(1, n):
            temp = a * (MT[x - 1] ^ (MT[x - 1] >> (w - 2))) + x
            MT[x] = temp & 0xffffffff
        
        if index >= n:
            MT = self.__twist(MT, upper_mask, lower_mask, n, a, m)
            index = 0

        y = MT[index]
        y = y ^ ((y << s) & b)
        y = y ^ ((y << t) & c)

        index += 1
        return y & 0xffffffff    
        
    def generateValue(self, factor=10, maxTime=5, method=Method.LCG):
        '''
        Returns a random number

        Args:
            factor: A greater value will generate more random values
            maxTime: Maximum time allowed for generation. A longer time will result in more randomness (A max time of 0 will have no randomness other than the start value)
        '''
        interval = maxTime / 4
        self.camera.capture_file('startvalue.png')
        sleep(interval)
        self.camera.capture_file('modulus.png')
        sleep(interval)
        self.camera.capture_file('multipier.png')
        sleep(interval)
        self.camera.capture_file('increment.png')

        startValue = rgb2gray(np.array(Image.open('startvalue.png')))
        modulus = rgb2gray(np.array(Image.open('modulus.png')))
        multipier = rgb2gray(np.array(Image.open('multipier.png')))
        increment = rgb2gray(np.array(Image.open('increment.png')))

        max_sigma = 30
        num_sigma = 10
        threshold = .1

        startValueBlob = blob_log(startValue, 1, max_sigma, num_sigma, threshold)
        modulusBlob = blob_log(modulus, 1, max_sigma, num_sigma, threshold)
        multipierBlob = blob_log(multipier, 1, max_sigma, num_sigma, threshold)
        incrementBlob = blob_log(increment, 1, max_sigma, num_sigma, threshold)
        
        startValueAverage = np.mean(startValueBlob[:, 2] * math.sqrt(2))
        modulusAverage = np.mean(modulusBlob[:, 2] * math.sqrt(2))
        multipierAverage = np.mean(multipierBlob[:, 2] * math.sqrt(2))
        incrementAverage = np.mean(incrementBlob[:, 2] * math.sqrt(2))

        if isinstance(method.LCG, method):
            return self.__LCG(startValueAverage, modulusAverage, multipierAverage, incrementAverage, factor)

        self.camera.capture_file('seed.png')
        seed = rgb2gray(np.array(Image.open('seed.png')))
        seedBlob = blob_log(seed, 1, max_sigma, num_sigma, threshold)
        seedAverage = np.mean(seedBlob[:, 2] * math.sqrt(2))
        return self.__MT(startValueAverage, modulusAverage, multipierAverage, incrementAverage, seedAverage)