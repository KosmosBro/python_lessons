# __ЗАДАНИЕ № 1 lambda__

def number_t(x):  # Создаем фуннкцию number_t
    return x + 100  # Возвращаем значение х и прибавляем к нему 100


print(number_t((lambda x: x + 100)(200)))  # Вызываем функцию lambda

print("__________________")

# __ЗАДАНИЕ № 2 map__

list_1 = range(1, 1000, 7)           # Создали список с элементами


def ret(x):                     # Создали функцию с возвращением значения х
    return x+20


funk = list(map(ret, list_1))   # С помощью map спользовали фунцию ret для списка list_1
print(funk)


print("__________________")

# __ЗАДАНИЕ № 3 iter()__

spisok = {12, 23, 45, 67}


kos = iter(spisok)          # Создали переменную kos и добавили в нее итератор
print(next(kos))
print(next(kos))
print(next(kos))
print(next(kos))

