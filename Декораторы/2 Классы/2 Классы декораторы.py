# декоратор может возвращать не только функцию, но и вызываемый объект

# экземпляры которых являются вызываемыми объектами, то есть содержат __call__()


# Использование классов декораторов может быть выгодно тем, что они избавляют от
# тройной последовательной вложенности функций и делают код более простым для понимания.



# import functools
#
# class do_twice:
#     def __init__(self, func):                 # декорируемая функция
#         functools.update_wrapper(self, func)  # сохранение информации о декорируемой функции
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         for _ in range(2):
#             value = self.func(*args, **kwargs) # вызов декорируемой функции
#         return value
#
#
# @do_twice
# def greet(name):
#     """docstring"""
#     print(f'Привет, {name}!')
#
#
# print(greet.__name__)
# print(greet.__doc__)
# выводит:
#
# greet
# docstring
#
#
# Когда мы сохраняем информацию о функции  помощью записи functools.update_wrapper(self, func),
# мы добавляем в словарь экземпляра __dict__ новые атрибуты с информацией о нашей функции:
#
# @do_twice
# def greet(name):
#     """docstring"""
#     print(f'Привет, {name}!')
#
#
# print(greet.__dict__)
#
#  {'__module__': '__main__', '__name__': 'greet', '__qualname__': 'greet',
#  '__doc__': 'docstring', '__annotations__': {}, '__wrapped__': <function greet at 0x00000235D4C404A0>,
#  'func': <function greet at 0x00000235D4C404A0>}
#
# Т.к. теперь greet ссылается на вызываемый объект(экземпляр do_twice), мы можем заглянуть в __dict__
# и убедиться в этом.
# Если же не использовать functools.update_wrapper(self, func) и попытаться узнать имя функции(greet.__name__)
# мы получим ошибку, т.к. в __dict__ нет такого ключа.





# декоратора с аргументами
# import functools
# class do_n_times:                 # не является объектом, заменяющим декорируемую функцию
#
#     def __init__(self, n):        # количество вызовов декорируемой функции
#         self.n = n
#
#     def __call__(self, func):     # передача декорируемой функции
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for _ in range(self.n):
#                 value = func(*args, **kwargs)   # вызов декорируемой функции
#             return value
#
#         return wrapper            # возвращает функцию wrapper(), которая и заменяет переданную
#
#
# @do_n_times(4)
# def greet(name):
#     print(f'Привет, {name}!')
#
#
# greet('Кемаль')
#
# выводит:
# Привет, Кемаль!
# Привет, Кемаль!
# Привет, Кемаль!
# Привет, Кемаль!
