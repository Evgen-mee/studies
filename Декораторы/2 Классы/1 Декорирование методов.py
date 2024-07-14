# import functools
#
# def do_n_times(n):                             # функция декоратор
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 value = func(*args, **kwargs)
#             return value
#         return wrapper
#     return decorator
#
# class Cat:
#     @do_n_times(4)                           # декорируем метод класса
#     def say(self):
#         print('Мяу')
#
#
# cat = Cat()
#
# cat.say()
#
# выводит:
# Мяу
# Мяу
# Мяу
# Мяу