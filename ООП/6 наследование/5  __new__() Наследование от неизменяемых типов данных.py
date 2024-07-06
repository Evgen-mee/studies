# задача метода __new__() заключается в создании и возврате нового пустого экземпляра класса,
# который после будет передан в инициализатор

# метод __new__() может возвращать экземпляр класса, отличного от класса, реализующего сам метод.
# В таком случае метод __init__() вызываться не будет

# Мы можем как добавить дополнительные атрибуты через __new__()
# Так и расширить класс за счет добавления методов

# Классы bool и NoneType не могут быть родительскими

# произвольное количество позиционных и именованных аргументов в методе __new__()
# необходимо для того чтобы не ограничивать сигнатуру метода __init__(),
# так как аргументы, передаваемые классу при создании его экземпляра,
# попадают как в метод __new__(), так и в метод __init__().

# lass Animal:
#     pass
#
# class Cat:
#     def __new__(cls, *args, **kwargs):                # 1 работает до init
#         print('1. Вызова метода __new__()')
#         return Animal()                               # 2 возвращает экземпляр другого класса
#
#     def __init__(self, name):                         # 3 не сработает т.к. создаем другой класс и init будет использоваться другого класса
#         print('2. Вызова метода __init__()')
#         self.name = name
#
#
# cat = Cat('Кемаль')                                    # Вызова метода __new__()


# Переопределение метода __new__()
#
# при наследовании от неизменяемых типов данных их значение определяется при создании, то есть в методе __new__()
#
#
#class Distance(float):
# __new__() принимает три аргумента:
# cls — текущий класс, класс Distance
# value — числовое значение экземпляра класса Distance                            # НЕИЗМЕНЯЕМОЕ ЗНАЧЕНИЕ
# unit — единицы измерения, значение атрибута unit экземпляра класса Distance     # МОЖЕМ МЕНЯТЬ В ЛЮБОМ МЕСТЕ
#     def __new__(cls, value, unit):
#         instance = super().__new__(cls, value)   # возвращает экземпляр класса Distance, который имеет весь функционал класса float
#         instance.unit = unit                     # добавляется атрибут с соответствующим значением
#         return instance                          # возвращаем класс
#
#
# distance = Distance(1, 'Meters')
#
# print(distance)        # 1.0
# print(distance.unit)   # Meters


# Дополнение класса


# class WordCountString(str):                               # наследник класса str
#     def __str__(self):
#         return f'{super().__str__()}, {self.words()}'     # переопределяет имеющийся метод
#
#     def words(self):                                       # определяет дополнительный метод
#         return len(self.split())
#
#
# wordcountstring = WordCountString('I Love Beegeek')
#
# print(wordcountstring.words()) # 3
# print(wordcountstring)         # I Love Beegeek, 3

#         if isinstance(other, Point):                        # проверка на тип
#             return self.x == other.x and self.y == other.y  # сравнили парметры
#         return NotImplemented

class ModularTuple(tuple):

    def __new__(cls, iterable=tuple(), size=100):
        return super().__new__(cls, tuple(map(lambda x: x % size, iterable)))

modulartuple = ModularTuple([101, 102, 103, 104, 105])

print(modulartuple)
print(type(modulartuple))


