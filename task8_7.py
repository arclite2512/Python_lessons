class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return ComplexNumber(a, b)

    def __mul__(self, other):
        a = (self.a * other.a) - (self.b * other.b)
        b = (self.a * other.b) + (self.b * other.a)
        return ComplexNumber(a, b)

    def __str__(self):
        return f'{self.a} + {self.b}i'


if __name__ == '__main__':
    z1 = ComplexNumber(1, -3)
    z2 = ComplexNumber(3, 5)
    z3 = z1 + z2
    z4 = z1 * z2

    print(f'z1 = {z1}')
    print(f'z2 = {z2}')
    print(f'z1 + z2 = {z3}')
    print(f'z1 * z2 = {z4}')
    