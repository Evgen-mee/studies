# Атрибуты _fields, _field_defaults
#
# - _fields
# содержит кортеж строк
# в котором перечислены имена полей
# from collections import namedtuple
# Person = namedtuple('Person', ['name', 'age', 'height'])
# tim = Person('Тимур', 29, 170)
# print(tim)
# print(tim._fields)
# print(Person._fields)
# выводит:
# Person(name='Тимур', age=29, height=170)
# ('name', 'age', 'height')
# ('name', 'age', 'height')
#
# - _field_defaults
# содержит словарь
# который сопоставляет имена полей с соответствующими значениями по умолчанию
# если таковые имеются
# from collections import namedtuple
# Person = namedtuple('Person', ['name', 'age', 'height'])
# ExtendedPerson = namedtuple('ExtendedPerson', [*Person._fields, 'weight'])  # распаковка полей старого кортежа
# timur = ExtendedPerson('Тимур', 29, 170, 65)
# print(timur)
# print(ExtendedPerson._fields)
# выводит:
# ExtendedPerson(name='Тимур', age=29, height=170, weight=65)
# ('name', 'age', 'height', 'weight')
#
#
# from collections import namedtuple
# Person = namedtuple('Person', ['name', 'age', 'height'])
# timur = Person('Тимур', 29, 170)
# for field, value in zip(Person._fields, timur):
#     print(field, '->', value)
# выводит:
# name -> Тимур
# age -> 29
# height -> 170
#
# можем выяснить, какие поля именованного кортежа имеют значения по умолчанию.
# from collections import namedtuple
# Person = namedtuple('Person', ['name', 'age', 'height', 'country'], defaults=['Russia'])
# timur = Person('Тимур', 29, 170)
# print(timur)
# print(timur._field_defaults)
# print(Person._field_defaults)
# Приведенный выше код выводит:
# Person(name='Тимур', age=29, height=170, country='Russia')
# {'country': 'Russia'}
# {'country': 'Russia'}
#
#
# Если именованный кортеж не предоставляет значений по умолчанию, тогда атрибут _field_defaults содержит пустой словарь.
# Приведенный ниже код:
# from collections import namedtuple
# Person = namedtuple('Person', ['name', 'age', 'height', 'country'])
# timur = Person('Тимур', 29, 170, 'Russia')
# print(Person._field_defaults)
# выводит:
# {}
#
#
# Методы _make(), _replace(), _asdict()
#  - index()
# возвращает индекс первого элемента, значение которого равняется переданному значению
#
# - count()
# возвращает количество элементов в кортеже, значения которых равны переданному значению
#
#  - _make()
# метод типа, а не конкретного экземпляра, поэтому вызывать его нужно через название типа (Person._make).
#
# используется для создания именованных кортежей из итерируемых объектов
# from collections import namedtuple
# Person = namedtuple('Person', ['name', 'age', 'height'])
# timur = Person._make(['Timur', 29, 170]) #передали список
#
# - _asdict()
# возвращает словарь, в котором имена полей используются в качестве ключей.
# Ключи результирующего словаря находятся в том же порядке, что и поля в исходном именованном кортеже.
# from collections import namedtuple
# Person = namedtuple('Person', ['name', 'age', 'height'])
# timur = Person._make(['Timur', 29, 170])
# print(timur._asdict())
# выводит:
# {'name': 'Timur', 'age': 29, 'height': 170}
#
#  - _replace()
# озволяет создавать новые именованные кортежи на основании уже существующих с заменой некоторых значений.
# from collections import namedtuple
# Person = namedtuple('Person', ['name', 'age', 'height', 'country'])
# timur1 = Person('Тимур', 29, 170, 'Russia')
# timur2 = timur1._replace(age=30, country='Germany')
# print(timur1)
# print(timur2)
# выводит:
# Person(name='Тимур', age=29, height=170, country='Russia')
# Person(name='Тимур', age=30, height=170, country='Germany')
#


