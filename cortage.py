cars = list()
for i in range(3):
    brand_car = input("Введите марку авто : ")
    model_car = input("Введите модель авто : ")
    year_car = input("Введите год авто : ")

    car = {
        'Brand': brand_car,
        'Model': model_car,
        'Year': year_car,
    }

    cars.append(car)

print(cars[0])
print(cars[1])
print(cars[2])
