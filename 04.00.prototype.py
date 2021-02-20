""""
    Creational:
        Prototype
"""
from copy import deepcopy


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Prototype:
    def __init__(self):
        self._object = {}

    def register(self, name, obj):
        self._object[name] = obj

    def unregister(self, name):
        del self._object[name]

    def clone(self, name, **kwargs):
        cloneObj = deepcopy(self._object.get(name))
        cloneObj.__dict__.update(kwargs)
        return cloneObj


p1 = Person('amir', 34)
pro2 = Prototype()
pro2.register('p2', p1)
PCopy2 = pro2.clone('p2')

print("p2 :", PCopy2.__dict__)
print("names :", PCopy2.name is p1.name)
print("ages :", PCopy2.age is p1.age)
print("id names :", f'{PCopy2.name is p1.name}-{id(p1.name)}')

print("="*100)

pro3 = Prototype()
pro3.register('p3', p1)
PCopy2 = pro3.clone('p3', age=43)

print("p3", PCopy2.__dict__)

