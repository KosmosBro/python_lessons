import json
import os


print('\n', "Здравствуйте , вас приветствует программа 'KOSMOS', '\n")
print("Пожалуйста, выберете действие  ")


while True:
    print('_________________________________________')
    write_new = print('1 - записать нового человека.')
    file = print('2 - просмотреть файлы в папке.')
    kreate = print('3 - редактировать файл.')
    view = print('4 - открыть файл')
    exit = print('5 - выйти из программы.')

    choise = input('выберете действие : ')

    if choise == '1':
        na = input('Введите имя : ')
        last = input('Введите фамилию : ')
        mid = input('Введите отчество : ')
        old = input('Введите год рождения : ')
        mon = input('Введите месяц рождения : ')
        da = input('Введите день рождения : ')
        adr = input('Введите адрес : ')

        new_list = {
            'Name': na,
            'Lastname': last,
            'Midlename': mid,
            'Year': old,
            'Month': mon,
            'Day': da,
            'Adres': adr
        }

        filename = 'D:\Python\python_lessons\data' + '/'
        with open(filename + na + '.json', 'w') as f:
            stroka = json.dumps(new_list)
            print(stroka + '\n')
            f.write(stroka)

    elif choise == '2':
        dir_path = 'data'
        directory = os.listdir(dir_path)
        for index, file in enumerate(directory):
            print(index, ':', file)

    elif choise == '3':
        new = input('Введите название файла')
        na = input('Введите имя : ')
        last = input('Введите фамилию : ')
        mid = input('Введите отчество : ')
        old = input('Введите год рождения : ')
        mon = input('Введите месяц рождения : ')
        da = input('Введите день рождения : ')
        adr = input('Введите адрес : ')

        new_list = {
            'Name': na,
            'Lastname': last,
            'Midlename': mid,
            'Year': old,
            'Month': mon,
            'Day': da,
            'Adres': adr
        }

        filename = 'D:\Python\python_lessons\data' + '/'
        with open(filename + new, 'w') as f:
            stroka = json.dumps(new_list)
            print(stroka + '\n')
            f.write(stroka)

    elif choise == '4':
        dir_path = 'data'
        directory = os.listdir(dir_path)
        for index, file in enumerate(directory):
            print(index, ':', file)

        index = input('Введите индекс файла : ')

        path = 'data'
        direct = os.listdir(path)
        file = path + '/' + file
        print(file)
        with open(file) as f:
            print(f.read())

    elif choise == '5':
        break

