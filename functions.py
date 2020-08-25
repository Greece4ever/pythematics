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

def ln(x : float,iterations : int = 100) -> float:
    if x < 0:
        raise ValueError("Complex domain error")
    total = 0
    for k in range(iterations):
        denominator = 1 / (2*k+1)
        apr = (x - 1) / (x + 1)
        final = denominator * power(apr,2*k+1)
        total += final
    return 2*total

def log(of_num : float,base : float = 10) -> float:
    return ln(of_num) / ln(base)


if __name__ == "__main__":
    print(log(8,2))
