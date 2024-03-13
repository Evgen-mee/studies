# def reduce(operation, items, initial_value):
#     acc = initial_value
#     for item in items:
#         acc = operation(acc, item)
#     return acc
#
# def add(x, y):
#     return x+y
#
#
# def mult(x, y):
#     return x*y
#
#
# numbers = [1, 2, 3, 4, 5]
#
# total = reduce(add, numbers, 0)
# product = reduce(mult, numbers, 1)
#
# print(total) == 15
# print(product) == 120

# необходимо подключить специальный модуль
# from functools import reduce
# reduce(func, iterable, initializer=None)
# Если начальное значение не установлено,
# то в его качестве используется первое значение из последовательности
