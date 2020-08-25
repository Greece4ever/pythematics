from typing import Union

def product(*args : Union[float,int]) -> Union[float,int]:
    """Returns the product of float or ints
        product(3,4,5) -> 60
        product(*[3,4,5]) -> 60
    """
    prod = 1
    for num in args:
        prod*=num
    return prod

def comaSplitNumber(num : Union[int,float]) -> str:
    """Given an integer or a floating number it returns
       a human readable string splitting the digits with commas
       example :
       input(1000) -> 1,000
       input(10000) -> 10,000
       input(1000.324) -> 1,000.324
    """
    num = str(num)
    oper_num = num.split('.')
    DIGITS = []
    iteration = 1
    for digit in reversed(oper_num[0]):
        DIGITS.append(digit)
        if(iteration%3==0):
            DIGITS.append(',')
        iteration+=1
    return_type = "".join(reversed(DIGITS))
    if(return_type.startswith(',')):
        return_type = return_type[1:len(return_type)]
    if (len(oper_num) > 1):
        return_type+=return_type[-1]
    return return_type


