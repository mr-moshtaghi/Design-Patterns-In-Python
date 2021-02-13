""""
    Meta Class
"""


class Singelton(type):
    _instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class db(metaclass=Singelton):
    pass


d1 = db()
d2 = db()

print(id(d1))
print(id(d2))
