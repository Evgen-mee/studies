# МНОЖЕСТВА это не упарядоченная коллекция уникальных (нет дубдей) элементов
# используют для того что бы убрать дубли
# может работать только с неизменяемыми типами данных
# числа, bool, строки, кортежи с остальными выдаст ошибку
# множество уберает дубли
# не можем обратиться по индексу

# создать множество a = {1,2,3,4,5} или a = set([1,2,3,])

# Методы issuperset(), issubset(), isdisjoint() могут принимать
# в качестве аргумента не только множество (тип данных set),
# но и любой итерируемый объект (список, строку, кортеж...).
# Сами же эти методы могут применяться только ко множеству (тип данных set)
# или замороженному множеству (тип данных frozenset).
#
# метод issubset() - возвращает значение True, если одно множество является подмножеством другого
# или <=
#
# метод issuperset() - возвращает значение True, если одно множество является надмножеством другого
# или >=
#
# метод isdisjoint() - метод возвращает значение True, если множества не имеют общих элементов

# Сравнение множеств по размеру и значению
# a == b вернет bool
# != > <

# метод a.add(7) добавляет значение в множество

# метод a.discard("значение") удаляет элемент по значению
# если передать НЕ существующее значение то не чего не произойдет

# метод a.remove("значение") удаляет элемент по значению
# если передать НЕ существующее значение то вылетит ОШИБКА

# метод x = d.pop() удаляет рандомный элемент из колекции и передает значение удаляемого экземпляра
# есле пременить к пустому множеству то приведет к ошибке

# метод a.update([1,2,3,4,]) добавляет все значения итерируемого обьект


# Все основные операции над множествами выполнятся двумя способами:
# метода
# соответствующего оператора
# Различие в том, что метод может принимать в качестве аргумента не только множество (тип данных set),
# но и любой итерируемый объект (список, строку, кортеж).

# методы (union(), intersection(), difference()) и операторы (|, &, -, ^)
# позволяют совершать операции над несколькими множествами сразу.

# Оператор ^ симметрической разности позволяет использовать несколько множеств,
# а метод symmetric_difference() – нет.

# Объединение множеств это множество, состоящее из элементов, принадлежащих хотя бы одному из объединяемых множеств
# обьеденить два множества
# c = a | b или если сохраняем в a |=b
# или
# метод union() на выходе множество, состоящее из элементов, принадлежащих хотя бы одному из объединяемых множеств
# возвращает новое множество в которое входят все элементы множеств
# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
# myset3 = myset1.union(myset2) = {1, 2, 3, 4, 5, 6, 7, 8}


# Пересечение множеств это множество, состоящее из элементов,
# принадлежащих одновременно каждому из пересекающихся множеств.
# получить пересечение множеств
# a = c & b на выходе получим а = значениям которые есть в c и b
# или
# метод intersection()
# a = c.intersection(b)
# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
# myset3 = myset1.intersection(myset2) = {3, 4}

# Метод intersection_update() -  изменяет исходное множество по пересечению.
# или &=
# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
# myset1.intersection_update(myset2)      # изменяем множество myset1
# myset1 = {3, 4}


# Разность множеств это множество, в которое входят все элементы первого множества,
# не входящие во второе множество.
# вычетание множеств (разность)
# c = a-b в c будут значения из a которых нет в b
# c = a{1,2,4} - b{4,5,6,7,8,}  итого c = {1,2}
# c = b{4,5,6,7,8,} - a{1,2,4}   итого c = {5,6,7,8,}
# сохранить сразу в b   b-=a
# или
# метод difference()
# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
# myset3 = myset1.difference(myset2) = {1, 2, 5}

# Метод difference_update() - изменяет исходное множество по разности.
# или -=
# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
# myset1.difference_update(myset2)      # изменяем множество myset1
# myset1 = {1, 2, 5}


# Симметрическая разность множеств это множество, включающее все элементы исходных множеств,
# не принадлежащие одновременно обоим исходным множествам
# Семитричная разность
# на выходе получаем множество НЕ совпадающих элементов
# c = b{4,5,6,7,8,} ^  a{1,2,4} итого с = {1,2,5,6,7,8}
# или
# метод symmetric_difference()
# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
# myset3 = myset1.symmetric_difference(myset2) = {1, 2, 5, 6, 7, 8}

# Метод symmetric_difference_update() - изменяет исходное множество по симметрической разности.
# или ^=
# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
# myset1.symmetric_difference_update(myset2)      # изменяем множество myset1
# myset1 = {1, 2, 5, 6, 7, 8}


# 2 Генераторы множеств и словарей
# a = {x**2 for i in range(1,5)} на выходе множество a{1,2,3,4}



# Замороженное множество (frozenset) также является встроенной коллекцией в Python.
# Обладая характеристиками обычного множества,
# замороженное множество не может быть изменено после создания.
#
# Для создания замороженного множества используется встроенная функция frozenset(),
# которая принимает в качестве аргумента другую коллекцию.
#
#
# Над замороженными множествами можно производить все операции,
# которые можно производить над обычными множествами:
#
# объединение множеств: метод union() или оператор |;
# пересечение множеств: метод intersection() или оператор &;
# разность множеств: метод difference() или оператор -;
# симметрическая разность множеств: метод symmetric_difference() или оператор ^
#
# Результатом операций над замороженными множествами будут тоже замороженные множества.
#
# Будучи изменяемыми, обычные множества не могут быть элементами других множеств.
# Замороженные множества являются неизменяемыми, а значит могут быть элементами других множеств.

# если проводится операция между обычным множеством и неизменяемым,
# то тип нового множества будет зависеть от того,
# какое множество в выражении было первым:
# set & frozenset
# set - forzenset
# set | frozenset
# set ^ frozenset
# в результате дадут обычное множество
# frozenset & set
# frozenset | set
# frozenset - set
# frozenset ^ set
# результат - неизменяемое множество

