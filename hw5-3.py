personal = {'Иванов': 21000, 'Петров': 19000, 'Сидоров': 18000, 'Васильев': 25000}
try:
    file_obj = open("salary.txt", 'w')
    for worker, salary in personal.items():
        file_obj.write(worker + ':' + str(salary) + "\n")
finally:
    file_obj.close()
sum = 0
c = 0
staff = []
with open("salary.txt", "r") as file_obj:
    for line in file_obj:
        print(line, end="")
        p = line.split(':')
        if int(p[1]) <= 20000:
            staff.append(p[0])
        sum += int(p[1])
        c += 1
avg = sum / c
print(f"Сотрудники, получающие менее 20000: {staff}")
print(f"Средняя зарплата: {avg}")