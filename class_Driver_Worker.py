n = 'Turan'


class Worker:
    salary = 0
    name = 'Anton'

    def __init__(self, name, salary=45):
        self.salary = salary
        self.name = name

    def work(self):
        print('This is', self.name, '---', 'His salary now : ', self.salary)


class Driver(Worker):
    def __init__(self, salary):
        self.salary = salary
        self.name = n

    def work(self):
        print('This is', self.name, '---', 'His salary now : ', self.salary)

    def __del__(self):
        print('Сотрудник уволен !')


a = Worker("Kosmos")
a.work()

print('_____')

b = Driver(24)
b.work()
