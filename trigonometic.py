from functools import lru_cache
from functions import factorial
import json
import decimal

with open('constants.json') as jsonfile:
    x = json.loads(jsonfile.read())

pi = x['pi'][0]


def toRad(degrees):
    return (pi/180)*degrees

def sin(x : float,degrees=False):
    if degrees:
        x = toRad(x)
    #Taylor series for sin x
    total = 0
    for i in range(100):
        alternating = (-1)**i
        denominator = factorial(2*i+1)
        alternating_denominator = alternating / denominator
        input_adjust = x**(2*i+1)
        total += alternating_denominator * input_adjust
    return total

def cos(x,degrees=False):
    #sin^2(x)+cos^2(x) = 1 => 1-sin^2(x) 
    if degrees:
        x = toRad(x)
    sinx = sin(x)**2
    res = 1-sinx
    return res**(1/2)

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


print(cos(30,degrees=True))