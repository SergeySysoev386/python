class Error:
    def __init__(self, *data):
        self.data = []

    def fig(self):
        while True:
            try:
                val = int(input('Введите число:'))
                self.data.append(val)
                print(f'Введенные Вами числа: - {self.data} \n ')
            except:
                print(f"Вводить можно только число")

my_data = Error(1)
print(my_data.fig())