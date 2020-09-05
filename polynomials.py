from .basic import product
from .random import random_complex

class Polynomial:
    def __init__(self,coefficients : list):
        degrees = {}
        i = 0
        for coefficient in coefficients:
            if coefficient < 0:
                raise ValueError("Cannot continue sequence for decimal Polynomial coefficent")
            degrees[i] = coefficient
            i+=1
        self.degree = i-1
        self.equation = degrees
        self.function = eval("lambda x :" + self.__str__(useSymbol=True).split(":")[1].strip().replace("^","**"))

    def __str__(self,useSymbol : bool = False):
        eq = []
        j = 0
        for item in self.equation:  
            if self.equation.get(item) == 0:
                continue
            eq.append(f' {self.equation.get(item)}{"*" if useSymbol else ""}{"x^" + str(item) if item not in (0,1) else "x" if item == 1  else ""} ' + f'{"+" if j != 0 else ""}')
            j+=1
        Joined = "".join(list(reversed(eq))).strip()
        if Joined.strip()[-1] == "*":
            Joined = Joined[:-1]
        return f'Polynomial of degree {self.degree} : {Joined}'   
    
    __repr__ = __str__

    def getFunction(self):
        return self.function

    def derivate(self,getFunction: bool = False):
        derivate = {}
        for term in self.equation:
            derivate[term-1] = (term)*self.equation.get(term)
        derivate.pop(-1)
        if not getFunction:
            return Polynomial([derivate.get(item) for item in derivate])
        return eval("lambda x : " + Polynomial(derivate).__str__(useSymbol=True).split(":")[1].strip().replace("^","**"))

    def integrate(self,getFunction: bool = False):
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

    def __add__(self,value : [int,float,complex,'Polynomial']) -> 'Polynomial':
        eq_copy = self.equation.copy()
        #Scalar
        if type(value) in (int,float,complex):
            eq_copy[0] = eq_copy[0] + value if 0 in eq_copy else value 
            return Polynomial
        #Polynomial
        else:
            choices = [value.equation.copy(),self.equation.copy()]
            max_element = max(choices)
            choices.pop(max_element)
            for i in range(len(max_element)):
                max_element[i] += choices[0]
            return Polynomial([item for item in max_element])


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


if __name__ == "__main__":
    # def f(x):
    #     return x**4+x**3+x**2+x

    P = Polynomial([3,4,5])
    print(P)
