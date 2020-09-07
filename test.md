You can easily work with Polynomials via the `polynomials.py` module

Here you use polynomials as per their default definition :
> In mathematics, a polynomial is an expression consisting of variables (also called indeterminates) and coefficients, that involves only the operations of addition, subtraction, multiplication, and non-negative integer exponentiation of variables (Wikipedia forgot division).

- Assuming that you do not re-define `x` you can simple use this all for you operations

```python
import pythematics.polynomials as pl

x = pl.x #You define the 'x' variable
P = 3*x+1
```
This would give the following output aimed at visualiazation:

```
Polynomial of degree 1 : 3x + 1
```

### Getting down to the interesting stuff

- The following 2 examples will explain all the operations while solving 2 equations

Let's consider the Following 2 algebraic equations : 
- **First** Degree 

>![First equation](http://www.sciweavers.org/upload/Tex2Img_1599431327/render.png)

- **Uknown** as of now Degree (*Polynomial Division*)

>![Second Equation](http://www.sciweavers.org/upload/Tex2Img_1599431677/render.png)

- The first One would be expressed as such 

```python
import pythematics.polynomials as pl
x = pl.x

term_0 = - (x / 2)
term_1 = (x+3) / 3
side_0 = term_0 + term_1 #The first side of our equation
side_1 = x + 1 # The second one
final_polynomial = side_0 - side_1 #Bring everything to one side
```
This is how the steps are gone

```
Polynomial of degree 1 : - 0.5x // term_0
Polynomial of degree 1 : 0.3333333333333333x + 1 //term_1
Polynomial of degree 1 : - 0.16666666666666669x + 1 // -0.16*x + 1 = x + 1
```
And thus the result is the difference of the 2 sides `side_0 - side_1 = 0` :
```
Polynomial of degree 1 : - 1.1666666666666667x 
```
Of course the root here is easy to find and it's zero, but what do you do in a different situation?

- Consider the second example

Here we can see 2 fractions that are both being divided by a Polynomial

- You could try doing Polynomial division in the first expression but you would end up doing nothing helpful
- In the second expression you can't do anything

Here is where `LCM` (Least common multiple) comes in handy (The equivalant of LCM in `num_theory.py`)
```python
#Find the LCM of x+1 and x
pol_lcm = LCM_POL(
    x+1,x
)

 # we multiply everything by pol_lcm
term0 = (x * pol_lcm) / (x+1)
term1 = (8 * pol_lcm) / (x)
s0 = term0[0] - term1[0] #We are performing polynomial division which gives (Output,Remainder)
s1 = pol_lcm * 1 #Do not forget to multiple the next side as well
final_polynomial = s0-s1 #Move everthing to one side
```
Now one way to get the root of this equation is by using  **Newton's method**

```python
from pythematics.functions import NewtonMethod

f_p_function = final_polynomial.getFunction() #Aquire the function of the pol (callabe)
root_0 = NewtonMethod(f_p_function,2,iterations=50) #Use 50 iterations to approximate and a start point
```
The output is `-0.888888888888889` which infact is the only root of this equation

Some things ought to be explained here in more depth:

#### What's going on during the division step?

> s0 = term0[0] - term1[0]

Here we are using indexes because the actual output is a list containing The result and remainder of the division 
```python
print(term1)

>> [Polynomial of degree 1 : 8x + 8, 0] # Polynomial in 0 index and remainder in 1
```

The remainder can either be another Polynomial or a scalar value : `int`,`float` or even `complex`

In this case the `LCM_POL` which represents the LCM multiple of these polynomials:

> **Finds the smallest Polynomial that can equally be devided by all of these Polynomials**

In **every** case the division will have a remainder of 0 , so it is safe to always use the 0th term

#### Why use Newton's method? How does it even work? What else is there to use?

## Finding roots of functions

By definition **Newton's** method is described as : (The same algorithm is used in most other methods)

> In numerical analysis, Newton's method, also known as the Newton–Raphson method, named after Isaac Newton and Joseph Raphson, is a root-finding algorithm which produces successively better approximations to the roots (or zeroes) of a real-valued function (using fixed point iteration). - Wikipedia

You begin with a starting point `starting_point : Union[float,int]` and each time You solve the linear equation of the slope of function getting closer each time (finding the derivative of the function)

Another alternative for real roots it the **Secant** Method which does the same but with 2 points

```python
final_polynomial = s0-s1
f_p_function = final_polynomial.getFunction()
root_0 = SecantMethod(f_p_function,1,2,2) #We choose Points 1 and 2 and we Iterate 2 times
print(root_0)
```
This outputs `-0.8888888888888888` as well but with only 2 iterations and no derivative computation

The secant method works needs few iterations to find the result and because it converges very fast this will cause `ZeroDivisionError` errors at event few iterations more than normal 

The number we chose was `2`, at the very next number `3` it causes an Error

```
ZeroDivisionError: float division by zero
```

Perhaps the most **powerful** but hard to get working method is the **Durand–Kerner** method which gives all complex roots of Polynomial equations (On the other hand Newton and Secant work on non-polynomial equations)

Let's consider the following Polynomial

```python
P = x**2 - 8*x - 9 #You can generate this using s0-1 from the equation example
```
To get all of it's roots we can apply the above method as follows

```python
roots = P.roots(iterations=50)
print(roots)
#or if you wish by the functional method
roots = applyKruger(final_polynomial.getFunction(),final_polynomial.degree,50)
print(roots)
```
The output in both cases is exatctly the same

```python
[(-1+0j), (9+0j)] # A list of complex numbers which are the roots (Generated in iteration 10)
[(-0.9999999869391464-4.333046649490722e-08j), (8.999999986939148+4.33304664947988e-08j)] #Iteration 9
```
This method also requires some starting points but they are automatically generated completely randomly   

This method will either work fine at low iterations giving all complex roots or may never work

> REMAINDER : **Durand-Kerner** is for polynomials only

## Delving deeper into Polynomials (Errors you might cause)

As of now all Polynomial arithimtic was defined using `x = pl.x ` and normal operations giving it a nice Pythonic feeling, but that is not how the system interprets it and there are some other methods to declare an instance of Pol

```python
P = Polynomial([3,4,1]) #The Class method of doing it which explains how everything works
G = PolString("x^2 + 4x + 3") #The string method of doing it
#In fact pl.x is just the following
x = PolString("x") #or
x = Polynomial([0,1])
```
This would output the following Polynomial
```
Polynomial of degree 2 : 1x^2 + 4x + 3 #P and G
Polynomial of degree 1 : + 1x #x
```

Despite the existance of the functions `derivative` and `integral` in **functions.py** which work at all cases perfectly they do not actually provide an observable and visualizable formula and to achive this you can use the `.diffrentiate` and `.integrate` methods for Polynomials

```
P = Polynomial([3,4,1])
print(P.diffrentiate()) #Polynomial of degree 1 : 2x + 4 
print(P.integrate()) #Polynomial of degree 3 : + 0.333x^3 + 2x^2 + 3x
```

As a remainder you can use `polynomial.getFunction()` to get a callabe of the corresponding polynomial
