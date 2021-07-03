"""
__new
"""


class A:
    def __init__(self, name):
        self.name = name

    def __new__(cls, name, *args, **kwargs):
        if name == "john":
            return None
        else:
            return super().__new__(cls, *args, **kwargs)


a1 = A('john')
a2 = A('sajjad')

print(a1)
print(a1.__class__.__class__)

print(a2.name)
