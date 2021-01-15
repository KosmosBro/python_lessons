
class Worker:
    salary = 20000


class Driver(Worker):
    def __init__(self, salary):
        self.salary = salary
        self.name = 'Anton'

    def work(self):
        print('This is', self.name, '---', 'his salary now', self.salary, '$')

    def __del__(self):
        print('Работник уволен!')


a = Driver(20000)
a.work()
