
class Salary:
    zarplata = 12000


class Driver(Salary):
    def __init__(self, zarplata):
        self.bila = 10000
        self.zarplata = zarplata
        self.name = 'Anton'

    def work(self):
        print('This is', self.name, '--', 'his salary was', self.bila, '---', 'his salary now :', self.zarplata)


a = Driver(102000)
a.work()


class Worker(Salary):
    def __init__(self, zarplata):
        self.bila = 15000
        self.zarplata = zarplata
        self.name = 'Oleg'

    def work(self):
        print('This is', self.name, '--', 'his salary was', self.bila, '---', 'his salary now :', self.zarplata)

    def __del__(self):
        print('объект удаляется')


a = Worker(202000)
a.work()
