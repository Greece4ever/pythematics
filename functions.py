from powers import power
from functools import lru_cache
from constants import e
from num_theory import isEven,isOdd

@lru_cache(maxsize=1000)
def factorial(n):
    if n in (1,0):
        return 1
    return n * factorial(n-1)


@lru_cache(maxsize=1000)
def doubleFactorial(n):
    if n in (1,0):
        return 1
    return n * doubleFactorial(n-2)

@lru_cache(maxsize=1000)
def fibonacci(n : int) -> int:
    if n in (0,1):
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

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

def myFunc(x):
    return 1 / x + x**5

if __name__ == "__main__":
    pass