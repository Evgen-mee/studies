# удаляет атрибут из объекта, называется делитером.

# class Cat:
#     def __init__(self, name):
#         self._name = name
#
#     def get_name(self):
#         return self._name
#
#     def set_name(self, name):
#         if isinstance(name, str) and name.isalpha():
#             self._name = name
#         else:
#             raise ValueError('Некорректное имя')
#
#     def del_name(self):                                 # делитер, используется для удаления имени
#         del self._name


# cat = Cat('Кемаль')

# cat.del_name()

# print(cat.get_name())
# приводит к возбуждению исключения AttributeError:
# AttributeError: 'Cat' object has no attribute '_name'



