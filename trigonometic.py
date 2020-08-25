import functions
from constants import pi,e
from powers import power
from powers import sqrt

# Conversions

def toRad(degrees):
    """Degrees to rad"""
    return (pi/180)*degrees

def toDegrees(rad):
    """Rad to degrees"""
    return (180 / pi) * rad

# Trigonometric

def sin(x : float,degrees=False,iterations : int = 100):
    """Domain : All Real"""
    if degrees:
        x = toRad(x)
    #Taylor series for sin x
    total = 0
    for i in range(iterations):
        alternating = (-1)**i
        denominator = functions.factorial(2*i+1)
        alternating_denominator = alternating / denominator
        input_adjust = x**(2*i+1)
        total += alternating_denominator * input_adjust
    return total

def cos(x,degrees=False):
    """Domain : All Real"""
    if degrees:
        x = toRad(x)
    reduced_pi = pi / 2
    return sin(reduced_pi-x)

def tan(x,degrees=False):
    """Domain : Everything but cos(x) != 0 """
    if degrees:
        x = toRad(x)
    return sin(x) / cos(x)

def cot(x,degrees=False):
    """Domain : Everything but sin(x) != 0 """
    if degrees:
        x = toRad(x)
    return 1 / tan(x)

def sec(x,degrees=False):
    """Domain : Everything but cos(x) != 0 """
    if degrees:
        x = toRad(x)
    return 1 / cos(x)

def csc(x,degrees=False):
    """Domain : Everything but sin(x) != 0 """
    if degrees:
        x = toRad(x)
    return 1 / sin(x)

# Inverse Trigonometric

def arcsin(x : float,iterations : int = 100,degrees : bool = False) -> float:
    """Domain (-1 <= x <= 1)"""
    if not (-1 <= x <= 1):
        raise ValueError("Math domain error not in [-1,1]")
    total = 0
    for n in range(iterations):
        nominator_0 = functions.factorial(2*n)
        nominator_1 = power(x,2*n+1)
        denominator_0 = power(power(2,n)*functions.factorial(n),2)
        denominator_1 = 2*n+1
        div_0 = nominator_0 / denominator_0
        div_1 = nominator_1 / denominator_1
        total += div_1 * div_0
    if degrees:
        total = toDegrees(total)
    return total

def arccos(x : float,iterations : int = 100,degrees : bool = False) -> float:
    """Domain (-1 <= x <= 1)"""
    if not (-1 <= x <= 1):
        raise ValueError("Math domain error not in [-1,1]")
    result = (pi / 2) - arcsin(x,iterations=iterations)
    if degrees:
        result = toDegrees(result)
    return result

def arctan(x : float,iterations : int = 100,degrees : bool = False) -> float:
    """Domain : All Real"""
    total = 0
    for n in range(iterations):
        nom_0 = power(2,2*n) * power(functions.factorial(n),2)
        den_0 = functions.factorial(2*n+1)
        div_0 = nom_0 / den_0
        nom_1 = power(x,2*n+1)
        den_0 = power(1 + power(x,2),n+1)
        div_1 = nom_1 / den_0
        final = div_0 * div_1
        total += final
    if degrees:
        total = toDegrees(total)
    return total

def arccot(x : float,iterations : int = 100,degrees : bool = False):
    """Domain : All Real"""
    result = (pi / 2) - arctan(x,iterations=iterations)
    if degrees:
        result = toDegrees(result)
    return result

def arcsec(x : float,iterations : int = 100,degrees : bool = False):
    """Domain : (x <= -1 or x >= 1)"""
    if (x <= -1) or (x >= 1):
        res =  arccos(1/x,iterations=iterations)
        if degrees:
            res = toDegrees(res)
        return res
    else:
        raise ValueError("Math domain error not in (x <= -1 or x >= 1)")

def arccsc(x : float,iterations : int = 100,degrees : bool = False):
    """Domain : (x <= -1 or x >= 1)"""
    if (x <= -1) or (x >= 1):
        result = ( pi / 2 ) - arcsec(x)
        if degrees:
            result = toDegrees(result)
        return result
    else:
        raise ValueError("Math domain error not in (x <= -1 or x >= 1)")

# Hyperbolic Trigonometric

def sinh(x : float,useTaylor : bool = False,iterations: int = 100) -> float:
    if useTaylor:
        return sum([
            power(x,2*n+1) / functions.factorial(2*n+1) for n in range(iterations)
        ])
    return (power(e,x) - power(e,-x)) / 2

def cosh(x : float,useTaylor : bool = False,iterations = 100) -> float:
    if not useTaylor:
        return (power(e,x) + power(e,-x)) / 2
    return sum([
        power(x,2*n) / functions.factorial(2*n) for n in range(iterations)
    ])

def tanh(x : float) -> float:
    return sinh(x) / cosh(x)

def coth(x : float) -> float:
    return 1 / tanh(x)

def sech(x : float) -> float:
    return 1 / cosh(x)

def csch(x : float) -> float:
    return 1 / sinh(x)

# Inverse Hyperbolic

def arsinh(x : float) -> float:
    """Domain : All Real"""
    return functions.ln(x+sqrt(power(x,2)+1))

def arcosh(x : float) -> float:
    """Domain : [1, +Infinity)"""
    if x < 1:
        raise ValueError("Math domain error [1,+Infinity]")
    return functions.ln(x+sqrt(power(x,2)-1))

def artanh(x : float) -> float:
    """Domain (-1 < x < 1)"""
    if not -1 < x < 1:
        raise ValueError("Math domain error not in  (-1,+1)")
    return 0.5*functions.ln((1+x)/(1-x))

def arcoth(x : float) -> float:
    """(-Infinity, −1) and (1, +Infinity)"""
    if x == 1 or x == -1:
        raise ValueError("Math domain error not in  (-Infinity, −1) and (1, +Infinity)")
    return 0.5*functions.ln((x+1)/(x-1))

def arsech(x : float) -> float:
    """Domain : (0, 1]"""
    if x >= 0 or  x > 1:
        raise ValueError("Math domain error not in (0, 1]")
    return functions.ln( (1+sqrt(1-power(x,2)) / x ))

def arcsch(x : float) -> float:
    """Domain : All Real Numbers except 0"""
    if x == 0:
        raise ValueError("Math domain error not in (All Real Numbers except 0)")
    return functions.ln( (1/x) + sqrt((1/power(x,2)) + 1) )

if __name__ == "__main__":
    print(sin(90,degrees=True))