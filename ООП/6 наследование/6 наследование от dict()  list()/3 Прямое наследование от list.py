# Методы remove() и pop() типа list не вызывают магический метод __delitem__().
# Метод __ne__() не вызывает метод __eq__()
# ЕСЛИ МЕТОД НЕ ПЕРЕОПРЕДЕЛЕН ТО ИДЕТ ОБРАЩЕНИЕ К МЕТОДАМ РОДИТЕЛЯ!!!

# автоматически сохраняет все свои элементы в виде строк
# class StringList(list):
#     def __init__(self, iterable):
#         super().__init__(str(item) for item in iterable)
#
#     def __setitem__(self, index, item):
#         super().__setitem__(index, str(item))
#
#     def insert(self, index, item):
#         super().insert(index, str(item))
#
#     def append(self, item):
#         super().append(str(item))
#
#     def extend(self, other):
#         if isinstance(other, type(self)):
#             super().extend(other)
#         else:
#             super().extend(str(item) for item in other)
#
#     def __repr__(self):
#         return f'{type(self).__name__}({super().__repr__()})'



