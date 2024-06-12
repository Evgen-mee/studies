# возвращает итератор, бесконечно генерирующий единственное значение, переданное в качестве аргумента.
# Количество генераций можно ограничить c помощью необязательного аргумента times.

# Аргументы функции:
# obj — любой Python объект
# times — количество повторений, по умолчанию имеет значение None
#
# from itertools import count, repeat
#
# for i, s in zip(count(), repeat('bee-and-geek', 5)):
#     print(i, s)
# и выводит:
#
# 0 bee-and-geek
# 1 bee-and-geek
# 2 bee-and-geek
# 3 bee-and-geek
# 4 bee-and-geek