from basic import isNumber
from typing import Union

class Vector:
    def __init__(self,array):
        for item in array:
            if not isNumber(item):
                raise ValueError("Vector arguments must be a list of {} or {} not {}".format(int,float,type(item)))
        self.matrix = array
        self.rows = len(self.matrix)
        self.collumns = 1

    def __str__(self):
        s1 =  str(self.matrix).replace(",",",\n").replace("]","\n]").replace("[","[\n ")
        s2 = "\n {} x {} Vector array\n".format(self.rows,self.collumns)
        return s1 + s2

    def getMatrix(self):
        return self.matrix

    def getSize(self):
        return self.rows

    def __add__(self,value):
        empty = []
        if type(value) == Vector:
            if value.getSize() != self.getSize():
                raise ValueError("Cannot multiply non equal-size collumns ({} with {})".format(value.getSize(),self.getSize()))
            for i in range(self.getSize()):
                empty.append(value.getMatrix()[i] + self.getMatrix()[i])
            return Vector(empty)
        raise TypeError("Cannot perform addition on Vector with {}".format(type(value)))

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

    def __len__(self):
        return self.rows

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

    def __rmul__(self,scalar : Union[int,float]):
        if type(scalar) in (int,float):
            return self.__mul__(scalar)
        raise TypeError("Cannot perform '*' operation on Vector with {}")

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
        
        self.ROW_LENGTHS = []

        for row in matrix:
            if type(row) == list:
                self.ROW_LENGTHS.append(len(row))
                for num in row:
                    if not isNumber(num):
                        raise TypeError("Row : {} , does not contain an argument or {} or {} but instead {}!".format(matrix.index(row),type(1),type(1.0),type(num)))
            else:
                raise ValueError("Every argument inside the basic array which is considered as a row should be of type {}".format(type([])))
        if len(self.ROW_LENGTHS) != self.ROW_LENGTHS.count(self.ROW_LENGTHS[0]):
            raise ValueError("All rows of a matrix shall only be of same size. not {}".format(self.ROW_LENGTHS))

        self.matrix = matrix
        self.rows = len(self.matrix)
        self.collumns = self.ROW_LENGTHS[0]
        self.isSquare = self.rows == self.collumns

        self.cols = []
        for j in range(self.ROW_LENGTHS[0]):
            self.cols.append([])

        for row in self.matrix:
            i = 0
            for value in row:
                self.cols[i].append(value)
                i+=1

    def rawMatrix(self):
        return self.matrix

    def colls(self,index):
        return self.cols[index]
    
    def is_square(self):
        return self.isSquare

    def collsAll(self):
        return self.cols

    def row(self,index):
        return self.matrix[index]

    def __len__(self):
        """Returns a tuple containng number of rows and collumns (rows,collumns)"""
        return (self.rows,self.collumns) # (number of rows,number of collumns)

    def __str__(self):
        """Returns a visual representation of the Matrix"""
        x = [item[:] for item in self.matrix]
        y = []
        yy = []
        for iteration in range(self.collumns):
            y.append(f"\tC{iteration+1}")
            yy.append("\t__")
        print("".join(y))
        # print("".join(yy))
        j = 1
        for item in x:
            if j > 9:
                print("\n   .........")
                print(f' R{len(x)}|',*x[-1])
                break
            item[0] = f'\t{item[0]}'
            print(f' R{j}|',"\t".join(str(val) for val in item))
            j+=1
        return f'\n{self.rows} x {self.collumns} Matrix\n'

    def __rmul__(self,scalar):
        """Matrix multiplication by scalar"""
        if type(scalar) in (int,float):
            new_matrix = [[] for i in range(self.rows)] #Add the rows
            i = 0
            for row in self.matrix:
                for constant in row:
                    new_matrix[i].append(constant * scalar)
                i+=1
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
        i = 0
        for row in self.matrix:
            k = 0 
            for num in row:
                new_matrix[i].append(num+Matrx.rawMatrix()[i][k])
                k +=1
            i+=1
        return Matrix(new_matrix)

    def __sub__(self,Matrx):
        if type(Matrx) != type(self):
            raise ValueError("A Matrix may only be added with another Matrix not {}!".format(type(Matrx)))
        if self.__len__() != Matrx.__len__():
            raise ValueError("Rows and Collumns must be equal! {} != {}".format(self.__len__(),Matrx.__len__()))
        new_matrix = [[] for row in range(self.rows)]
        i = 0
        for row in self.matrix:
            k = 0 
            for num in row:
                new_matrix[i].append(num-Matrx.rawMatrix()[i][k])
                k +=1
            i+=1
        return Matrix(new_matrix)

    def __mul__(self,value):
        if type(value) in (int,float):
            return self.__rmul__(value)
        row_0 = self.__len__()
        col_0 = value.__len__()
        if row_0[1] != col_0[0]: 
            raise ValueError(f"\nCannot multiply a {row_0[0]} x {row_0[1]} with a {col_0[0]} x {col_0[1]} Matrix,\nMatrix 1 must have the same number of rows as the number of collumns in Matrix 2 \n({row_0[1]} != {col_0[0]})")
        new_matrix = [[] for i in range(row_0[0])]
        COLS_M2 = value.collsAll()
        j = 0
        for row in self.matrix:
            for collumn in COLS_M2:
                iterations = 0
                total = 0
                for scalar in collumn:
                    total += scalar*row[iterations]
                    iterations+=1
                new_matrix[j].append(total)
            j+=1
        return Matrix(new_matrix)


def removeCollumn(matrix : Matrix,index : int) -> Matrix:
    """Returns a reduced collumn version of a Matrix"""
    raw_matrix = [item[:] for item in matrix.rawMatrix()]
    for row in raw_matrix:
        row.pop(index)
    return Matrix(raw_matrix)

def determinant(matrix : Matrix) -> float:
    dimensions = matrix.__len__()
    if not matrix.is_square():
        raise ValueError("Cannot compute determinant of non square matrix : {}".format(dimensions))
    if dimensions[0] == 2:
        return matrix.rawMatrix()[0][0] * matrix.rawMatrix()[-1][-1] - matrix.rawMatrix()[0][-1]* matrix.rawMatrix()[-1][0]
    raw_matrix = matrix.rawMatrix()
    tmp = [item[:] for item in raw_matrix]
    tmp.pop(0)
    i = 0 
    STORAGE = []
    for i in range(matrix.__len__()[0]): #Loop throw the first row
        y = removeCollumn(Matrix(tmp),i)
        multiplier = raw_matrix[0][i] if (i+1)%2!=0 else -raw_matrix[0][i]
        STORAGE.append(multiplier * determinant(y))
        i+=1
    return sum(STORAGE)



if __name__ == "__main__":
    # A = Matrix([
    #         [436,9,10,11,7], #Number of row
    #         [437,9,10,11,3],
    #         [438,9,10,11,4],
    #         [430,9,10,11,5],
    #         [434,9,10,11,6],
    #         [453,93,16,15,64],
    #         ])

    A = Matrix([
        [1,3,5,9],
        [1,3,1,7],
        [4,3,9,7],
        [5,2,0,9]
    ])

    print(determinant(A))