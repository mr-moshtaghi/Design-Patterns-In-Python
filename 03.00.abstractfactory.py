"""
	Abstract Factory
		Car => Benz, Bmw => Suv, Coupe
			benz suv => gla, glc
			bmw suv => x1, x2
			benz coupe => cls, E-class
			bmw coupe => m2, m4
"""

from abc import ABC, abstractmethod

#
#
# class Car(ABC):
#     @abstractmethod
#     def call_suv(self):
#         pass
#
#     @abstractmethod
#     def call_coupe(self):
#         pass
#
#
# class Benz(Car):
#     def call_suv(self):
#         return Gla()
#
#     def call_coupe(self):
#         return Cls()
#
#
# class Bmw(Car):
#     def call_suv(self):
#         return X1()
#
#     def call_coupe(self):
#         return M2()
#
#
# class Suv(ABC):
#     @abstractmethod
#     def creating_suv(self):
#         pass
#
#
# class Coupe(ABC):
#     @abstractmethod
#     def creating_coupe(self):
#         pass
#
#
# class Gla(Suv):
#     def creating_suv(self):
#         print("This is your suv benz gla...")
#
#
# class X1(Suv):
#     def creating_suv(self):
#         print("This is your suv bmw x1...")
#
#
# class Cls(Coupe):
#     def creating_coupe(self):
#         print("this is your coupe benz cls...")
#
#
# class M2(Coupe):
#     def creating_coupe(self):
#         print("this is your coupe bmw m2...")
#
#
# def clientSuv(order):
#     suv = order.call_suv()
#     suv.creating_suv()
#
#
# def clientCoupe(order):
#     coupe = order.call_coupe()
#     coupe.creating_coupe()
#
#
# clientCoupe(Benz())


##############################################################################
"""
	Abstract Factory:
		Car => 1.benz, 2.bmw  => 1.suv, 2.coupe
			benz suv => gla, glc
			bmw suv => x1, x2
			benz coupe => cls, E-class
			bmw coupe => m2, m4
"""


class Car(ABC):
    @abstractmethod
    def call_suv(self):
        pass

    @abstractmethod
    def call_coupe(self):
        pass


# ----------------------------------------------------------
class Benz(Car):
    @staticmethod
    def call_suv(model):
        return model

    @staticmethod
    def call_coupe(model):
        return model


class Bmw(Car):
    @staticmethod
    def call_suv(model):
        return model

    @staticmethod
    def call_coupe(model):
        return model


# ----------------------------------------------------------
class Suv(ABC):
    @abstractmethod
    def creating_suv(self):
        pass


class Coupe(ABC):
    @abstractmethod
    def creating_coupe(self):
        pass


# ----------------------------------------------------------
class Gla(Suv, Benz):
    def creating_suv(self):
        print('This is your suv Benz Gla...')


class Glc(Suv, Benz):
    def creating_suv(self):
        print('This is your suv Benz Glc...')


class X1(Suv, Bmw):
    def creating_suv(self):
        print('This is your suv Bmw X1...')


class X2(Suv, Bmw):
    def creating_suv(self):
        print('This is your suv Bmw X2...')


# ----------------------------------------------------------
class Cls(Coupe, Benz):
    def creating_coupe(self):
        print('This is your coupe Benz Cls...')


class Eclass(Coupe, Benz):
    def creating_coupe(self):
        print('This is your coupe Benz E-class...')


class M2(Coupe, Bmw):
    def creating_coupe(self):
        print('This is your coupe Bmw M2...')


class M4(Coupe, Bmw):
    def creating_coupe(self):
        print('This is your coupe Bmw M4...')


# ----------------------------------------------------------
def OrderSuv(corp, model):  # corp is the company, model is the model of the car
    if issubclass(model, corp):  # check if the model is related to corp, so you cannot call M2 from Benz
        suv = corp().call_suv(model())
        suv.creating_suv()
    else:
        raise NameError()


def OrderCoupe(corp, model):
    if issubclass(model, corp):
        coupe = corp().call_coupe(model())
        coupe.creating_coupe()
    else:
        raise NameError()


try:
    OrderCoupe(Benz, Cls)
except (NameError,
        AttributeError):  # calling Corporation incorrectly will raise NameError, calling Model incorrectly will raise AttributeError
    print('Sorry, we dont have this model....')

try:
    OrderSuv(Bmw, Glc)
except (NameError, AttributeError):
    print('Sorry, we dont have this model....')
