
month = input('Введите месяц : ')

winter = ["декабрь", "январь", "февраль"]
spring = ["март", "апрель", "май"]
summer = ["июнь", "июль", "июль"]
autumn = ["сентябрь", "октябрь", "ноябрь"]

if month in winter:
    print('Сейчас зима, холодно!')

elif month in autumn:
    print('Сейчас осень, прохладно!')

elif month in spring:
    print('Сейчас весна, тепло!')

elif month in summer:
    print('Сейчас лето, жарко!')
else:
    print("Введите корректное значение!")
