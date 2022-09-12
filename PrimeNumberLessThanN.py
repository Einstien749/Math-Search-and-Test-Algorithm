"""Developer : Odimayo Taiye
FullStack Developer 

This program returns a list of Prime Numbers Less Than a number n"""

# PrimeNumber Test Function
from PrimeTest import *


def PrimeLessThanN(m):
    primeLessThanN = []
    for i in range(2,m):
        if PrimeTest(i) == "Number is a Prime":
            primeLessThanN.append(i)
    
    return primeLessThanN