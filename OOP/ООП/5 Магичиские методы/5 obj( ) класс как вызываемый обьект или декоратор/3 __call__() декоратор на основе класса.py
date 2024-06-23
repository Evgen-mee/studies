# class UppercaseDecorator:
#     def __init__(self, func):
#         self.func = func                             # приняли функцию в атрибут
#
#     def __call__(self, *args, **kwargs):             # 1) приняли аргументы
#         return self.func(*args, **kwargs).upper()    # 2) вызвали функцию из атрибута
#                                                      # 3) передали аргументы
#                                                      # 4) вернули результат работы функции
#
#
# @UppercaseDecorator
# def greet(name):
#     return f'Привет, {name}'
#
#
# print(greet('Кемаль'))  # ПРИВЕТ, КЕМАЛЬ

