class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return f'{self.lists[0]:3} {self.lists[1]:3} {self.lists[2]:3}\n' \
               f'{self.lists[3]:3} {self.lists[4]:3} {self.lists[5]:3}'

    def __add__(self, next_matrix):
        self.lists = [sum(el) for el in zip(self.lists, next_matrix.lists)]
        return self.__str__()


matrix = Matrix([1, 2, 3, 4, 5, 6])
matrix2 = Matrix([6, 5, 4, 3, 2, 1])

print(matrix, matrix2, sep='\n' * 2, end='\n' * 3)

print(matrix + matrix2)
