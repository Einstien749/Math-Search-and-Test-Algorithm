from PrimeTest import *
from PrimeNumberLessThanN import *
from math import *

""" Mersenne Prime Less Than a Number"""

def MersennePrime(m):
    p = []
    end = int(log2(m + 1))
    for i in range(2,end):
        if PrimeTest((2**i) - 1) == "Number is a Prime":
            p.append((2**i) - 1)
    
    return p