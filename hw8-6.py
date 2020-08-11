class app:

    def __init__(self, title, price, numb, *args):
        self.t = title
        self.p = price
        self.n = numb

        self.full = []
        self.appstore = []
        self.my_store = {'Наименование продукта': self.t, 'Цена': self.p, 'Количество': self.n}

    def __str__(self):
        return f'{self.t} цена {self.p} количество {self.n}'


    def reception(self):

        try:
            unit = input(f'Введите модель ')
            unit_p = int(input(f'Введите цену '))
            unit_n = int(input(f'Введите количество '))
            unique = {'Модель': unit, 'Цена': unit_p, 'Количество': unit_n}
            self.my_store.update(unique)
            self.appstore.append(self.my_store)
            print(f'Список техники -\n {self.appstore}')
        except:
            return f'Ошибка'
        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'ввод ')
        if q == 'Q' or q == 'q':
            self.appstore.append(self.my_store)
            print(f'Все товары склада -\n {self.appstore}')
            return f'Выход'
        else:
            return app.reception(self)


class Printer(app):
    def to_print(self):
        return


class Scanner(app):
    def to_scan(self):
        return


class Copier(app):
    def to_copier(self):
        return


unit_1 = Printer('Canon', 5555, 22, 4)
unit_2 = Scanner('SuperCopie', 5555, 5, 55)
unit_3 = Copier('Epson', 5555, 44, 33)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
