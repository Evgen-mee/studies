# Для того чтобы создать декоратор, принимающий аргументы,
# необходимо добавить еще один уровень вложенности,
# то есть создать функцию, которая возвращает нужный декоратор:

# import functools
# def print_symbols(symbol, length):       # 1) функция, которая принимает аргументы symbol и length
#     def decorator(func):                 # 3) декоратор принимает функцию
#         @functools.wraps(func)           # 4) переписывает имя и комментарий wrapper на func
#         def wrapper(*args, **kwargs):    # 6) вложенная функция принимает параметры
#             print(symbol * length)       # 7) исполняемый код
#             return func(*args, **kwargs) # 8) возвращаем результат работы func
#         return wrapper                   # 5) декоратор возвращает вложенную функцию
#     return decorator                     # 2) возвращает декоратор

# @print_symbols('*', 30)
# def add(a, b):
#     return a + b
#
# @print_symbols('-', 10)
# def mult(a, b):
#     return a * b
#
# @print_symbols('=', 40)
# def diff(a, b):
#     return a - b
#
# print(add(3, 9))
# print(mult(10, 20))
# print(diff(100, 1))
