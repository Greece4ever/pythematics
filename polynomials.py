#Relative imports
from .random import random_complex;from .basic import isNumber;from .basic import product; 
#Built-in imports
from typing import Union
import re

NUMBER_REGEX = r"^((\-)|(\+))?\d+((\.)\d+)?"

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

def PolString(eqstring : str) -> Polynomial:
    eqstring = " " + re.sub(r"\s+",'',eqstring.strip())
    print(eqstring)
    eqdict = {}
    iterations = len(eqstring)
    print("MAX ITERATIONS : {}".format(iterations))
    i = 0 
    while i < iterations:
        base = None
        expo = None
    # for term in eqstring:
        if eqstring[i] == "x":
            index = i;substring1 = eqstring[:index];substring2 = eqstring[index:]
            try:
                if eqstring[i+1] == '^':
                    expo = re.search(r"((\-)|(\+))?\d+((\.)\d+)?",substring2).group()
            except:
                pass

            base =  list(re.finditer(NUMBER_REGEX,substring1)) #last match
            if not len(base) < 1:
                print("nope")
                base = base[-1].group()
            else:
                if (i-1) > -1:
                    print(eqstring[i-1])
                    print(eqstring)
                    if eqstring[i-1] in (" ","+","-") :
                        for j in list(reversed(eqstring[:i])):
                            if isNumber(j):
                                raise SyntaxError("Passed a number with no operator")
                            
                            if j == "+":
                                base = 1
                                break
                            
                            if j == "-":
                                base = -1
                                break
                        else:
                            base = 1             
                        base = 1 # index out of range
            if expo is None:
                expo = 1

        if base is not None:
            if not int(expo) in eqdict:
                eqdict[int(expo)] = [] 
            eqdict[int(expo)].append(base)
                    
        i+=1
    print(eqdict)



if __name__ == "__main__":
    p = Polynomial([7,-5,3])
    f = Polynomial([-4,6,2])
    print(PolString(("  2x^2  +  3x^4   - 4x^3 +   ")))