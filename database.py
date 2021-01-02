import json
import os

dir_path = 'data'
directory = os.listdir(dir_path)
for index, file in enumerate(directory):
    print(index, ':', file)

print("БАЗА ДАННЫХ ПРЕСТУПНИКА")
name_crim = input('Введите имя : ')
last_name = input('Введите фамилию : ')
midleName = input('Введите отчество : ')
year_crimm = input('Введите год рождения : ')
month_crim = input('Введите месяц рождения : ')
day_crim = input('Введите день рождения : ')
adress_crim = input('Введите адрес : ')
criminal_record = input('Введите статью : ')

criminal = {
    'Name': name_crim,
    'Last_Name': last_name,
    'Middle_Name': midleName,
    'Year': year_crimm,
    'Month': month_crim,
    'Day': day_crim,
    'Address': adress_crim,
    'Record': criminal_record,
}

filename = 'D:\Python\python_lessons\data\crim.py'

with open(filename, 'w') as f:
    stroka = json.dumps(criminal)
    print(stroka + '\n')
    f.write(stroka)
