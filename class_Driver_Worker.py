
class Worker:
    salary = 20000


class Driver(Worker):
    def __init__(self, a):
        self.zarplata = 10000
        self.name = 'Anton'

    def work(self):
        print('This is', self.name, '---', 'His salary was', self.zarplata, '---', 'his salary now', self.salary, '$')

    def __del__(self):
        print('Работник уволен!')


a = Driver(20000)
a.work()
