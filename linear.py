from basic import isNumber
from typing import Union

class Vector:
    def __init__(self,array):
        for item in array:
            if not isNumber(item):
                raise ValueError("Vector arguments must be a list of integers not {}".format(type(item)))
        self.matrix = array
        self.rows = len(self.matrix)
        self.collumns = 1

    def __str__(self):
        s1 =  str(self.matrix).replace(",",",\n").replace("]","\n]").replace("[","[\n ")
        s2 = "\n {} x {} Vector array".format(self.rows,self.collumns)
        return s1 + s2

    def getMatrix(self):
        return self.matrix

    def getSize(self):
        return self.rows

    def __add__(self,value):
        empty = []
        if isNumber(value): #Scalar
            for item in self.matrix:
                empty.append(value+item)
            return Vector(empty)

        # Vector addition

        elif type(value == Vector):
            if value.getSize() != self.getSize():
                raise ValueError("Cannot multiply non equal-size collumns ({} with {})".format(value.getSize(),self.getSize()))
            for i in range(self.getSize()):
                empty.append(value.getMatrix()[i] + self.getMatrix()[i])
            return Vector(empty)

    def __sub__(self,value):
        empty = []
        if type(value) == type(self):
            if value.getSize() != self.getSize():
                raise ValueError("Cannot multiply non equal-size collumns ({} with {})".format(value.getSize(),self.getSize()))
            for i in range(self.getSize()):
                empty.append(value.getMatrix()[i] - self.getMatrix()[i])
            return Vector(empty)
        else:
            raise ValueError("Cannot Perform subtraction : {} with {}".format(type(self),type(value)))


    def __mul__(self,value):
        """Vector Multiplication by scalar
            if other value is Vector,
            the dot product is returned
        """
        empty = []
        if isNumber(value): #Scalar
            for item in self.matrix:
                empty.append(value*item)
            return Vector(empty)
        elif type(value) == type(self):
            if value.getSize() != self.getSize():
                raise ValueError("Cannot multiply non equal-size collumns ({} with {})".format(value.getSize(),self.getSize()))
            for num in range(self.getSize()):
                empty.append(value.getMatrix()[num] * self.getMatrix()[num])
            return sum(empty)
        else:
            raise ValueError("Cannot Multiply {} with {}".format(type(self),type(value)))

    def dot(self,Vector) -> Union[float,int]:
        return self.__mul__(Vector) 
    
    # def cross(self,Vector)


class Matrix:
    """
    [[1,2,3,4,5],[3,5,5,3],[3,4,5,6],[4,5,6,4]]
    """
    def __init__(self,matrix):
        """Takes an array of arrays of numbers
            The arrays inside the array as seen as the rows
        """
        if type(matrix) != list:
            raise ValueError("Matrix must be an array of arrays.")
        
        ROW_LENGTHS = []

        for row in matrix:
            if type(row) == list:
                ROW_LENGTHS.append(len(row))
                for num in row:
                    if not isNumber(num):
                        raise ValueError("Row : {} , does not contain an argument or {} or {} but instead {}!".format(matrix.index(row),type(1),type(1.0),type(num)))
            else:
                raise ValueError("Every argument inside the basic array which is considered as a row should be of type {}".format(type([])))
        if len(ROW_LENGTHS) != ROW_LENGTHS.count(ROW_LENGTHS[0]):
            raise ValueError("All rows of a matrix shall only be of same size.")

        self.matrix = matrix
        self.rows = len(self.matrix)
        self.collumns = ROW_LENGTHS[0]
    
    def __str__(self):
        import itertools
        x = self.matrix
        y = []
        yy = []
        for iteration in range(self.collumns):
            y.append(f"\tC{iteration+1}")
            yy.append("\t__")
        print("".join(y))
        print("".join(yy))
        j = 1
        for item in x:
            if j > 9:
                print("\n   .........")
                print(f' R{len(x)}|',*x[-1])
                break
            item[0] = f'\t{item[0]}'
            print(f' R{j}|',"\t".join(str(val) for val in item))
            j+=1
        return f'\n{self.rows} x {self.collumns} Matrix'

A = Matrix([
           [43,9,10,11,7],
           [43,9,10,11,3],
           [43,9,10,11,4],
           [43,9,10,11,5],
           [43,9,10,11,6],
           [43,9,10,11,7],
           [43,9,10,11,7],
           [43,9,10,11,7],

           ])

print(A)