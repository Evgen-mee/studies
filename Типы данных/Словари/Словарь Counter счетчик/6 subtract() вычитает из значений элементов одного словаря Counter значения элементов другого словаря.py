# вычитает из значений элементов одного словаря Counter значения элементов другого словаря.
# добен методу update(), но вычитает количества, а не складывает их.
# у результирующего словаря значения ключей могут быть нулевыми или отрицательными

# можно заменить на знак -
# работает только с Counter словарями
# НО из результирующего словаря исключаются элементы с нулевыми и отрицательными значениями.

# from collections import Counter
# counter1 = Counter(i=4, s=40, a=1, p=20, b=98, z=69)
# counter2 = Counter(i=2, s=20, a=6, p=12, m=1, z=69)
# counter1.subtract(counter2)       # обновляем значения в counter1
# print(counter1)                   # Counter({'b': 98, 's': 20, 'p': 8, 'i': 2, 'z': 0, 'm': -1, 'a': -5})


# может принимать любой итерируемый объект
# from collections import Counter
# counter = Counter(i=4, s=40, a=1, p=20, b=98, z=69)
# letters = 'iisssssapppz'
# counter.subtract(letters)       # обновляем значения в counter
# print(counter)                  # Counter({'b': 98, 'z': 68, 's': 35, 'p': 17, 'i': 2, 'a': 0})


# используем -
# from collections import Counter
# counter1 = Counter(i=10, s=40, p=10, m=1)
# counter2 = Counter(i=2, s=8, p=10, m=3)
# print(counter1 - counter2)        # Counter({'s': 32, 'i': 8})
# print(counter2 - counter1)        # Counter({'m': 2})




