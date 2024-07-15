# Основным преимуществом классов данных является то, что они
# автоматически реализуют минимально необходимый базовый функционал, определяя методы:
# __init__()
# __repr__()
# __eq__()

# Аннотации типов обязательно должны присутствовать, но не обязательно должны соблюдаться

# По умолчанию экземпляры классов данных являются изменяемыми,
# поэтому мы можем без проблем менять значения их атрибутов, а также добавлять им новые атрибуты

# что бы классы были неизменяемы нужно
# передать декоратору @dataclass в качестве параметра frozen значение True
# @dataclass(frozen=True)

#  атрибуты без значений по умолчанию не могут стоять после атрибутов со значениями по умолчанию!!!

# при необходимости можем добавлять и переопределять методы

# Декоратор @dataclass имеет параметры init, repr и eq, отвечающие за
# автоматическую реализацию одноименных магических методов.
# По умолчанию данные параметры имеют значение True.
# @dataclass(init=False)                                    # не реализуем магический метод __init__()
# @dataclass(repr=False)                                    # не реализуем магический метод __repr__()
# @dataclass(eq=False)                                      # не реализуем магический метод __eq__()

# Было
# class Person:
#     def __init__(self, name, surname, age):
#         self.name = name                                  # имя
#         self.surname = surname                            # фамилия
#         self.age = age                                    # возраст


# Стало
# from dataclasses import dataclass
# @dataclass
# class Person:
#     name: str
#     surname: field(repr=False)                            # данный атрибут не будет отображаться т.к.  repr=False
#     age: int = None                                       # возраст по умолчанию равен None
#     friends: list = field(default_factory=list)           # функция list(), возвращающая пустой список


# Тип можно так же указать через "или".
# from dataclasses import dataclass
#
# @dataclass
# class Book:
#     name: str | int | float | tuple
#     author: object
#     release_year: Exception
#
#
# book = Book('Fight Club', 'Chuck Palahniuk', 1996)
#
# print(book.release_year)

print(round(1/3, 2))