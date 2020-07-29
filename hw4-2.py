parent_list = [2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
child_list = [el for num, el in enumerate(parent_list) if parent_list[num - 1] < parent_list[num]]
print(f'Исходный список {parent_list}')
print(f'Выведенный список {child_list}')