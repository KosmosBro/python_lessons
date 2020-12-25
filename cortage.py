
brand_car = input("Введите бренд авто : ")
model_car = input("Введите модель авто : ")
year_car = input("Введите год авто : ")

cars = {
    'Brand': 'Subaru',
    'Model': 'Impreza',
    'Year': '2005',
}

del_year = cars.popitem()
del_model = cars.popitem()
del_brand = cars.popitem()

cars.setdefault(del_brand[0], brand_car)
cars.setdefault(del_model[0], model_car)
cars.setdefault(del_year[0], year_car)

print(cars.items())
