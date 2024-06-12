# последовательный обход с помощью цикла for
# for сам перехватывает исключение StopIteration
# numbers = [-3, 6, 1, -90, 34, -25, 23, -21]
# positive_numbers = map(abs, numbers)     # создаем объект итератора
# for num in positive_numbers:             # обходим итератор циклом for
#     print(num)

# преобразования итератора в коллекцию
# numbers = [-3, 6, 1, -90, 34, -25, 23, -21]
# positive_numbers = map(abs, numbers)                 # создаем объект итератора
# positive_numbers_list = list(positive_numbers)       # преобразуем итератор в список


# Оператор принадлежности in
# Проверка на вхождение проверяется путем перебора всех элементов

# from copy import copy
# def get_min_max(iterable):
#     try:
#         return min(copy(iterable)), max(iterable)
#     except:
#         pass
#
#
#
#
#
#
# ДатаВремя = iter(range(100_000_000))
#
# print(get_min_max(ДатаВремя))