#Relative imports
from .random import random_complex;from .basic import isNumber,isInteger;from .basic import product; 
#Built-in imports
from typing import Union
import re

NUMBER_REGEX = r"(((\-)|(\+))?\d+((\.)\d+)?)"

class Polynomial:
    def __init__(self,coefficients : list):
        degrees = {}
        i = 0
        for coefficient in coefficients:
            degrees[i] = coefficient
            i+=1
        if coefficients.count(0) == len(coefficients):
            degrees = {0 : 0}
        if len(coefficients) == 1:
            degrees = {0 : coefficients[0]}
        self.degree = i-1
        self.equation = degrees
        self.array = coefficients
        self.function = eval("lambda x :" + self.__str__(useSymbol=True).split(":")[1].strip().replace("^","**"))
        self.type = type(self)

    def eq(self):
        return self.equation

    def arr(self):
        return self.array

    def getFunction(self):
        return self.function

    def deg(self):
        return self.degree

    def __str__(self,useSymbol : bool = False):
        eq = []
        j = 0
        for item in self.equation:  
            if self.equation.get(item) == 0:
                continue
            eq.append(f'{"+" if j != len(self.equation)-1 and not "-" in str(self.equation.get(item)) else ""  } {"(" if "j" in str(self.equation.get(item)) else ""}{str(self.equation.get(item)).replace("-","- ")}{")" if "j" in str(self.equation.get(item)) else ""}{"*" if useSymbol else ""}{"x^" + str(item) if item not in (0,1) else "x" if item == 1  else ""} ')
            j+=1
        Joined = "".join(list(reversed(eq))).strip()
        if Joined.strip()[-1] == "*":
            Joined = Joined[:-1]
        return f'Polynomial of degree {self.degree} : {Joined}'   
    
    __repr__ = __str__

    def derivate(self,getFunction: bool = False):
        derivate = {}
        for term in self.equation:
            derivate[term-1] = (term)*self.equation.get(term)
        derivate.pop(-1)
        if not getFunction:
            return Polynomial([derivate.get(item) for item in derivate])
        return eval("lambda x : " + Polynomial(derivate).__str__(useSymbol=True).split(":")[1].strip().replace("^","**"))

    def integral(self,getFunction: bool = False):
        integral = {}
        for term in self.equation:
            integral[term+1] = round(1 / (term+1),3) * self.equation.get(term) if term !=0 else self.equation.get(term)
        if not getFunction:
            for i in range(max(list(integral))):
                if i not in integral:
                    integral[i] = 0
            returntype = list(integral)
            returntype.sort()
            return Polynomial([integral.get(item) for item in returntype])

    def __neg__(self):
        return -1 * self

    def __add__(self,value : [int,float,complex,'Polynomial']) -> 'Polynomial':
        eq_copy = self.equation.copy()
        #Scalar
        if type(value) in (int,float,complex):
            eq_copy[0] = eq_copy[0] + value if 0 in eq_copy else value
            return Polynomial([eq_copy.get(item) for item in eq_copy])
        #Polynomial
        elif type(value) == type(self):
            array_1 = [value.eq().get(item) for item in value.eq()]
            array_2 = [self.equation.get(item) for item in self.equation]
            if len(value.eq()) > len(self.eq()):
                for i in range(len(value)):
                    array_1[i] += array_2[i]
                return Polynomial(array_1)
            for i in range(len(self.eq())):
                array_2[i] += array_1[i]
            return checkPolynomial(array_2)
        raise TypeError("Cannot add Polynomial with {}".format(type(value)))

    def __sub__(self,value : [int,float,complex,'Polynomial']) -> Union['Polynomial',float]:
        eq_copy = self.equation.copy()
        #Scalar
        if type(value) in (int,float,complex):
            eq_copy[0] = eq_copy[0] - value if 0 in eq_copy else value
            return Polynomial([eq_copy.get(item) for item in eq_copy])
        elif type(value) == type(self):
            return self + (-1 * value)
        raise TypeError("Cannot perform subtraction on Polynomial with {}".format(type(value)))

    def __mul__(self,value : [int,float,complex,"Polynomial"]) -> Union['Polynomial',float]:
        if type(value) in (int,float,complex):
            return checkPolynomial([value * num for num in self.array])
        
        elif type(value) == self.type:
            dick0 = self.equation
            dick1 = value.eq()
            new_dick = {}
            for item in dick0:
                for value in dick1:
                    if not (value+item) in new_dick:
                        new_dick[value+item] = []
                    new_dick[value+item].append(dick1.get(value) * dick0.get(item))
            for num in new_dick:
                new_dick[num] = sum(new_dick[num])
            item_max = max([item for item in new_dick])
            for i in range(item_max):
                if i not in new_dick:
                    new_dick[i] = 0
            x = [item for item in new_dick]
            x.sort()
            return checkPolynomial([new_dick.get(item) for item in x])

        raise ValueError("Cannot multiply Polynomial with {}".format(type(value)))

    def __rmul__(self,value : [int,float,complex,"Polynomial"]) -> Union['Polynomial',float]:
        return self.__mul__(value)

    def __pow__(self,value : int) -> Union['Polynomial',float]:
        if not type(value) == int:
            raise TypeError("Cannot perform polynomial exponentiation with {}".format(type(value)))
        return product(*[self for i in range(value)])
    
    def __truediv__(self,value : [int,float,complex,"Polynomial"]) -> Union[float,"Polynomial"]:
        if type(value) in (int,float,complex):
            new_dict = self.equation.copy()
            for item in new_dict:
                new_dict[item] = new_dict[item] / value 
            return checkPolynomial([new_dict.get(item) for item in new_dict])
        elif type(value) == self.type:
            # x^2+2x+1  P1  
            # x+1       P2
            RESULT_DICT = []
            # NOTE Divide the term of the highest degree of the divisor (x^2)
            # NOTE with the highest term of the number you are dividing (x)

            # NOTE Mutliply the above result with the number you are dividing  x*(x+1)
            # NOTE Now subtract from the divisor the above result x^2+2x+1 - (x^2 + x)
            # NOTE Repeat the same thing with the above result
            # NOTE Keep repeating the algorithm until you are left with a constant remainder
            if self.degree < value.deg():
                raise ValueError("Cannot divide Polynomial of degree {} with one of {} (The first polynomial must have a higherdegree ({} < {})  )".format(self.degree,value.deg(),self.degree,value.deg()))
            self_copy = Polynomial(self.array.copy())
            value_copy = Polynomial(value.arr().copy())

            while self_copy.deg() !=0:
                print(self_copy)
                max_divisor_pow = max([num for num in self_copy.eq()]) #The highest power    (P1)
                max_dividand_pow = max([num for num in value_copy.eq()]) #The highest power      (P2)

                max_divisor = self_copy.eq().get(max_divisor_pow) #P1 coefficient
                max_dividand = value_copy.eq().get(max_dividand_pow)   #P2 coefficient
                div = max_divisor_pow / max_dividand_pow #Divde the degrees
                div_const = max_divisor / max_dividand #Divide the constants

                new_poly_dict = PolynomialFromDict({div : div_const}) #The division result
                RESULT_DICT[div] = div_const
                times = new_poly_dict * value #The multiplication result
                self_copy = self - times
            
            return self_copy
        raise TypeError("Cannot divide Polynomial with {}".format(type(value)))

    def roots(self,iterations : int) -> complex:
        """It returns an list of complex numbers that are it roots or are approximately very close to them
           WARNING : THIS FUNCTION IS NOT STABLE AND REQUIRES ADJUSTING (OVERFLOW ERRORS DUE TO VERY LOW NUMBERS ARE COMMON)
        """
        return applyKruger(self.function,self.degree,iterations)
    

