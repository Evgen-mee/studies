# Возвращает итератор, элементами которого являются накопленные суммы или накопленные результаты функции func.

# генерирует все промежуточные результаты

# Аргументы функции:
# iterable — итерируемый объект
# func — функция, принимающая два аргумента, по умолчанию используется функция сложения operator.add
# initial — начальное значение, по умолчанию имеет значение None

# from itertools import accumulate
# import operator
# data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
# print(list(accumulate(data)))                 # [3, 7, 13, 15, 16, 25, 25, 32, 37, 45]
# print(list(accumulate(data, operator.mul)))   # [3, 12, 72, 144, 144, 1296, 0, 0, 0, 0]
# print(list(accumulate(data, max)))            # [3, 4, 6, 6, 6, 9, 9, 9, 9, 9]
# print(list(accumulate(data, min)))            # [3, 3, 3, 2, 1, 1, 0, 0, 0, 0]





