# _replace() позволяет создавать новые именованные кортежи на основании уже существующих с заменой некоторых значений.
# Потребность в данном методе вызвана тем, что именованные кортежи являются неизменяемыми.


# from collections import namedtuple
# Person = namedtuple('Person', ['name', 'age', 'height', 'country'])
# timur1 = Person('Тимур', 29, 170, 'Russia')
# timur2 = timur1._replace(age=30, country='Germany')
# print(timur1)   # Person(name='Тимур', age=29, height=170, country='Russia')
# print(timur2)   # Person(name='Тимур', age=30, height=170, country='Germany')