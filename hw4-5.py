from functools import reduce


def multi_func(el_p, el):
    return el_p * el

print(f'Список четных значений: {[el for el in range(100, 1001) if el % 2 == 0]}')
print(f'Результат перемножения элементов списка: {reduce(multi_func, [el for el in range(99, 1001) if el % 2 == 0])}')