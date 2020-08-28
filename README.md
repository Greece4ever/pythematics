## Pythematics

Pythematics is a **zero-dependency** python math library written from scratch, that  aims to extend the built-in one, by using modern *Python* function indications and introducing some other mathematical concepts such as :

- Complex Numbers
- Linear Algebra
- Number Theory

Every function from `pow` to more advanced functions such as `erfi` has been refactored in modern Python

To be more specific here is the list of all sub-modules (the names describe what they do)

- **```basic.py```** For basic operations
- **```trigonometric.py```** For trigonometric related things
- **```linear.py```** For linear algebra stuff
- **```powers.py```** For exponentiation and that type of thing
- **```functions.py```** Famous functions that have no specific category
- **```constants.py```** Keeps some constants in storage


|  You can easily install **pythematics** using pip

```
pip install pythematics 
```
## Basic functions

This includes all the functions of `pythematics.basic` which are simple and can be quite usefull

 - Verification

```python
from pythematics.basic import *

def isNumber(arg) -> bool: ... #Verifies wheter an argument can be converted to a floating number

def isInteger(num : Union[float,int]) -> bool:... #Checks if a number is an integer

#Given a function and an two points x_0 x_1) it checks whether that function has a root in that interval
def isRoot(function : callable,x_0 : float,x_1 : float) -> bool:

# Samples

# isNumber()
>>> isNumber(3)
>>> True

>>> isNumber('5')
>>> True

# isInteger()
>>> isInteger('5.00')
>>> True

>>> isInteger(5)
>>> True

# isRoot

def f(x):
   return x+1

>>> isRoot(f,-2,3) # (-2,3) There exists one at -1
>>> True

```
- Readability
```python
from pythematics.basic import comaSplitNumber

#Given a large number it returns a human readable string inserting commas (,) every 3 places
def comaSplitNumber(num : Union[int,float]) -> str: 

>>> comaSplitNumber(100000)
>>> '100,000'
```
## General functions
Here are some general mathematical functions that are popular and have no special category

```python
""" 
 These function have either no special meaning or are not referencing something specifically,
 it's just a collection of popular math functions
"""
from pythematics.functions import *

# The exponential function which can either be calculated using Taylor series or an aproximation of e
def exp(x : float,iterations : int = 100,taylor_exapnsion=False) -> float: ...

# The natural log function which has been extended to allow negative and complex nubmers
def ln(x : float,iterations : int = 100) -> Union[float,complex]:

#A generilization of the above function with custom base
def log(of_num : float,base : float = 10) -> float: ...

# Quadratic and Linear equation solver that returns complex roots
def quadratic(a,b,c) -> Union[Tuple[complex],Tuple[float]]: ...

# A shorthand for cos(x) + i*sin(x)
def cis(x : float) -> complex:

# The error function and it's complex equivalant
def erf(x : float) -> float: ...
def erfi(x : float) -> float: ...

# Factorials (Here is the only external depedency on the built-in LRU_CACHE from functools
@lru_cache(maxsize=1000)
def factorial(n : int) -> int: ... #returns the factorial of a number

@lru_cache(maxsize=1000)
def doubleFactorial(n : int) -> int: ... #returns the double factorial )

# and of course the other recursive function

@lru_cache(maxsize=1000)
def fibonacci(n : int) -> int:


# Complex Counter-Parts

>>> ln(-1)
>>> 3.141592653589793j #Complex number with imaginary part equal to pi (see function for how it computes)

>>> ln(complex(0,1))
>>> 3.141592653589793j #Complex number with imaginary part equal to pi (see function how it computes)

>>> ln(complex(1,1) # Also check the function definition for more info for these computations
>>> (0.34657359027997253+0.7853981633974481j)

```

## Exponentiation and subroots

This includes new versions of the `pow` and `sqrt` functions, written from scratch generalizing them operate with complex numbers

```python
import * from pythematics.powers

def power(base : Union[float,complex],exponent : Union[float,complex]) -> Union[float,complex]: ...
#This is a function for computing powers-exponentiation
# You can pass a  base or exponent any integer or floating point value
# And in addition you can also pass any complex number
# Too see why this works you can see the definition

def sqrt(x : float,iterations : int = 100,catchNegativeRoot=False) -> Union[float,complex]:
# This function computes square roots, using Newton's method
# You can specify whether you want to get complex numbers or throw an exception
# Whenver x is negative

def nthRoot(subroot : float,n : int,iterations : int = 100,catchNegativeRoot=False) -> float:
# This is a generilization of the above function
# You can also specify for even roots wheter you want complex numbers

# 3 Ways to compute the square root of 9
>>> power(9,0.5)
>>> 3.0
>>> nthRoot(9,2)
>>> 3.0
>>> sqrt(9)
>>> 3.0

# And with complex numbers

>>> power(complex(3,1),2) # Works normally as an integer or a float
>>> (8+6j)

>>> power(2,complex(3,1)) #Here it treates complex exponents specially
>>> (8.638961276313635+0.7692389013639723j)
```
## Number theory

