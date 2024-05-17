# Тип Counter является подтипом типа dict,
# специально разработанный для подсчета хешируемых объектов в Python.
# Counter хранит объекты в качестве ключей, а их количество — в качестве значений.
#
# можем преобразовать объект типа Counter в обычный словарь с помощью функции dict()
#
# fromkeys() НЕ РАБОТАЕТ
#
# можно сравнивать между собой
#
# Если обратиться по ключу, которого нет в Counter словаре,
# то ошибка KeyError возникать не будет.
# Будет возвращено нулевое значение.
# При этом ключ создан не будет.
#
#
# from collections import Counter
# counter = Counter('mississippi')     # создаем счетчик на основе строки
# print(counter)
# выводит:
# Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
#
#
# можем создавать объекты типа Counter,
# явно указывая начальные значения количества объектов.
# from collections import Counter
# counter1 = Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
# counter2 = Counter(i=4, s=4, p=2, m=1)
# print(counter1)
# print(counter2)
# выводит:
# Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
# Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
#
#  - update()
# Для изменения объектов типа Counter
# не заменяет значения как у обычных словарей!!!
# суммирует существующие значения
# для новых объектов  создает новые пары
#
# принимает любой итерируемый объект: список, строку, кортеж
# можем передавать другой объект типа Counter, либо обычный словарь
#
# from collections import Counter
# letters = Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
# print(letters)
# letters.update('missouri')
# print(letters)
# выводит:
# Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
# Counter({'i': 6, 's': 6, 'p': 2, 'm': 2, 'o': 1, 'u': 1, 'r': 1})
#
#
# если значения по ключам будут иметь тип, отличный от числового,
# но при этом допускающий сложение (например, строки),
# то ошибок при вызове метода update() возникать не будет.
# from collections import Counter
# counter1 = Counter(i=4, s='4')
# counter2 = Counter(i=5, s='5')
# counter1.update(counter2)
# print(counter1)
# выводит:
# Counter({'i': 9, 's': '54'})


from itertools import chain
x ="123"
print("".join(*chain.from_iterable(zip(x,x))))