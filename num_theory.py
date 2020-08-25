from basic import product
from typing import Union

def isEven(num : int) -> bool:
    return num%2==0

def isOdd(num : int) -> bool:
    return not isEven(num)

def isPrime(num : int) -> bool:
    for i in range(2,int(1+num**(1/2))):
        if(num%i==0):
            return False
    return True

def GCD(*args : int) -> int:
    # num1 // num2
    # num1%num2
    pass


def LCM(*args: Union[str, list]) -> int:
    args = args[0] if len(args) == 1 else args

    # if the input is one number the outpout is the same number
    if (type(args) == int):
        return args

    state = {}
    nums = []

    # Create an Object keeping track of their state
    for item in args:
        state[item] = item

    def validState():
        """Checks if the object is in final format"""
        for item in state:
            if state[item] != 1:
                return False
        return True

    k = 1
    DIVISORS = []

    # Continue too loop through prime numbers while the state is not True
    while not validState():

        isAppended = False
        DIVISORS = []

        # Skip if not prime
        if not isPrime(k):
            k += 1
            continue

        for item in state:
            num = state[item]

            if num == 1:
                # Instance of object is in its final form
                DIVISORS.append(False)
                continue

            # when num is divisible by k we append k to nums[] and reduce the state
            if num % k == 0:
                state[item] = num / k  # State is reduced by k
                DIVISORS.append(True)
                if not isAppended:
                    nums.append(k)
                    isAppended = True
            else:
                DIVISORS.append(False)
        if not True in DIVISORS:
            k += 1
    return product(*nums)

def main():
    print(LCM(3,4,5))


if __name__ == "__main__": 
    main()