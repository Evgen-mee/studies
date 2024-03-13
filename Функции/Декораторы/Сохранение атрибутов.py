#  - Сохранение атрибутов __name__ и __doc__ для декорируемой функции
# все функции содержат специальные атрибуты
#  - __name__ — имя функции
#  - __doc__ — строка документирования
#
# def greet(name):
#     '''Функция приветствия пользователя.'''
#     return f'Hello {name}!'
# print(greet.__name__) # greet
# print(greet.__doc__)  # Функция приветствия пользователя.
#
# как к функции greet() был применен декоратор,
# её атрибуты __name__ и __doc__ изменились на имя и строку внутренней функции wrapper()
#
# что бы имя и документация не менялись
# на внутреннию строку декоратора
# используем следующий код:
# def bold(func):
#     def wrapper(*args, **kwargs):
#         return '<b>' + func(*args, **kwargs) + '</b>'
#     wrapper.__name__ = func.__name__   # присвоили во внутреннию функцию декоратора
#     wrapper.__doc__ = func.__doc__     # данные вызываемой функции
#     return wrapper                     # вернули внутреннию функцию
#
# @bold
# def greet(name):
#     '''Функция приветствия пользователя.'''
#     return f'Hello {name}!'
# print(greet.__name__)
# print(greet.__doc__)
#
# на практике используют декоратор:
# import functools
# def bold(func):
#     @functools.wraps(func) # атрибуты __name__ и __doc__ не перетираются после применения декоратора bold
#     def wrapper(*args, **kwargs):
#         return '<b>' + func(*args, **kwargs) + '</b>'
#     return wrapper
# @bold
# def greet(name):
#     '''Функция приветствие пользователя.'''
#     return f'Hello {name}!'
# print(greet.__name__)
# print(greet.__doc__)
#
#
#
