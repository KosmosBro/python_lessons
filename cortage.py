car = list()
for i in range(1, 4):
    brand_car = input("Введите бренд авто : ")
    model_car = input("Введите модель авто : ")
    year_car = input("Введите год авто : ")

    cars = {
        'Brand': 'Subaru',
        'Model': 'Impreza',
        'Year': '2005',
        }

    cars['Year'] = year_car
    cars['Model'] = model_car
    cars['Brand'] = brand_car

    car.append(cars)
print(car)
