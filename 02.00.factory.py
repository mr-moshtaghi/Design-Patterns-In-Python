""""
    Creational:
        Factory Method 
"""

#
# class A:
#     def __init__(self, name, format):
#         self.name = name
#         self.format = format
#
#
# class B:
#     def edit(self, file):
#         if file.format == "json":
#             print(f'Editing JSON file ...{file.name}')
#         elif file.format == "xml":
#             print(f'Editing JSON file ...{file.name}')
#         else:
#             raise ValueError("Sorry...")
#
#
# a1 = A('first', 'json')
# b1 = B()
# b1.edit(a1)


#################################################################


# class A:
#     def __init__(self, name, format):
#         self.name = name
#         self.format = format
#
#
# class B:
#     def edit(self, file):
#         if file.format == "json":
#             self.edit_json(file)
#         elif file.format == "xml":
#             self.edit_xml(file)
#         else:
#             raise ValueError("Sorry...")
#
#     def edit_json(self, file):
#         print(f'Editing JSON file ...{file.name}')
#
#     def edit_xml(self, file):
#         print(f'Editing JSON file ...{file.name}')
#
#
# a1 = A('first', 'json')
# b1 = B()
# b1.edit(a1)

####################################################################

#
# class A:
#     def __init__(self, name, format):
#         self.name = name
#         self.format = format
#
#
# class B:
#     def edit(self, file):  # client
#         edit = self._get_edit(file)
#         return edit(file)
#
#     def _get_edit(self, file):  # creator
#         if file.format == "json":
#             return self.edit_json
#         elif file.format == "xml":
#             return self.edit_xml
#         else:
#             raise ValueError("Sorry...")
#
#     def edit_json(self, file):  # product
#         print(f'Editing JSON file ...{file.name}')
#
#     def edit_xml(self, file):  # product
#         print(f'Editing XML file ...{file.name}')
#
#
# a1 = A('first', 'xml')
# b1 = B()
# b1.edit(a1)

############################################################################

from abc import ABC, abstractmethod


class Creator(ABC):
    @abstractmethod
    def make(self):
        pass

    def call_edit(self):
        product = self.make()
        result = product.edit()
        return result


class JsonCreator(Creator):
    def make(self):
        return Json()


class XmlCreator(Creator):
    def make(self):
        return Xml()


# ------------------------------------------

class Product(ABC):
    @abstractmethod
    def edit(self):
        pass


class Json(Product):
    def edit(self):
        return "Editing Json File...."


class Xml(Product):
    def edit(self):
        return "Editing Xml File...."


# -----------------------------------------

def client(format):
    return format.call_edit()


print(client(XmlCreator()))

#############################################################
