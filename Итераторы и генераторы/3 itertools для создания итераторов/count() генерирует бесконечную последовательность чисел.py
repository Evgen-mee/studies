# возвращает итератор, генерирующий бесконечную последовательность чисел.

# В отличие от встроенной функции range(), в функции count() аргумент для задания верхней границы не предусмотрен.

# не можем создать список на основе итератора, который возвращает функция count() поскольку он является бесконечным

# from itertools import count
#
# count1 = count()
#
# print(next(count1))                                  # 0
# print(next(count1), next(count1), next(count1))      # 1 2 3
#
# count2 = count(69, 10)
#
# print(next(count2))                                  # 69
# print(next(count2))                                  # 79
# print(next(count2), next(count2), next(count2))      # 89 99 109
#
# for i in zip(count(10), ['a', 'b', 'c']):
#     print(i)
# выводит:
# (10, 'a')
# (11, 'b')
# (12, 'c')