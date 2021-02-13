""""
    Creational:
        singleton
"""

import math as m1
import math as m2
print("m1:", id(m1))
print("m2:", id(m2))

print("is m1 equals m2?", m1 is m2)


class Singelton(type):
    _instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class Db(metaclass=Singelton):
    pass


d1 = Db()
d2 = Db()

print("d1:", id(d1))
print("d2:", id(d2))

print("is d1 equals d2?", d1 is d2)
print("is d1 equals d2?", d1 == d2)
