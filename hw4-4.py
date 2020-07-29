parent_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
child_list = [el for el in parent_list if parent_list.count(el) < 2]
print(f'Элементы списка, не имеющие повторений: {child_list}')