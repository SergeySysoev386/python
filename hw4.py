def sal():
    try:
        time = float(input('Укажите время работы: '))
        salary = int(input('укажите ставку в час в рублях: '))
        prize = int(input('укажите размер премии: '))
        res = time * salary + prize
        print(f'заработная плата сотрудника составляет:  {res}')
    except ValueError:
        return print
sal()