# фабричной функции, порождающей новые типы данных
#
# Сигнатура функции имеет вид:
# namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)
# Аргументы:
#
# Обязательные:
#  - typename отвечает за имя создаваемого типа
#  - field_names за названия полей
#
# Не обязательные:
#  - rename  переименовывает имена полей если имя совпадает с системными именами
#  - defaults присваивает значения по умолчанию (с конца)
#  - module меняет __main__ на введенное имя

# - field_names
# Параметр field_names является списком:
# from collections import namedtuple
# Point = namedtuple('Point', ['x', 'y'])               # в качестве второго параметра передаем список
# point =  Point(2, 4)
# print(point)                                          # выводит Point(x=2, y=4)
#
# Параметр field_names является кортежем:
# from collections import namedtuple
# Point = namedtuple('Point', ('x', 'y'))               # в качестве второго параметра передаем кортеж
# point =  Point(2, 4)
# print(point)                                          # выводит Point(x=2, y=4)
#
# Параметр field_names является словарем:
# В этом случае для полей именованного кортежа используются ключи словаря,
# поэтому в качестве значений можно указать, все что угодно.
# from collections import namedtuple
# Point = namedtuple('Point', {'x': 0, 'y': 69})        # в качестве второго параметра передаем словарь
# point =  Point(2, 4)
# print(point)                                          # выводит Point(x=2, y=4)
#
# Параметр field_names является строкой:
# При создании именованного кортежа с помощью строки мы указываем поля
# либо через символ пробела, либо разделяя их символом ,.
# from collections import namedtuple
# Point = namedtuple('Point', 'x y')                    # в качестве второго параметра передаем строку
# point =  Point(2, 4)
# print(point)                                          # выводит Point(x=2, y=4)
#
# from collections import namedtuple
# Point = namedtuple('Point', 'x,y')                   # в качестве второго параметра передаем строку
# point =  Point(2, 4)
# print(point)                                         # выводит Point(x=2, y=4)


#  - rename
# переименовывает имена полей если имя совпадает с системными именами
# from collections import namedtuple
# headers = ('name', 'surname', 'age', 'class')
# Student = namedtuple('Student', headers, rename=True)
# stud = Student('Роман', 'Белых', 26, 10)
# print(stud)                                             # Student(name='Роман', surname='Белых', age=26, _3=10)
# автоматически переименовал поле class в _3


#  - defaults
# используется для того, чтобы установить значения по умолчанию для полей именованного кортежа
# from collections import namedtuple
# Point = namedtuple('Point', ['x', 'y'], defaults=(0, 0))
# point1 = Point()      # используем значения по умолчанию
# point2 = Point(1, 9)
# print(point1)         # Point(x=0, y=0)
# print(point2)         # Point(x=1, y=9)
#
# Можно указать значение по умолчанию только для некоторых полей,
# при этом defaults присваивает значения по умолчанию с конца.
# from collections import namedtuple
# Point = namedtuple('Point', ['x', 'y'], defaults=(0,))
# point =  Point(7)      # используем значения по умолчанию для y
# print(point)           # Point(x=7, y=0)


#  - module
#  меняет __main__ на введенное имя
# from collections import namedtuple
# Point = namedtuple('Point', ['x', 'y'], module='customtypes')
# point = Point(1, 2)
# print(type(point))    # <class 'customtypes.Point'>