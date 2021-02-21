"""
    Encapsulation
        setter - getter - deleter
"""


# class Person:
#     def __init__(self, age):
#         self.__age = age
#
#     def getter_age(self):
#         return self.__age
#
#     def setter_age(self, age):
#         self.__age = age
#         return self.__age
#
#     def deleter_age(self):
#         del self.__age
#
#
# p1 = Person(34)
# print(p1.getter_age())
# p1.setter_age(43)
# print(p1.getter_age())
# p1.deleter_age()
# print(p1.getter_age())

# حالت بالا بیشتر در زبان جاوا میباشد و در پایتون به صورت بالا استفاده نمیشود


class Person:
    def __init__(self):
        self.__age = 0

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @age.deleter
    def age(self):
        del self.__age


p1 = Person()
print(p1.age)
p1.age = 43
print(p1.age)
del p1.age
print(p1.age)
