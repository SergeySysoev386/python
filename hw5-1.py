f = open('123.txt', 'w')
text = input('Введите текст:' '\n')
while text:
    f.write(text)
    text = input('Введите текст:' '\n')
    if not text:
        break

f.close()
f = open('123.txt', 'r')
while True:
    content = f.read(1024)
    print(content)

    if not content:
        break
f.close()
