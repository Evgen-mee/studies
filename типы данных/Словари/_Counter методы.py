#  - most_common()
# возвращает список наиболее повторяемых элементов и количество каждого из них.
# Метод возвращает список кортежей вида (ключ, число повторений).
# from collections import Counter
# letters = Counter('mississippi')
# numbers = Counter([5, 6, 7, 1, 3, 9, 9, 1, 2, 5, 5, 7, 7, 9])
# print(letters.most_common())
# print(numbers.most_common())
# выводит:
# [('i', 4), ('s', 4), ('p', 2), ('m', 1)]
# [(5, 3), (7, 3), (9, 3), (1, 2), (6, 1), (3, 1), (2, 1)]
#
#
# если передать целочисленный аргумент n,
# то он вернет n самых часто повторяющихся элементов.
# from collections import Counter
# letters = Counter('mississippi')
# numbers = Counter([5, 6, 7, 1, 3, 9, 9, 1, 2, 5, 5, 7, 7, 9])
# print(letters.most_common(3))
# print(numbers.most_common(4))
# выводит:
# [('i', 4), ('s', 4), ('p', 2)]
# [(5, 3), (7, 3), (9, 3), (1, 2)]
#
#
# Для поиска самых редких элементов,
# можно использовать срезы с отрицательным шагом.
# letters = Counter('mississippi')
# numbers = Counter([5, 6, 7, 1, 3, 9, 9, 1, 2, 5, 5, 7, 7, 9])
# print(letters.most_common()[-1])
# print(letters.most_common()[::-1])
# print(numbers.most_common()[-3:-1])
# выводит:
# ('m', 1)
# [('m', 1), ('p', 2), ('s', 4), ('i', 4)]
# [(6, 1), (3, 1)]
#
#
#
#  - elements()
# возвращает итератор по элементам,
# в котором каждый элемент повторяется столько раз,
# во сколько установлено его значение.
# Элементы возвращаются в порядке их появления.
# from collections import Counter
# letters = Counter('mississippi')
# numbers = Counter([5, 6, 7, 1, 3, 9, 9, 1, 2, 5, 5, 7, 7, 9])
# print(list(letters.elements()))
# print(list(numbers.elements()))
# выводит:
# ['m', 'i', 'i', 'i', 'i', 's', 's', 's', 's', 'p', 'p']
# [5, 5, 5, 6, 7, 7, 7, 1, 1, 3, 9, 9, 9, 2]
#
# сли количество элементов по некоторому ключу меньше единицы,
# то метод elements() просто проигнорирует его.
#
#  - total()
# вычисляет сумму всех значений Counter словаря, включая отрицательные.
# from collections import Counter
# letters = Counter(i=4, s=4, a=0, p=2, b=-98, m=1)
# print(letters.total())
# выводит:
# -87
#
# В более ранних версиях Python приведенный выше код можно заменить кодом:
# from collections import Counter
# letters = Counter(i=4, s=4, a=0, p=2, b=-98, m=1)
# print(sum(letters.values()))
#
#
#  - subtract()
# вычитает из значений элементов одного словаря Counter
# значения элементов другого словаря.
# Метод subtract() подобен методу update(),
# но вычитает количества, а не складывает их. При этом у результирующего
# словаря значения ключей могут быть нулевыми или отрицательными.
# from collections import Counter
# counter1 = Counter(i=4, s=40, a=1, p=20, b=98, z=69)
# counter2 = Counter(i=2, s=20, a=6, p=12, m=1, z=69)
# counter1.subtract(counter2)       # обновляем значения в counter1
# print(counter1)
# выводит:
# Counter({'b': 98, 's': 20, 'p': 8, 'i': 2, 'z': 0, 'm': -1, 'a': -5})
#
# может принимать любой итерируемый объект
# from collections import Counter
# counter = Counter(i=4, s=40, a=1, p=20, b=98, z=69)
# letters = 'iisssssapppz'
# counter.subtract(letters)       # обновляем значения в counter
# print(counter)
# выводит:
# Counter({'b': 98, 'z': 68, 's': 35, 'p': 17, 'i': 2, 'a': 0})
#
#
#  - Операторы +, -, &, |
# при использовании операторов + и - из результирующего словаря
# исключаются элементы с нулевыми и отрицательными значениями
# from collections import Counter
# counter1 = Counter(i=10, s=40, p=10, m=1)
# counter2 = Counter(i=2, s=8, p=10, m=3)
# print(counter1 + counter2)
# print(counter1 - counter2)
# print(counter2 - counter1)
# выводит:
# Counter({'s': 48, 'p': 20, 'i': 12, 'm': 4})
# Counter({'s': 32, 'i': 8})
# Counter({'m': 2})
#
# пересечения (&) и объединения (|)
# возвращают минимум и максимум из соответствующих значений.
# from collections import Counter
# counter1 = Counter(i=10, s=40, p=10, m=1)
# counter2 = Counter(i=2, s=8, p=10, m=3)
# print(counter1 & counter2)
# print(counter1 | counter2)
# выводит:
# Counter({'p': 10, 's': 8, 'i': 2, 'm': 1})
# Counter({'s': 40, 'i': 10, 'p': 10, 'm': 3})
#
#
#  - операторы <, <=, >, >=
# from collections import Counter
# counter1 = Counter('aabc')
# counter2 = Counter('abc')
# print(counter1 > counter2)
# counter1 = Counter('abcde')
# counter2 = Counter('abc')
# print(counter1 > counter2)
# counter1 = Counter('abcde')
# counter2 = Counter('abcdf')
# print(counter1 > counter2)
# print(counter1 < counter2)
# выводит:
# True
# True
# False
# False
#
#
#  - __dict__
# используется для динамического наделения объектов дополнительным функционалом
# from collections import Counter
# counter = Counter(green=10, red=25, blue=5)
# print(counter.__dict__)
# counter.__dict__['min_value'] = lambda: min(counter.values())
# counter.max_value = lambda: max(counter.values())
# print(counter.min_value())
# print(counter.max_value())
# выводит:
# {}
# 5
# 25
#




