def kerner_durand(APPROXIMATIONS,function):
    TEMP_STORAGE = []
    for value in APPROXIMATIONS:
        current = APPROXIMATIONS.get(value)
        nominator = function(current) 
        #Handle Dividing
        denominator =  [] #list of all the subtractions
        cop = APPROXIMATIONS.copy()
        cop.pop(value)
        for item in cop:
            denominator.append(current - cop.get(item)) 
        TEMP_STORAGE.append(current - nominator / product(*denominator))
    i = 0 
    for item in APPROXIMATIONS:
        APPROXIMATIONS[item] = TEMP_STORAGE[i]
        i+=1
    return APPROXIMATIONS

def checkPolynomial(pol_list : list):
    if len(pol_list) in  (pol_list.count(pol_list[0]),pol_list.count(0)):
        return pol_list[0]
    return Polynomial(pol_list)
    
def applyKruger(function : callable,degree : int,iterations : int):
    APPROXIMATIONS = {}
    #Get our starting points
    for i in range(0,degree):
        APPROXIMATIONS[i] =  random_complex() #Begin with random numbers

    INITIAL = APPROXIMATIONS.copy()
    try:
        for i in range(iterations):
            APPROXIMATIONS = kerner_durand(APPROXIMATIONS,function)
    except:
        print("Root Calclualtion Failed")
        APPROXIMATIONS = INITIAL
        applyKruger(function,degree,iterations)
    #for visual purposes
    return [APPROXIMATIONS.get(item) for item in APPROXIMATIONS]

