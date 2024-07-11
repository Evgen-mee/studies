# обеспечивает то же поведение, что list, с дополнительной возможностью
# предоставления доступа к базовому списку через атрибут экземпляра data

# Наследники класса UserList должны предоставить инициализатор
# который можно вызывать либо без аргументов, либо с одним аргументом, определяющим начальный набор элементов.

# НЕ ОЧЕНЬ ЭКОНОМИТ ВРЕМЯ МОЖНО ИСПОЛЬЗОВАТЬ ПРЯМОЕ НАСЛЕДОВАНИЕ!!!

# super() используется в __init__  для предотвращения проблемы в дальнейших сценариях наследования
# В остальных методах используется атрибут data, который содержит обычный список

# ЕСЛИ НАМ ПОТРЕБУЮТСЯ ДОПОЛНИТЕЛЬНЫЕ МЕТОДЫ ТО ИХ НУЖНО ПРОПИСЫВАТЬ ВСЕ!!

# сохраняет все свои элементы в виде строк
# from collections import UserList
# class StringList(UserList):
#     def __init__(self, iterable):
#         super().__init__(str(item) for item in iterable) # super()
#
#     def __setitem__(self, index, item):
#         self.data[index] = str(item)
#
#     def insert(self, index, item):
#         self.data.insert(index, str(item))
#
#     def append(self, item):
#         self.data.append(str(item))
#
#     def extend(self, other):
#         if isinstance(other, type(self)):
#             self.data.extend(other)
#         else:
#             self.data.extend(str(item) for item in other)
#
#     def __repr__(self):
#         return f'{type(self).__name__}({self.data.__repr__()})'







