# _make() используется для создания именованных кортежей из итерируемых объектов

# метод типа, а не конкретного экземпляра, поэтому вызывать его нужно
# через название типа (Person._make)

# from collections import namedtuple
# Person = namedtuple('Person', ['name', 'age', 'height'])
# timur = Person._make(['Timur', 29, 170])
# print(timur)  # Person(name='Timur', age=29, height=170)

