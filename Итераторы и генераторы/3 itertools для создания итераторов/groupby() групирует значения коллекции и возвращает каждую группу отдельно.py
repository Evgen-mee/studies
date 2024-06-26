# используется для группировки смежных элементов итерируемого объекта.
# Она возвращает итератор, содержащий кортежи, каждый из которых состоит из двух элементов:
# первый — значение, характеризующее группу,
# второй — итератор, содержащий элементы соответствующей группы.

# Аргументы функции:
# iterable — итерируемый объект
# key — функция, вычисляющая значение, характеризующее группу

# Если ключ key не указан или равен None, ключом по умолчанию является функция тождественности,
# которая возвращает элемент без изменений.

# не только сам результат вызова функции groupby() является итератором,
# но и вторые элементы результирующих кортежей также являются итераторами.

# тобы все равные элементы попали в одну группу, необходимо сначала отсортировать начальные данные!!!


# from itertools import groupby
# numbers = [1, 1, 1, 7, 7, 7, 7, 15, 7, 7, 7]
# group_iter = groupby(sorted(numbers))
# for key, values in group_iter:
#     print(f'{key}: {list(values)}')            # преобразуем итератор в список
#
# выводит:
# 1: [1, 1, 1]
# 7: [7, 7, 7, 7, 7, 7, 7]
# 15: [15]


# Использование аргумента key
#
# from itertools import groupby
#
# numbers = [1, 1, 1, 7, 7, 7, 7, 15, 7, 7, 7]
#
# key_func = lambda num: num < 10
#
# group_iter = groupby(sorted(numbers, key=key_func), key=key_func)
#
# for key, values in group_iter:
#     print(f'{key}: {list(values)}')
# выводит:
#
# False: [15]
# True: [1, 1, 1, 7, 7, 7, 7, 7, 7, 7]
