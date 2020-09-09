## Pythematics

>**Pythematics** is a zero-dependency math library for Python that aims extends some Mathematical fields that are seemingly abandoned by other libraries while offering a fully **Pythonic** experience.

The main **field** that this library aims to introduce to Python is **Polynomials** in a way that allows for super-complicated and **high** degree equations to be solved giving all **Reall** and **Complex** Solutions as well as combining it with fields such as **Linear Algebra** and allowing for **Matrix**-**Polynomial** Manipulations methods like finding **Eigenvalues** and **Eigenvectors**.

**Imagine** that you want to solve a super-complex Equation like the following

> ![Complicated Equation](http://www.sciweavers.org/upload/Tex2Img_1599688663/render.png)

The only hard thing would be to write this thing...

```python
import pythematics.polynomials as pl

x = pl.x #Declare the x variable

#First Long Term
numerator0 = x**2 * (3*x**8 + 7*x**4 + 2*x**11 - 13*x**5) + 7
denominator0 = x**2 + 3*x**3 + 1

#Second Long Term
numerator1 = x**4+x**3+x**2+x 
denominator1 = x+1

side2 = x**2 + 3*x + 4 #Second side of the equation

#Get rid of the fractions
lcm_mul = LCM_POL(
    denominator0,denominator1
)

frac_0 = (numerator0 * lcm_mul) / denominator0 #First Fraction
frac_1 = (numerator1 * lcm_mul) / denominator1 #Second Fraction
side2 *= lcm_mul #Multplie the other side as well
side1 = frac_0[0] - frac_1[0] #The first side
final_polynomial = side1-side2 #Bring Everything to one side
roots = final_polynomial.roots(iterations=1000)
print(final_polynomial)
print(roots)

for root in roots: #Validate The result
    print(root) #Print the number
    func_root = final_polynomial.getFunction()(root) #Substitute the root into the Polynomial function
    print(func_root)
    print("\n")
```
And in just a few **mili-seconds** We are able to get the following results from our calculations but **NOTE** : Here we are dealing with a **14th** Degree Polynomial and we are trying to find all it's roots so to be safe we increased the iterations to **1000** to get an accurate result even though the results are also as accurate at **300** iterations

Every single Result is a complex number that looks something like this `(1.032132131e-14+3.312312e-15)` which means it's that number raised to the **-14th** Power which is ultimately very close to zero


The output was so long that it did not fit into the screen so check [here](#todo) for the Outputs

