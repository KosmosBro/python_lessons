
def number_t(x):                                # Создаем фуннкцию number_t
    return x + 10                               # Возвращаем значение х и прибавляем к нему 100


print(number_t((lambda x: x + 100)(200)))        # Вызываем функцию lambda

print("__________________")


list_1 = range(1, 1000, 7)                      # Создали список с элементами


print(list(map(number_t, list_1)))               # С помощью map спользовали фунцию ret для списка list_1

print("__________________")

kos = iter(list_1)                   # Создали переменную kos и добавили в нее итератор
print(next(kos))
print(next(kos))
print(next(kos))
print(next(kos))
