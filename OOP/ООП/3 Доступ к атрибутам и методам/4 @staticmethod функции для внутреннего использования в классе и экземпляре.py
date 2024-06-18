# не имеют обязательного параметра self или cls
# не могут изменять ни состояние объекта, ни состояние класса

# могут вызываться внутри методов экземпляра или класса для вычисления каких-либо значений,
# которые напрямую не связаны с экземплярами класса или самим классом


# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_age(self, in_human_years=False):
#         if in_human_years:
#             return Cat.age_in_human_years(self.age)          # переводим кошачьи года в человеческие
#         return self.age
#
#     @staticmethod
#     def age_in_human_years(age):
#         return (age + (age < 5) - (age > 8)) * 7             # переводим кошачьи года в человеческие
#
#
# cat = Cat('Кемаль', 2)
#
# print(cat.get_age())         # 2                                # возраст в кошачьих годах
# print(cat.get_age(True))     # 21                                # возраст в человеческих годах