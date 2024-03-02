# Define class matrix that asks the user for two 2D arrays m1 and m2
class Matrix:
    def __init__(self):
        self.m1 = self.getmatrix("first")
        self.m2 = self.getmatrix("second")

    def getmatrix(self, name):
        # ask the user for the number of rows and columns
        rows = int(input(f"Number of rows of the {name} matrix: "))
        columns = int(input(f"Number of columns of the {name} matrix: "))

        # create an empty matrix
        matrix = []

        # iterate through the rows of the matrix and ask the user for the elements
        for i in range(rows):
            row = []
            for j in range(columns):
                row.append(int(input(f"Element at position ({i + 1}, {j + 1} of the {name} matrix: ")))
            matrix.append(row)

        return matrix
    
    # print the matrix in a readable format
    def printmatrix(self, m1, m2):
        
        print("First matrix:")
        for row in m1:
            print(row)

        print("\nSecond matrix:")
        for row in m2:
            print(row)

# debugging
# m = Matrix()
# m.printmatrix(m.m1, m.m2)

# define class operations that inherits from the matrix class
class MatrixOperations(Matrix):
    def __init__(self):
        super().__init__()

    def multiply(self):
        # check if multiplication is not possible
        if len(self.m1[0]) != len(self.m2):
            # raise a ValueError if yes
            raise ValueError("The number of columns in the first matrix must "
                             "be equal to the number of rows in the second "
                             "matrix"
                             )
        
        # create a result matrix with zeros
        result = [
            [0 for _ in range(len(self.m2[0]))] for _ in range(len(self.m1))
            ]

        # iterate through the rows of m1
        for i in range(len(self.m1)):
            # iterate through the columns of m2
            for j in range(len(self.m2[0])):
                # iterate through the rows of m2
                for k in range(len(self.m2)):
                    # multiply the elements of m1 and m2 and add them to the
                    # result matrix at the corresponding position 
                    result[i][j] += self.m1[i][k] * self.m2[k][j]

        print("\nResult matrix:")
        for row in result:
            print(row)

# debugging
mo = MatrixOperations()
mo.printmatrix(mo.m1, mo.m2)
mo.multiply()



