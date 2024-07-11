# При наследовании от dict методы update(), __init__(), setdefault()
# НЕ ВЫЗЫВАЕЮТ ПЕРЕОБПРЕДЕЛЕННЫЙ МЕТОД  __setitem__() а обращащаются к родительскому __setitem__()!!!
# class UpperCaseDict(dict):
#     def __init__(self, items=(), **kwargs):
#         # если не пременить update к входным данным то при создании класса с переданными значениями
#         # будет создан просто словарь без перевода ключа в строку верхнего регистра
#         self.update(items)
#         self.update(kwargs)
#
#     # если не переопределить метод добавления то отработает версия родителя
#     # который не переводит ключ в строку верхнего регистра
#     def update(self, items):
#         if isinstance(items, dict):
#             items = items.items()
#         for key, value in items:
#             self[key] = value
#
#     # если не переопределить метод добавления то отработает версия родителя
#     # который не переводит ключ в строку верхнего регистра при использовании метода setdefault
#     def setdefault(self, key, value):
#         if str(key).upper() not in self:
#             self[key] = value
#
#
#     def __setitem__(self, key, value):   # автоматически сохраняет все ключи в виде строк в Верхнем регистре
#         key = str(key).upper()
#         super().__setitem__(key, value)
#
#     def __repr__(self):
#         return f'{type(self).__name__}({super().__repr__()})'