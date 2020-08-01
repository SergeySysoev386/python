def summary():
    try:
        with open('count.txt', 'w') as file_obj:
            line = input('Введите цифры через пробел:')
            file_obj.writelines(line)
            count = line.split()
            print(sum(map(int, count)))
    except IOError:
        print('Ошибка')
    except ValueError:
        print('Ошибка')
summary()