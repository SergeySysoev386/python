eng_ru = {'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыре'}
list = []
translate = []
try:
    file_obj = open("1.txt", 'r')
    for line in file_obj:
        t = line.split(" - ")
        print(t)
        if t[0] in eng_ru:
            word = eng_ru[t[0]]
            translate.append(word +' - '+ t[1])
    print(translate)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file_obj.close()

try:
    frus = open("2.txt", "w")
    frus.writelines(translate)

finally:
    frus.close()