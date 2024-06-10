# группирует несколько словарей вместе,
# что позволяет рассматривать их как единое целое.
#
# Объекты типа ChainMap обычно создаются на основе словарей.
# from collections import ChainMap
# empty_chain_map = ChainMap()                      # создаем пустой ChainMap объект
# print(empty_chain_map)
# numbers = {'one': 1, 'two': 2}
# letters = {'a': 'A', 'b': 'B'}
# chain_map = ChainMap(numbers, letters)            # создаем ChainMap объект на основе словарей numbers и letters
# print(chain_map)
# выводит:
# ChainMap({})
# ChainMap({'one': 1, 'two': 2}, {'a': 'A', 'b': 'B'})
#
#
# можем создавать объекты типа ChainMap, используя метод fromkeys().
# from collections import ChainMap
# chain_map1 = ChainMap.fromkeys(['one', 'two', 'three'])
# chain_map2 = ChainMap.fromkeys(['one', 'two', 'three'], -1)
# print(chain_map1)
# print(chain_map2)
# выводит:
# ChainMap({'one': None, 'two': None, 'three': None})
# ChainMap({'one': -1, 'two': -1, 'three': -1})
#
#
# Для получения значений по ключу квадратные скобки, либо метод get()
# from collections import ChainMap
# numbers = {'one': 1, 'two': 2}
# letters = {'a': 'A', 'b': 'B'}
# alpha_num = ChainMap(numbers, letters)
# print(alpha_num['one'])
# print(alpha_num['b'])
# print(alpha_num.get('a'))
# print(alpha_num.get('c'))
# print(alpha_num.get('d', False))
# выводит:
# 1
# B
# A
# None
# False
#
#
# объект в котором есть повторяющиеся ключи в объединяемых словарях.
# когда у объединяемых словарей есть повторяющиеся ключи, мы получаем только значение из первого словаря
#
# from collections import ChainMap
# for_adoption = {'dogs': 15, 'cats': 8, 'pythons': 9}
# vet_treatment = {'dogs': 7, 'cats': 2, 'tigers': 3}
# pets = ChainMap(for_adoption, vet_treatment)
# print(pets['dogs'])
# print(pets['cats'])
# print(pets['pythons'])
# print(pets['tigers'])
# выводит:
# 15
# 8
# 9
# 3
#
#
# Итерирование происходит в обратном порядке от последнего указанного словаря к первому
# будем получать первое из значений.
# from collections import ChainMap
# numbers = {'one': 1, 'two': 2}
# letters = {'a': 'A', 'b': 'B'}
# alpha_num = ChainMap(numbers, letters)
# for key in alpha_num:
#     print(key, '->', alpha_num[key])
# выводит:
# a -> A
# b -> B
# one -> 1
# two -> 2
#
#
# можем обновлять, добавлять, удалять и извлекать элементы
# все эти операции действуют только на первый из объединяемых словарей
#
# Удаления значения по ключу, которого нет в первом словаре возникает ошибка
# Даже если указанный ключ есть в одном из объединяемых словарей, кроме первого.
# from collections import ChainMap
# numbers = {'one': 1, 'two': 2}
# letters = {'a': 'A', 'b': 'B'}
# alpha_num = ChainMap(numbers, letters)
# print(alpha_num)
# alpha_num['c'] = 'C'
# print(alpha_num)
# alpha_num['b'] = 'b'
# print(alpha_num)
# alpha_num.pop('two')
# print(alpha_num)
# del alpha_num['c']
# print(alpha_num)
# alpha_num.clear()
# print(alpha_num)
# выводит:
# ChainMap({'one': 1, 'two': 2}, {'a': 'A', 'b': 'B'})
# ChainMap({'one': 1, 'two': 2, 'c': 'C'}, {'a': 'A', 'b': 'B'})
# ChainMap({'one': 1, 'two': 2, 'c': 'C', 'b': 'b'}, {'a': 'A', 'b': 'B'})
# ChainMap({'one': 1, 'c': 'C', 'b': 'b'}, {'a': 'A', 'b': 'B'})
# ChainMap({'one': 1, 'b': 'b'}, {'a': 'A', 'b': 'B'})
# ChainMap({}, {'a': 'A', 'b': 'B'})
#
#
# можем объединять их с помощью словарного метода update()
# for_adoption = {'dogs': 15, 'cats': 8, 'pythons': 9}
# vet_treatment = {'hamsters': 2, 'tigers': 3}
# pets = {}
# pets.update(for_adoption)
# pets.update(vet_treatment)
#
# len() возвращает количество уникальных ключей ChainMap


#
#  - maps
# возвращает словарь
# При создании пустого ChainMap объекта его атрибут maps будет содержать пустой словарь
# from collections import ChainMap
# for_adoption = {'dogs': 15, 'cats': 8, 'pythons': 9}
# vet_treatment = {'dogs': 7, 'cats': 2, 'tigers': 3}
# pets = ChainMap(for_adoption, vet_treatment)
# print(pets)
# print(pets.maps)
# print(type(pets.maps))
# выводит:
# ChainMap({'dogs': 15, 'cats': 8, 'pythons': 9}, {'dogs': 7, 'cats': 2, 'tigers': 3})
# [{'dogs': 15, 'cats': 8, 'pythons': 9}, {'dogs': 7, 'cats': 2, 'tigers': 3}]
# <class 'list'>
#
#  - new_child(m=None)
# возвращает новый объект ChainMap()
# содержащий новый словарь m, за которым следуют все словари текущего объекта:
#
# если указан словарь m, то он вставляется первым
# в списке существующих словарей текущего объекта ChainMap
#
# если m не указан, то используется пустой словарь, который также вставляется первым
#
# from collections import ChainMap
# dad = {'name': 'Timur', 'age': 29}
# mom = {'name': 'Rosaly', 'age': 28}
# old_family = ChainMap(dad, mom)
# son = {'name': 'Soslan', 'age': 0}
# new_family = old_family.new_child(son)
# print(old_family)
# print(new_family)
# выводит:
# ChainMap({'name': 'Timur', 'age': 29}, {'name': 'Rosaly', 'age': 28})
# ChainMap({'name': 'Soslan', 'age': 0}, {'name': 'Timur', 'age': 29}, {'name': 'Rosaly', 'age': 28})
#
# from collections import ChainMap
# dad = {'name': 'Timur', 'age': 29}
# mom = {'name': 'Rosaly', 'age': 28}
# old_family = ChainMap(dad, mom)
# new_family = old_family.new_child()
# print(old_family)
# print(new_family)
# выводит:
# ChanMap({'name': 'Timur', 'age': 29}, {'name': 'Rosaly', 'age': 28})
# ChainMap({}, {'name': 'Timur', 'age': 29}, {'name': 'Rosaly', 'age': 28})
#
#
#
#  -  parents
# возвращает новый объект ChainMap, содержащий все словари, кроме первого.
# from collections import ChainMap
# dad = {'name': 'Timur', 'age': 29}
# mom = {'name': 'Rosaly', 'age': 28}
# son = {'name': 'Soslan', 'age': 0}
# family = ChainMap(son, dad, mom)
# print(family)
# print(family.parents)
# print(type(family.parents))
# выводит:
# ChainMap({'name': 'Soslan', 'age': 0}, {'name': 'Timur', 'age': 29}, {'name': 'Rosaly', 'age': 28})
# ChainMap({'name': 'Timur', 'age': 29}, {'name': 'Rosaly', 'age': 28})
# <class 'collections.ChainMap'>


























