# Тип Counter является подтипом типа dict,
# специально разработанный для подсчета хешируемых объектов в Python.
# Counter хранит объекты в качестве ключей, а их количество — в качестве значений.

# Ключами словаря должны быть хешируемые значения (неизменяемые объекты)

# можем преобразовать объект типа Counter в обычный словарь с помощью функции dict()

# fromkeys() НЕ РАБОТАЕТ

# можно сравнивать между собой

# Если обратиться по ключу, которого нет в Counter словаре,
# то ошибка KeyError возникать не будет.
# Будет возвращено нулевое значение.
# При этом ключ создан не будет.


# from collections import Counter
# counter = Counter('mississippi')     # создаем счетчик на основе строки
# print(counter)                       # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})


# можем создавать объекты типа Counter, явно указывая начальные значения количества объектов.
# from collections import Counter
# counter1 = Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
# counter2 = Counter(i=4, s=4, p=2, m=1)
# print(counter1)                     # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
# print(counter2)                     # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

from collections import Counter
print(Counter(sorted(map(int, input()))).items(), sep='\n')