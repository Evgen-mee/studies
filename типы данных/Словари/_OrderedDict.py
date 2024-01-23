# Как и defaultdict, эти словари можно создавать любым
# из доступных способов, как и обычные словари:
# from collections import OrderedDict
# numbers1 = OrderedDict({'one': 1, 'two': 2, 'three': 3})
# numbers2 = OrderedDict([('one', 1), ('two', 2), ('three', 3)])
# numbers3 = OrderedDict(one=1, two=2, three=3)


# В Python 3.9 появились операторы | и |= которые реализуют операцию конкатенации словарей,
# как обычных, так и OrderedDict
#
# Тип данных OrderedDict проигрывает типу dict по производительности:


# одержат дополнительный атрибут __dict__
# from collections import OrderedDict
# letters = OrderedDict(b=2, d=4, a=1, c=3)
# print(letters)
# print(letters.__dict__)
# letters.__dict__['advanced'] = '144'
# print(letters)
# print(letters.__dict__)
# выводит:
# OrderedDict([('b', 2), ('d', 4), ('a', 1), ('c', 3)])
# {}
# OrderedDict([('b', 2), ('d', 4), ('a', 1), ('c', 3)])
# {'advanced': '144'}



# При сравнении на равенство обычного словаря (тип dict) и OrderedDict словаря
# порядок расположения их элементов неважен.


# При сравнение на равенство OrderedDict словарей порядок расположения их элементов важен.
#
# Тип OrderedDict является изменяемым
#
# при вставке новый элемент в существующий OrderedDict словарь, то этот элемент добавится в конец словаря.
#
# Если мы удалим элемент из существующего OrderedDict словаря
# и снова вставим его, то он будет помещен в конец словаря.
#
# Если мы обновляем значение по существующему ключу,
# то ключ сохраняет свою позицию.
#
# можем перебирать ключи напрямую
# или можем использовать словарные методы items(), keys() и values().
#
# При итерировании по OrderedDict словарям
# мы можем использовать встроенную функцию reversed()
#
# from collections import OrderedDict
# numbers = OrderedDict(one=1, two=2, three=3)
# # перебор ключей напрямую
# for key in reversed(numbers):
#     print(key, '->', numbers[key])
# print()
# # перебор пар (ключ, значение) через метод
# for key, value in reversed(numbers.items()):
#     print(key, '->', value)
# print()
# # перебор ключей через метод
# for key in reversed(numbers.keys()):
#     print(key, '->', numbers[key])
# print()
# # перебор значений через метод
# for value in reversed(numbers.values()):
#     print(value)


#  - move_to_end()
# позволяет переместить существующий элемент либо в конец, либо в начало словаря
#
# - key (обязательный аргумент) – ключ, который идентифицирует перемещаемый элемент
# - last (необязательный аргумент) – по умолчанию True перемещает элемент в конец, значение False – в начало
#
# Если при вызове метода move_to_end()
# переданный ключ отсутствует в словаре, то возникает ошибка
#
# from collections import OrderedDict
# numbers = OrderedDict(one=1, two=2, three=3)
# print(numbers)
# numbers.move_to_end('one')       # last=True
# print(numbers)
# numbers.move_to_end('three', last=False)       # last=False
# print(numbers)
# выводит:
# OrderedDict([('one', 1), ('two', 2), ('three', 3)])
# OrderedDict([('two', 2), ('three', 3), ('one', 1)])
# OrderedDict([('three', 3), ('two', 2), ('one', 1)])
#
# можем сортировать OrderedDict словарь по ключам
# from collections import OrderedDict
# letters = OrderedDict(b=2, d=4, a=1, c=3)
# for key in sorted(letters):
#     letters.move_to_end(key)
# print(letters)
# выводит:
# OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])


#  - popitem() позволяет удалить и вернуть элемент либо из конца, либо из начала словаря
# по умолчанию удаляет и возвращает элемент в
# порядке LIFO (Last-In/First-Out, последний пришел/первый ушел).
# Другими словами, метод popitem() удаляет элементы с конца словаря.
#
# from collections import OrderedDict
# numbers = OrderedDict(one=1, two=2, three=3)
# print(numbers.popitem())
# print(numbers)
# print(numbers.popitem())
# print(numbers)
# выводит:
# ('three', 3)
# OrderedDict([('one', 1), ('two', 2)])
# ('two', 2)
# OrderedDict([('one', 1)])
#
#
# необязательный аргумент last=False, то он начнет удалять и возвращать элементы
# в порядке FIFO (First-In/First-Out, первый пришел/первый ушел).
# from collections import OrderedDict
# numbers = OrderedDict(one=1, two=2, three=3)
# print(numbers.popitem(last=False))
# print(numbers)
# print(numbers.popitem(last=False))
# print(numbers)
# выводит:
# ('one', 1)
# OrderedDict([('two', 2), ('three', 3)])
# ('two', 2)
# OrderedDict([('three', 3)])




# При сравнение на равенство OrderedDict словарей порядок расположения их элементов важен.
# from collections import OrderedDict
# letters1 = OrderedDict(a=1, b=2, c=3, d=4)
# letters2 = OrderedDict({'b': 2, 'a': 1, 'c': 3, 'd': 4})
# letters3 = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
# print(letters1 == letters2)
# print(letters1 == letters3)
# выводит:
# False
# True
#
# При сравнении на равенство обычного словаря (тип dict) и OrderedDict словаря
# порядок расположения их элементов неважен.
#
#
# В Python 3.9 появились операторы | и |= которые реализуют операцию конкатенации словарей,
# как обычных, так и OrderedDict
#
# Тип данных OrderedDict проигрывает типу dict по производительности:

from collections import OrderedDict

def custom_sort(ordered_dict, by_values=False):
    if by_values:
        for key in sorted(ordered_dict, key=lambda x: ordered_dict[x]):
            ordered_dict.move_to_end(key)
    else:
        for key in sorted(ordered_dict):
            ordered_dict.move_to_end(key)











