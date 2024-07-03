# Атрибут класса можно изменить только через сам класс
# class Cat:
#     night_vision = True
#
# cat1 = Cat()
# cat2 = Cat()
# Cat.night_vision = False
# print(cat1.night_vision)       # False
# print(cat2.night_vision)       # False


# При попытке изменения атрибута класса через его экземпляр мы лишь добавляем этому
# экземпляру атрибут с аналогичным именем.
#
# class Cat:
#     night_vision = True
#
# cat1 = Cat()
# cat2 = Cat()
# cat1.night_vision = False
#
# print(cat1.night_vision, cat1.__dict__)  # False {'night_vision': False}
# print(cat2.night_vision, cat2.__dict__)  # True {}

