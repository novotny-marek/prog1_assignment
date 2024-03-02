# Define class matrix that asks the user for two 2D arrays m1 and m2
class Matrix:
    def __init__(self):
        self.m1 = self.getmatrix("first")
        self.m2 = self.getmatrix("second")
    # ask the user if they want to read the matrix from a file or input
    def getmatrix(self, name):
        choice = input(f"Do you want to read the {name} matrix from a file? (y/n): ")
        if choice.lower() == "y":
            filename = input(f"Enter the filename for the {name} matrix: ")
            matrix = self.readmatrixfromfile(filename)
        else:
            matrix = self.readmatrixfrominput(name)

        return matrix
    # read the matrix from a file
    def readmatrixfromfile(self, filename):
        matrix = []
        try:
            with open(filename, "r") as file:
                for line in file:
                    row = [int(num) for num in line.strip().split()]
                    matrix.append(row)
        except FileNotFoundError:
            print(f"File '{filename}' not found. Please try again.")
            matrix = self.readmatrixfromfile(filename)

        return matrix
    # read the matrix from input
    def readmatrixfrominput(self, name):
        rows = int(input(f"Number of rows of the {name} matrix: "))
        columns = int(input(f"Number of columns of the {name} matrix: "))

        matrix = []
        for i in range(rows):
            row = []
            for j in range(columns):
                element = int(input(f"Element at position ({i + 1}, {j + 1}) of the {name} matrix: "))
                row.append(element)
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

        choice = input("Do you want to save the result matrix? (y/n): ")
        if choice.lower() == "y":
            self.savematrix(result)

    def savematrix(self, matrix):
        with open('./matrix/result.txt', "w") as file:
            for row in matrix:
                file.write(" ".join(str(num) for num in row) + "\n")
        print("Matrix saved successfully")

# debugging
mo = MatrixOperations()
mo.printmatrix(mo.m1, mo.m2)
mo.multiply()