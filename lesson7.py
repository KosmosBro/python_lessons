#
# class Poroda:
#     age = 12
#     name = 'Marusya'
#
# s1 = Poroda()
#
# class animal(Poroda):
#     def __init__(self, age, name):
#         self.poroda = 'horse'
#         self.age = age
#         self.name = name
#
#     def show(self):
#         print('This is :', self.poroda, '---', 'His name :', self.name, '---', 'It is', self.age, 'years old')
#
# f = animal(20 ,'Marusya')
# f.show()
#
# class man(Poroda):
#     def __init__(self, age, name):
#         self.poroda = 'man'
#         self.age = age
#         self.name = name
#
#     def show(self):
#         print('This is :', self.poroda, '---', 'His name :', self.name, '---', 'It is', self.age, 'years old')
#
# m = man(12, 'Oleg')
# m.show()

class salary:
    zarplata = 12000

class Driver(salary):
    def __init__(self, zarplata):
        self.bila = 10000
        self.zarplata = zarplata
        self.name = 'Anton'

    def work(self):
        print('This is', self.name, '--', 'his salary was', self.bila, '---',  'his salary now :', self.zarplata)

a = Driver(102000)
a.work()

class Worker(salary):
    def __init__(self, zarplata):
        self.bila = 15000
        self.zarplata = zarplata
        self.name = 'Oleg'

    def work(self):
        print('This is', self.name, '--', 'his salary was', self.bila, '---',  'his salary now :', self.zarplata)

    def __del__(self):
        print('объект удаляется')

a = Worker(202000)
a.work()
