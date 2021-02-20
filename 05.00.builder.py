""""
    Creational:
        Builder
"""
from abc import ABC, abstractmethod


class Director:
    def setBuilder(self, builder):
        self.__builder = builder

    def getCar(self):
        car = Car()

        body = self.__builder.getBody()
        car.setBody(body)

        engine = self.__builder.getEngine()
        car.setEngine(engine)

        wheel = self.__builder.getWheel()
        car.setWheel(wheel)

        return car


# ===============================================================

class Car:
    def __init__(self):
        self.__wheel = None
        self.__engine = None
        self.__body = None

    def setWheel(self, wheel):
        self.__wheel = wheel

    def setBody(self, body):
        self.__body = body

    def setEngine(self, engine):
        self.__engine = engine

    def detail(self):
        print(f'Body: {self.__body.shape}')
        print(f'Engine: {self.__engine.horsepower}')
        print(f'Wheel: {self.__wheel.size}')


# =============================================================

class Builder(ABC):

    @abstractmethod
    def getBody(self):
        pass

    @abstractmethod
    def getEngine(self):
        pass

    @abstractmethod
    def getWheel(self):
        pass


class Benz(Builder):
    def getBody(self):
        body = Body()
        body.shape = 'Suv'
        return body

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 500
        return engine

    def getWheel(self):
        wheel = Wheel()
        wheel.size = 24
        return wheel


class Bmw(Builder):
    def getBody(self):
        body = Body()
        body.shape = 'Sedan'
        return body

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 340
        return engine

    def getWheel(self):
        wheel = Wheel()
        wheel.size = 18
        return wheel


# =======================================================
class Body:
    shape = None


class Engine:
    horsepower = None


class Wheel:
    size = None


car1 = Bmw()
director = Director()
director.setBuilder(car1)
b1 = director.getCar()
b1.detail()
