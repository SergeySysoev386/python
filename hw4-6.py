from itertools import count
from itertools import cycle

def iter_func(start_number, stop_number):
    for el in count(start_number):
        if el > stop_number:
            break
        else:
            print(el)
def cycle_func(my_list, iteration):
    i = 0
    iter = cycle(my_list)
    while i < iteration:
        print(next(iter))
        i+=1
iter_func(start_number = int(input("Введите начальне число: ")), stop_number = int(input("Введите конечное число: ")))
cycle_func(my_list = [1, 2], iteration = int(input("Задайте итерацию: ")))