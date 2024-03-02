m1 = [[1, 2, 3],
      [1, 2, 3],
      [1, 2, 3],
      [1, 2, 3]]
m2 = [[1, 2, 3],
      [1, 2, 3],
      [1, 2, 3]]

class Multiply:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

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

        print(result)

Multiply(m1, m2).multiply()