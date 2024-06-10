# содержит кортеж строк, в котором перечислены имена полей
# обращаться к атрибуту _fields можно как через класс так и через обьект класса

# from collections import namedtuple
# Person = namedtuple('Person', ['name', 'age', 'height'])
# tim = Person('Тимур', 29, 170)
# print(tim)                 # Person(name='Тимур', age=29, height=170)
# print(tim._fields)         # ('name', 'age', 'height')
# print(Person._fields)      # ('name', 'age', 'height')


# можем создавать новые именованные кортежи на основании уже существующих
# from collections import namedtuple
# Person = namedtuple('Person', ['name', 'age', 'height'])
# ExtendedPerson = namedtuple('ExtendedPerson', [*Person._fields, 'weight'])  # распаковка полей старого кортежа
# timur = ExtendedPerson('Тимур', 29, 170, 65)
# print(timur)                                           # ExtendedPerson(name='Тимур', age=29, height=170, weight=65)
# print(ExtendedPerson._fields)                          # ('name', 'age', 'height', 'weight')


# _fields для перебора полей и их значений
# from collections import namedtuple
# Person = namedtuple('Person', ['name', 'age', 'height'])
# timur = Person('Тимур', 29, 170)
# for field, value in zip(Person._fields, timur): # передали имена и значения
#     print(field, '->', value)
#
# выводит:
# name -> Тимур
# age -> 29
# height -> 170


