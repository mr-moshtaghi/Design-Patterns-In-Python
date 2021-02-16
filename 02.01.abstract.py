"""
    Abstract Class     Abstract Method
"""

from abc import ABC, abstractmethod


class A:
    def show(self):
        pass


class B(A):
    pass


print("1")
print("############")


####################################


class C(ABC):
    def show(self):
        pass


class D(C):
    pass


print("2")

d1 = D()
print("############")


######################################

class E(ABC):
    @abstractmethod
    def show(self):
        pass


class F(E):
    def show(self):
        print('Show method...')


print("3")

f1 = F()
f1.show()
print("############")


######################################

class G(ABC):
    @abstractmethod
    def show(self):
        print('Abstract Show methode ...')


class H(G):
    def show(self):
        super().show()
        print('Show method...')


print("4")
h1 = H()
h1.show()
print("############")