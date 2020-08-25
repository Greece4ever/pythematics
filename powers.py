from basic import product
from num_theory import isEven
from basic import isInteger
import fractions
import functions
from typing import Union

def power(base : Union[float,int],exponent : Union[int,complex]) -> Union[float,complex]:
    """
    The power function equivalant of the python operation a**b\n
    it can handle any floating or integer value for a base\n
    for an exponent it can handle any integer or complex number but when provided a floating point number,\n
    it will convert it to an integer fraction and pass the operation to nthRoot,\n
    it is not suggested to use floats for exponents\n

    Here is how it treats complex numbers => :
    ** e^(ix) = cos(x) + i *sin(x) #cis(x) for short
    ** e^(i*ln(a)) = cis(ln(a))
    ** e^(ln(a^i)) = cis(ln(a))
    ** a^i = cis(ln(a))
    ** (a^i)^b = (cis(ln(a)))^b
    ** a^(bi) + a^c = (cis(ln(a)))^b + a^c
    ** a^(bi+c) = (cis(ln(a)))^b + a^c

    """
    if type(exponent) == type(complex(0,1)):
        s = exponent # a*i+b
        return power(base,s.real) + power(functions.cis(functions.ln(base)),s.imag)

    if exponent < 0:
        return 1 / power(base,-exponent)

    if not isInteger(exponent):
        if type(exponent) == float:
            # b^(k/n) <=> nthroot(b^k)
            res = fractions.Fraction(exponent) #external import to convert floating point to an integer fraction
            return nthRoot(power(base,res.numerator),res.denominator)
        else:
            raise ValueError("Power operations does not support {}".format(type(exponent)))

    x = [base for i in range(int(exponent))]
    return product(*x)


def isRoot(function : callable,x_0 : float,x_1 : float) -> bool:
    if (function(x_0)*function(x_1)) < 0:
        return True
    return False


def sqrt_subfunction(x,c):
    return power(x,2) - c


def sqrt(x : float,iterations : int = 100) -> float:
    if x <= 0:
        if(x==0):
            return 0.0
        raise ValueError("Value {} is less than 0".format(x))

    point = 1
    for i in range(iterations):
        function_difference = sqrt_subfunction(point,x) / (2*point)
        point = point - function_difference
    return point

def nth_subfunction(x,exponent,c):
        return power(x,exponent) - c

def nthRoot(subroot : float,n : int,iterations : int =100) -> float:
    # f(x) = x**n - c
    # f'(x) = n*x**(n-1) 
    if(isEven(n)) or n==0:
        if n==0:
            return 0.0
        if subroot < 0:
            raise ValueError("Even root must contain only positive floating values not {}".format(subroot))
    
    def diffeq(x):
        raised = power(x,n-1)
        return n*raised

    point = 1
    for i in range(iterations):
        function_difference = nth_subfunction(point,n,subroot) / diffeq(point)
        point = point - function_difference

    return point

if  __name__ == "__main__":
    print(power(2,complex(3,4))) 