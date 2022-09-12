"""Developer : Odimayo Taiye
FullStack Developer 

This program test if a number is a Prime Number"""

# PrimeNumber Test Function

def PrimeTest(n):
    h = True
    for i in range(2,n):
        if n%i == 0:
            h = False
            break
        else:
            pass
    
    if h:
        return "Number is a Prime"

    else:
        return "Number Not A Prime"
        