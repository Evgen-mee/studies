# можем сымитировать наличие в классе нескольких инициализаторов.
#
# from functools import singledispatchmethod
#
# class Cat:
#     @singledispatchmethod
#     def __init__(self, breed, name, age):
#         self.breed = breed
#         self.name = name
#         self.age = age
#
#     @__init__.register(list)
#     def _from_list(self, data):
#         self.breed, self.name, self.age = data
#
#
# cat1 = Cat('Британский', 'Кемаль', 1)                         # передаем все данные отдельно
# cat2 = Cat(['Манчкин', 'Роджер', 1])                          # передаем список с данными
#
# print(cat1.breed, cat1.name, cat1.age)
# print(cat2.breed, cat2.name, cat2.age)