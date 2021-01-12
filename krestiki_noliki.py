k = [
    [3, 3, 3],
    [3, 3, 3],
    [3, 3, 3]
]


def kos():
    for d in range(3):
        print('\n', k[d])
        d += 1


kos()

for i in range(9):
    x_stroka = int(input('Введите номер строки : '))
    x_stolb = int(input('Введите номер столбика : '))
    k[x_stroka][x_stolb] = 'X'
    print(k)

    o_stroka = int(input('Введите номер строки : '))
    o_stolb = int(input('Введите номер столбика : '))
    k[o_stroka][o_stolb] = 'O'
    print(k)
