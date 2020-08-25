from functools import lru_cache
from functions import factorial
from constants import pi,e
from powers import power

def toRad(degrees):
    return (pi/180)*degrees

def sin(x : float,degrees=False,iterations : int = 100):
    if degrees:
        x = toRad(x)
    #Taylor series for sin x
    total = 0
    for i in range(iterations):
        alternating = (-1)**i
        denominator = factorial(2*i+1)
        alternating_denominator = alternating / denominator
        input_adjust = x**(2*i+1)
        total += alternating_denominator * input_adjust
    return total

def cos(x,degrees=False):
    if degrees:
        x = toRad(x)
    reduced_pi = pi / 2
    return sin(reduced_pi-x)


def tan(x,degrees=False):
    if degrees:
        x = toRad(x)
    return sin(x) / cos(x)

def cot(x,degrees=False):
    if degrees:
        x = toRad(x)
    return 1 / tan(x)

def sec(x,degrees=False):
    if degrees:
        x = toRad(x)
    return 1 / cos(x)

def csc(x,degrees=False):
    if degrees:
        x = toRad(x)
    return 1 / sin(x)

def sinh(x : float,useTaylor : bool = False,iterations: int = 100) -> float:
    if useTaylor:
        return sum([
            power(x,2*n+1) / factorial(2*n+1) for n in range(iterations)
        ])
    return (power(e,x) - power(e,-x)) / 2

def cosh(x : float,useTaylor : bool = False,iterations = 100) -> float:
    if not useTaylor:
        return (power(e,x) + power(e,-x)) / 2
    return sum([
        power(x,2*n) / factorial(2*n) for n in range(iterations)
    ])

def tanh(x : float) -> float:
    return sinh(x) / cosh(x)

def coth(x : float) -> float:
    return 1 / tanh(x)

def sech(x : float) -> float:
    return 1 / cosh(x)

def csch(x : float) -> float:
    return 1 / sinh(x)

def main():
    print(cos(pi/2))

if __name__ == "__main__":
    main()