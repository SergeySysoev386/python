list = ['Иванов\n', 'Петров\n', 'Сидоров\n', 'Васильев\n']
with open("list.txt", 'w') as file_obj:
    file_obj.writelines(list)
with open("list.txt") as file_obj:
    lines = 0
    letters = 0
    for line in file_obj:
        lines += line.count('\n')
        letters = len(line)-1
        print(f" Количество букв в строке: {letters}")
    print(f"Количество строк: {lines}")