In this sub-module you can find operations that are commonly found in Number theory

```python
from pythematics.num_theory import *

# Here are the Unique operations

def GCD(*nums : int) -> int: # Returns the Greatest Common Divisor among a series of numbers

def LCM(*args: Union[int, list]) -> int: # Returns the Least Common Multiple among a list of numbers

>>> LCM(25,50,75)
>>> 150 # The smallest number that can be divded by all three numbers above

>>> GCD(25,50,75)
>>> 25 # The Greatest number that can divide all these numbers equally
```

## Trigonometry

This script includes all the trignometric, inverse trigonometric hyperbolic and inverse hyperbolic functions

Everything here is computed once using a Taylor series and then some kind of formula is used for simplicity

You can specify wheter you want to use radians or degrees by adjusting the `degrees` parameter

+ In `Trigonometric` it adjusts the output in degrees
+ In `Inverse Trigonometric` it tells the function that you have enter degrees

of course there are the 2 built in functions for radian and degree conversions

```python
from pythematics.constants import pi #For working with radians

def toRad(degrees : float) -> float:... # Degrees to radians
def toDegrees(rad : float) -> float: #Radians to degrees
```

**Trigonometric** (These may be either floating point , integer or complex numbers)

- `sin(x)`
- `cos(x)`
- `tan(x)`
- `cot(x)`
- `sec(x)`
- `csc(x)`

**Inverse Trigonometric** (Only real numbers can be computed accurattelly)
- `arcsin(x)`
- `arccos(x)`
- `arctan(x)`
- `arccot(x)`
- `arcsec(x)`
- `arccsc(x)`  

**Hyperbolic Trigonometric** (Real and Complex numbers)
- `sinh(x)`
- `cosh(x)`
- `tanh(x)`
- `coth(x)`
- `csch(x)`
- `sech(x)`

**Inverse Hyperbolic** (Only real to ensure accuraccy)
- `arsinh(x)`
- `arcosh(x)`
- `artanh(x)`
- `arcoth(x)`
- `arcsch(x)`
- `arsech(x)`

## Linear Algebra

This submodule utilizes Vector and Matrix manipulation by creating the `Vector` and `Matrix` classes

To create a matrix you pass into the constructor an array of arrays in the following way:

```python
from pythematics.linear import *

# Matrix (Array of arrays)
A = Matrix([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

# Vector (Array of numbers)
a = Vector([
    1,
    2,
    3
])
```
This is the Output

```
#The Matrix

 CI |   C1       C2      C3
 R1 |   1         2       3
 R2 |   4         5       6
 R3 |   7         8       9

3 x 3 Matrix

# The Vector

R1|   1
R2|   2
R3|   3

3 x 1 Vector array
```
You can do any Vector operation that you want

```python
# Scalar multiplication     /
3* Vector([1,2,3])
# Vector Addition
Vector([5,6,7,8]) + Vector([3,4,5,6])
# Vector Subtraction
Vector([5,6,7,8]) - Vector([3,4,5,6])
```
- Scalar Multiplication
```
R1|   3
R2|   6
R3|   9

3 x 1 Vector array
```
- Vector Addition
```
R1|   8
R2|  10
R3|  12
R4|  14
```
- Vector Subtraction
```
R1|  -2
R2|  -2
R3|  -2
R4|  -2
```

By default when multiplying 2 Vectors together you taking their dot product
```python
>>> Vector([5,6,7,8]) * Vector([3,4,5,6])
>>> 122
```

But you can also take the cross product of two vectors by calling the Built-in function
```python
w =  Vector([5,6,7]) 
v = Vector([3,4,5])
print(cross(v,w))
```

```
R1|  -2
R2|   4
R3|  -2

3 x 1 Vector array
```
You can also perform The same operations on Matrix :
 - Addition
 - Subtraction
 - Multiplication

```python
A = Matrix([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

addition = A+A
subtraction = A-A
multiplication = A*A

print(addition,subtraction,multiplication)
```

```
 #Addition

 CI |   C1       C2      C3
 R1 |   2         4       6
 R2 |   8        10      12
 R3 |   14       16      18

3 x 3 Matrix

 #Subtraction

 CI |   C1       C2      C3
 R1 |   0         0       0
 R2 |   0         0       0
 R3 |   0         0       0

3 x 3 Matrix

 #Multiplication

 CI |   C1       C2      C3
 R1 |   30       36      42
 R2 |   66       81      96
 R3 |   102     126     150

3 x 3 Matrix
```
You can also perform the following operations on matrices :
- **Trace**
- **Identity Matrix Generator**
- **Determinant**
- **Inverse Matrix**
  - **Cofactors**
  - **Adjugate (transpose)**
  - **Minors**

## Other Operations

For more details and other methods, you can delve deeper into this library using the built-in `dir()`,
which not only will provide you extra methods but will document and tell you how they are computed
