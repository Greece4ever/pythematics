from powers import power
from functools import lru_cache

@lru_cache(maxsize=1000)
def factorial(n):
    if n in (1,0):
        return 1
    return n * factorial(n-1)

def exp(x : float,iterations : int = 100,taylor_exapnsion=False):
    if(not taylor_exapnsion):
        return 
    """Taylor expansion of e^x used for approximations"""
    return sum([power(x,n) / factorial(n) for n in range(iterations)])

