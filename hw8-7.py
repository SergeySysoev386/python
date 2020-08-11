class Complex:
    def __init__(self, a, b, *data):
        self.a = a
        self.b = b
        self.c = 'a + b * x'

    def __add__(self, other):
        print(f'Сумма равна')
        return f'c = {self.a + other.a} + {self.b + other.b} * x'

    def __mul__(self, other):
        print(f'Произведение равно')
        return f'c = {self.a * other.a} + {self.b * other.a} * x'

    def __str__(self):
        return f'c = {self.a} + {self.b}'


c_1 = Complex(4, 2)
c_2 = Complex(5, 8)
print(c_1)
print(c_1 + c_2)
print(c_1 * c_2)