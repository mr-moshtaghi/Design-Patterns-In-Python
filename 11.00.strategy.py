"""
    Strategy
"""
from abc import ABC, abstractmethod


class Context:
    def __init__(self, direction, sentence):
        self._direction = direction
        self.sentence = sentence

    def sorting(self):
        return self._direction.direct(self.sentence)


class Direction(ABC):
    @abstractmethod
    def direct(self, data):
        pass


class Right(Direction):
    def direct(self, data):
        print(data[::-1])


class Left(Direction):
    def direct(self, data):
        print(data)


c1 = Context(Right(), 'Hello World...')
c1.sorting()

c2 = Context(Left(), 'Hello World...')
c2.sorting()
