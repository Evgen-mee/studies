# мы можем связать один метод сразу с несколькими типами.
# from functools import singledispatchmethod
#
# class Cat:
#     @singledispatchmethod
#     def __init__(self, breed, name, age):
#         self.breed = breed
#         self.name = name
#         self.age = age
#
#     @__init__.register(list)                       # список
#     @__init__.register(tuple)                      # кортеж
#     def _from_list_tuple(self, data):
#         self.breed, self.name, self.age = data
#
#
# cat1 = Cat(('Британский', 'Кемаль', 1))
# cat2 = Cat(['Манчкин', 'Роджер', 1])
#
# print(cat1.breed, cat1.name, cat1.age)       # Британский Кемаль 1
# print(cat2.breed, cat2.name, cat2.age)       # Манчкин Роджер 1
