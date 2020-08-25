from basic import product

def isEven(num : int) -> bool:
    return num%2==0

def isOdd(num : int) -> bool:
    return not isEven(num)

def isPrime(num : int) -> bool:
    for i in range(2,int(1+num**(1/2))):
        if(num%i==0):
            return True
    return False

def LCM(*args: int) -> int:
    """
    Takes as input arguments either a list of POSITIVE integers or POSITIVE integers LCM(int1,int2,int3...) or LCM([int1,int2,int3...])
    Returns the least common multiple of n numbers
        Follows Euclid's algorithm that goes like this:
            => Store the state of the numbers in a format like this
                {
                    num1 : num1,
                    num2 : num2
                    ...
                }
            Now we create a loop that we keep until the values of num(i) are all 1.0 (we divide them with prime numbers in that while loop)
            => Perform % (modulo) => num(i) % prime_number
                - Where prime_number is a number that is selected from the loop
                - if modulo == 0 store that prime_number in a list
            => Finally when all Values are 1:
                => return the product of the prime_numbers

    Exampels :
        LCM(1,2,3)
        PROCCESS :
            <--------------->
            2 % 2 == 0
            3 % 2 == 1
            <--------------->
            3 % 2 == 1
            <--------------->
            3 % 3 == 0
        ITERATIONS : 3
        OUTPUT : 6

    """
    args = args[0] if len(args) == 1 else args

    # if the input is one number the outpout is the same number
    if (type(args) == int):
        return args

    print(args)
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
    return product(nums)


def main():
    print(LCM(50,35,12))


if __name__ == "__main__": 
    main()