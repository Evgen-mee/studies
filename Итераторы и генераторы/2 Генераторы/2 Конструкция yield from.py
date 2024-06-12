# Конструкция yield from
# синтаксическая конструкция yield from <iterable>
# позволяет объединить две конструкции: yield и цикл for

# было:
# def get_data():
#    for num in range(5):
#       yield num
#    for char in 'ABC':
#       yield char
# стало:
# def get_data():
#    yield from range(5)
#    yield from 'ABC'

# Было:
# def chain(*iterables):
#    for it in iterables:
#       for value in it:
#          yield value
# Стало:
# def chain(*iterables):
#    for it in iterables:
#       yield from it
# Применение:
# for i in chain('AB', [1, 2], (4, 5), {'name': 'Timur', 'age': 29}):
#     print(i, end=' ')


# конструкция yield from позволяет вкладывать один генератор в другой,
# таким образом создавать субгенераторы (вложенные генераторы).
#
# позволяет легко управлять сразу несколькими генераторами, настраивать их взаимодействие.
#
# def generator2():
#    yield 'Red'
#    yield 'Blue'
#
# def generator1():
#    yield 'Green'
#    yield from generator2()  # запрашиваем значение из субгенератора
#    yield 'Yellow'
#    yield 'Black'
#
# for color in generator1():
#    print(color, end=' ')
#
#
# Конструкции yield и yield from можно использовать для написания рекурсивных генераторов.


# def numbers(start):                    # бесконечный генератор
#    if not isinstance(start, int):      # проверка на тип
#       raise TypeError('Аргументом должно быть целое число')
#    yield start                         # вернули стартовое число
#    yield from numbers(start + 1)       # бесконечная рекрусия
#
# for index, number in enumerate(numbers(0)):
#     if index > 5:
#         break
#     print(number)
