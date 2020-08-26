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
    Matrices shall be passed in the following format :

    [   c1  c2 c3 c4
     #R1 [1, 2, 3,  4],
     #R2 [3, 5, 5,  3],
     #R3 [3, 4, 5,  6],
     #R4 [4, 5, 6,  4]
        
    ]
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
                        raise TypeError("Row : {} , does not contain an argument or {} or {} but instead {}!".format(matrix.index(row),type(1),type(1.0),type(num)))
            else:
                raise ValueError("Every argument inside the basic array which is considered as a row should be of type {}".format(type([])))
        if len(ROW_LENGTHS) != ROW_LENGTHS.count(ROW_LENGTHS[0]):
            raise ValueError("All rows of a matrix shall only be of same size.")

        self.matrix = matrix
        self.rows = len(self.matrix)
        self.collumns = ROW_LENGTHS[0]

        self.cols = []
        for j in range(ROW_LENGTHS[0]):
            self.cols.append([])

        for row in self.matrix:
            for value in row:
                self.cols[row.index(value)].append(value)
    
    def rawMatrix(self):
        return self.matrix

    def colls(self,index):
        return self.cols[index]

    def collsAll(self):
        return self.cols

    def row(self,index):
        return self.matrix[index]

    def printRaw(self):
        return str(self.matrix).replace(",","\t").replace("]","]\n").replace("[[","[\n\t [")

    def __len__(self):
        """Returns a tuple containng number of rows and collumns (rows,collumns)"""
        return (self.rows,self.collumns) # (number of rows,number of collumns)

    def __str__(self):
        """Returns a visual representation of the Matrix"""
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

    def __rmul__(self,scalar):
        """Matrix multiplication by scalar"""
        if type(scalar) in (int,float):
            new_matrix = [[] for i in range(self.rows)] #Add the rows
            for row in self.matrix:
                for constant in row:
                    new_matrix[self.matrix.index(row)].append(constant * scalar)
            return Matrix(new_matrix)
        else:
            raise TypeError("You may only multiply a {} object with either a {} or a {}".format(type(self),int,float))

    def __neg__(self):
        return (-1) * self
    
    def __add__(self,Matrx):
        if type(Matrx) != type(self):
            raise ValueError("A Matrix may only be added with another Matrix not {}!".format(type(Matrx)))
        if self.__len__() != Matrx.__len__():
            raise ValueError("Rows and Collumns must be equal! {} != {}".format(self.__len__(),Matrx.__len__()))
        new_matrix = [[] for row in range(self.rows)]
        for row in self.matrix:
            for num in row:
                new_matrix[self.matrix.index(row)].append(num+Matrx.rawMatrix()[self.matrix.index(row)][row.index(num)])
        return Matrix(new_matrix)

    def __sub__(self,Matrx):
        if type(Matrx) != type(self):
            raise ValueError("A Matrix may only be added with another Matrix not {}!".format(type(Matrx)))
        if self.__len__() != Matrx.__len__():
            raise ValueError("Rows and Collumns must be equal! {} != {}".format(self.__len__(),Matrx.__len__()))
        new_matrix = [[] for row in range(self.rows)]
        for row in self.matrix:
            for num in row:
                new_matrix[self.matrix.index(row)].append(num-Matrx.rawMatrix()[self.matrix.index(row)][row.index(num)])
        return Matrix(new_matrix)

    def __mul__(self,value):
        row_0 = self.__len__()
        col_0 = value.__len__()
        if row_0[1] != col_0[0]:
            raise ValueError(f"\nCannot multiply a {row_0[0]} x {row_0[1]} with a {col_0[0]} x {col_0[0]} Matrix,\nMatrix 1 must have the same number of rows as the number of collumns in Matrix 2 \n({row_0[1]} != {col_0[0]})")
        new_matrix = [[] for i in range(row_0[0])]
        COLS_M2 = value.collsAll()
        print(new_matrix)
        for row in self.matrix:
            num_row = self.matrix.index(row)
            CACHE = []
            for number in row:
                index = row.index(number)
                CACHE.append(number * COLS_M2[num_row])
        
        return row_0,col_0

if __name__ == "__main__":
    A = Matrix([
            [436,9,10,11,7], #Number of row
            [437,9,10,11,3],
            [438,9,10,11,4],
            [430,9,10,11,5],
            [434,9,10,11,6],
            [453,93,16,15,64],
            ])
    B = Matrix([
        [3,4,5,6],
        [8,9,10,11]
    ])

    C = Matrix([
        [3],
        [4],
        [5],
        [6]
    ])

    print(B*C)