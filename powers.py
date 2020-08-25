from basic import product
from num_theory import isEven
from basic import isInteger

def power(base : float,exponent : int) -> float:
    if exponent < 0:
        return 1 / power(base,-exponent)
    if not isInteger(exponent):
        print(exponent)
        raise ValueError("Power function cannot handle decimal numbers, \n if you want to use roots use function 'powers.nthRoot' with integer values")
    x = [base for i in range(exponent)]
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


