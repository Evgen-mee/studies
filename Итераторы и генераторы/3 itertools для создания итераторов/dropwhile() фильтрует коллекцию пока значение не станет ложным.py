# возвращает итератор, который генерирует элементы из входного итерируемого объекта сразу же после того,
# как для заданного условия будет получено ложное значение.

# не выдает никаких выходных данных до тех пор, пока функция predicate не вернет ложное значение

# Аргументы функции:
# predicate — фильтрующая функция, возвращающая bool значение
# iterable — итерируемый объект

# from itertools import dropwhile
# numbers = [1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
# words = ['is', 'an', 'of', 'python', 'C#', 'beegeek', 'is']
#
# new_numbers = list(dropwhile(lambda num: num <= 5, numbers))
# print(new_numbers)
#
# for word in dropwhile(lambda s: len(s) == 2, words):
#     print(word)
#
# выводит:
# [6, 7, 8, 9, 10, 1, 2, 3]
# python
# C#
# beegeek
# is


# Если требуется обеспечить более сложную логику фильтрации,
# то вместо использования лямбда функции нужно определить функцию явно
#
# from itertools import dropwhile
# def should_drop(x):
#     print('Testing:', x)
#     return x < 1
#
# for i in dropwhile(should_drop, [-1, 0, 1, 2, -2]):
#     print('Yielding:', i)
#
# выводит:
# Testing: -1
# Testing: 0
# Testing: 1
# Yielding: 1
# Yielding: 2
# Yielding: -2