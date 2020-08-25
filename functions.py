from powers import power
from functools import lru_cache
from constants import e

@lru_cache(maxsize=1000)
def factorial(n):
    if n in (1,0):
        return 1
    return n * factorial(n-1)

def exp(x : float,iterations : int = 100,taylor_exapnsion=False):
    if(not taylor_exapnsion):
        return power(e,x)
    return sum([power(x,n) / factorial(n) for n in range(iterations)])

def ln(x,iterations=100):
    #ln(1+x)
    sumarray = [
        power(-1,n+1)*(power(x,n) / n) for n in range(1,iterations)
    ]
    return sum(sumarray)

if __name__ == "__main__":
    print(ln(e-1))    