def PolynomialFromDict(poly_dict : dict) -> Union[Polynomial,float]:
    deg_array = [item for item in poly_dict]

    for i in range(int(max(deg_array))):
        if i not in poly_dict:
            poly_dict[i] = 0 
    deg_array = [item for item in poly_dict]
    deg_array.sort()
    result_array = []
    for item in deg_array:
        x_type = poly_dict.get(item)
        if isInteger(x_type):
            result_array.append(int(x_type))
            continue
        result_array.append(x_type)
    return checkPolynomial(result_array)

def PolString(eqstring : str) -> Polynomial:
    #Check at the end of the string for constants
    eqstring = " " + re.sub(r"\s+",'',eqstring.strip()) #Remove all white space
    eqdict = {}
    exp_iteral = NUMBER_REGEX + r"?(-?x)?(\^(" + NUMBER_REGEX + r"))?"
    res = list(re.finditer(exp_iteral,eqstring))
    res = [item.group() for item in res if item.group().strip() != ""]
    for item in res:
        item = item.strip()
        if not 'x' in item: #Constants
            exponent = 0
            base = float(item)
        else:
            if '^' in item: #Power
                new_str = [x for x in item.split("x^") if x.strip() != '']
                if not item.startswith("x"):
                    base =  float(new_str[0]) if new_str[0] !='-' else -1
                    exponent = float(new_str[1])  
                else:
                    new_str_new = [x for x in item.split("^") if x.strip() !='']
                    base = float(new_str_new[0]) if new_str_new[0] != 'x' else 1
                    exponent = float(new_str_new[1]) if new_str_new[1] !='x' else 1
            else: #No Power
                if item.startswith('x'):
                    base = 1
                else:
                    replacement = item.replace("x",'')
                    if replacement.strip() =='-':
                        base = -1
                    else:
                        base = float(item.replace("x",''))
                exponent = 1
        if not exponent in eqdict:
            eqdict[exponent] = []
        eqdict[exponent].append(base)
    for expo in eqdict:
        eqdict[expo] = sum(eqdict[expo])
    return PolynomialFromDict(eqdict)

if __name__ == "__main__":
    P = PolString("x^3 - 5x^2 + 2x -1")
    x = PolString("x-3")
    y = PolString("-x + 1")
    z = PolString(" x^2 + 1")
    zz = PolString("5x^5 - 4x^4 + 3x^3 - 2x^2 + x")
    print(P)
    print(x)
    print(y)
    print(z)
    print(zz)

