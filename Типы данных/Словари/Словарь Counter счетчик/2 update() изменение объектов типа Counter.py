# не заменяет значения как у обычных словарей
# суммирует существующие значения
# для новых объектов метод update() создает новые пары ключ: количество

# принимает любой итерируемый объект

# можно заменить на знак +
# работает только с Counter словарями
# НО из результирующего словаря исключаются элементы с нулевыми и отрицательными значениями.

# from collections import Counter
# letters = Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
# print(letters)                    # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
# letters.update('missouri')        # добавили итерируемый обьект к letters
# print(letters)                    # Counter({'i': 6, 's': 6, 'p': 2, 'm': 2, 'o': 1, 'u': 1, 'r': 1})


# используем +
# from collections import Counter
# counter1 = Counter(i=10, s=40, p=10, m=1)
# counter2 = Counter(i=2, s=8, p=10, m=3)
# print(counter1 + counter2)          # Counter({'s': 48, 'p': 20, 'i': 12, 'm': 4})



