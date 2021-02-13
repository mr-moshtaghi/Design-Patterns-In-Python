"""

__call__

"""


class A:
    def __call__(self, *args, **kwargs):
        print("Call method ...")


a1 = A()
a1()
