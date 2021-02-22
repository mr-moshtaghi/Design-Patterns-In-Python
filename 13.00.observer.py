"""
    behavioral:
        observer
"""


class Observer:  # کلاسی هست که دو کلاس one و two را از تغییر باخبر میکند
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)


class Data(Observer):  # کلاسی هست که قراره تغییر کند
    def __init__(self, name):
        super().__init__()
        self.name = name
        self._data = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        return self.notify()


class One:  # کلاسی که میخواهد از تغییر با خبر شود
    def update(self, subject):
        print(f'One {subject.name} new {subject.data}')


class Two:  # کلاسی که میخواد از تغییر با خبر شود
    def update(self, subject):
        print(f'Two {subject.name} new {subject.data}')


d1 = Data('amir')
o = One()
t = Two()

d1.attach(o)
d1.attach(t)

d1.data = 54
