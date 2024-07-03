# Обращение к дескриптору через класс приводит к вызову метода __get__()
# с автоматической передачей в качестве экземпляра класса значения None
# Для корректной работы дескриптора рекомендуется всегда проверять,
# какое обращение происходит к дескриптору — через класс или через экземпляр класса.
# if obj is None:  # проверка на то, как осуществляется обращение
#     return self
# if self.attr in obj.__dict__:
#     return obj.__dict__[self.attr]


# Дескрипторы делятся на два вида

#  - non-data descriptor (дескриптор не данных)
# дескрипторы не данных не могут менять значения какого-либо свойства, так как не имеют сеттера и делитера.
# class A:
#     def __get__(self, instance, owner):
#         return ...
# имеют тот же приоритет доступа, что и обычные атрибуты класса
# если мы решим записать в переменную данные
# pt.xr = 5
# то вызовиться сетор обьекта pt
# и в его __dict__ будет записанно xr = 5

#  - data descriptor (дескриптор данных)
#
# class B:
#     def __get__(self, instance, owner):
#         return ...
#
#     def __set__(self, instance, value):
#         ...
#
#     def __del__(self):
#         ...


# class Integer:                               # Дискриптор класс для int
#
#     @classmethod
#     def verify_coord(cls, coord):             # проверка на тип
#         if type(coord) != int:
#             raise TypeError("Координата должна быть целым числом")
#
#     def __set_name__(self, owner, name):     # 2 автоматически вызывался магический метод при создании
#         self.name = "_" + name
#         # self являлся ссылкой на создаваемый экземпляр класса Integer
#         # owner – ссылка на класс Point3D
#         # name – имя атрибута
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):      # 5 вызывается метод
#         self.verify_coord(value)
#         setattr(instance, self.name, value)   # 6 формируем в обьекте локальное свойство с именем self.name и присваиваем значение value.
#                                               # 7 В результате, в объекте pt появляются локальные свойства _x, _y, _z с соответствующими значениями.
#         # self – это ссылка на объект дескриптора;
#         # instance – ссылка на объект pt, из которого произошло обращение к дескриптору;
#         # value – присваиваемое значение
#
#
# class Point3D:                           # класс имеющий 3 атрибута одинакового формата
#     x = Integer()                        # 1 записали в переменную обьект класса Integer
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x                      # 4.0  self.x сейчас дискриптор (Integer())
#         self.y = y                      # 4.1  присваеваем переменную в Integer()
#         self.z = z                      # 4.2  вызывается метод __set__ в Integer()
#
#
# pt = Point3D(1, 2, 3)          # 3 при создании обьекта сработает __init__




