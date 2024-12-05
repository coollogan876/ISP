'''
Python bitwise operators: https://www.geeksforgeeks.org/python-bitwise-operators/
'''
import time

def __twist(MT, upper_mask, lower_mask, n, a, m):
        for i in range(0, n):
            x = (MT[i] & upper_mask) + (MT[(i+1) % n] & lower_mask)
            xA = x >> 1
            if (x % 2) != 0:
                xA = xA ^ a
            MT[i] = MT[(i + m) % n] ^ xA
        return MT

def __MT(w, n, m, r, seed):
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
        MT = __twist(MT, upper_mask, lower_mask, n, a, m)
        index = 0

    y = MT[index]
    y = y ^ ((y << s) & b)
    y = y ^ ((y << t) & c)

    index += 1
    return y & 0xffffffff

minValue = 0
maxValue = 100

#Generate a random number using the time as a seed
print(minValue + (__MT(25, 10, 4, 5, (time.time() * 1000).__int__())) % (maxValue - minValue + 1)) 