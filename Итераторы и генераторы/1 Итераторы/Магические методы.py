# У всех итерируемых объектов есть магический метод __iter__(),
# который преобразует итерируемый объект в итератор.
# iter() вызывает за кулисами именно этот магический метод
# words = ['hello', 'beegeek', 'python']
# iterator = iter(words)      # за кулисами вызывается метод words.__iter__()
# print(type(words))
# print(type(iterator))
#
# У всех итераторов есть магический метод __next__()
# обеспечивает выдачу очередного элемента
# ords = ['hello', 'beegeek', 'python']
# iterator = iter(words)      # за кулисами вызывается метод words.__iter__()
# print(next(iterator))       # за кулисами вызывается метод iterator.__next__()
# print(next(iterator))       # за кулисами вызывается метод iterator.__next__()
#
#
# метод __iter__(), который возвращает сам итератор (сам себя)
# любой итератор является итерируемым объектом
# Задача метода __iter__() – превращать итерируемый объект в итератор
# ords = ['hello', 'beegeek', 'python']
# iterator1 = iter(words)          # за кулисами вызывается метод words.__iter__()
# iterator2 = iter(iterator1)      # за кулисами вызывается метод iterator1.__iter__()
#
# если функции iter() передается итератор, то она возвращает его же
# если передать коллекцию то вернется итератор на основе этого итерируемого объекта.
#
# Если циклу for передается не итератор, а итерируемый объект, то его метод __iter__() должен возвращать не сам объект,
# а итератор на основе этого итерируемого объекта.
#
#
# Протокол итератора
# Любой итерируемый объект реализует протокол итератора.
#  - чтобы получить итератор, мы должны передать функции iter() итерируемый объект
#  - любой объект, передаваемый функции next() без исключения TypeError — итератор
#  - любой объект, передаваемый функции iter() и возвращающий сам себя — итератор
#
#
# Особенность функции iter()
# стандартное использование:
# iter() преобразует итерируемый объект в итератор
# в таком виде функция используется в большинстве случаев.
# iter(iterable) -> iterator
#
# с двумя аргументами:
# iter(callable, sentinel) -> iterator
# callable -  должен являться функцией
# sentinel — некоторым стоп-значением
#
# созданный итератор будет вызывать указанную функцию callable
# и проверять полученное значение на равенство со значением sentinel
# Если полученное значение равно sentinel, то возбуждается исключение StopIteration
# иначе итератор выдает значение, полученное из функции callable
#
# генерирует неопределенное количество случайных чисел:
# from random import choice
# def test_iter():
#     values = list(range(1, 11))
#     return choice(values)
# random_iterator = iter(test_iter, 2)
# for num in random_iterator:  # Будет генерировать случайное число от 11 до 1010 до тех пор, пока не будет возвращено число 22
#     print(num)
#
# считывает строки текстового файл ДатаВремя.txt до тех пор, пока очередная строка не окажется пустой.
# with open('ДатаВремя.txt') as file:
#     for line in iter(file.readline, ''):    # читаем, пока не попадется пустая строка
#         # Делаем что-то с line.




# __init__()
#
#
# class Counter:
#     def __init__(self, low, high):  # конструктор принимает два аргумента low и high (помимо self)
#         self.low = low
#         self.high = high
#
#     def __iter__(self):  # возвращает ссылку на сам итератор для поддержания протокола итератора
#         return self
#
#     def __next__(self):  # возвращает следующий элемент или возбуждает исключение StopIteration
#         if self.low > self.high:
#             raise StopIteration
#         else:
#             self.low += 1
#             return self.low - 1
#
# counter1 = Counter(3, 10)  # создаем итератор Counter, передавая значения low=3, high=10
# for i in counter1:  # неявно вызываем функцию next()
#     print(i)
# counter2 = Counter(100, 103)  # создаем итератор Counter, передавая значения low=100, high=103
# print(next(counter2))  # явно вызываем функцию next()
# print(next(counter2))  # явно вызываем функцию next()
#
# бесконечный итераторEvenNumbers
# генерирует последовательность всех целых четных чисел от значения begin
#
# class EvenNumbers:
#     def __init__(self, begin):  # конструктор принимает один аргумент begin (помимо self)
#         self.begin = begin + begin % 2
#
#     def __iter__(self):        # возвращает ссылку на сам итератор для поддержания протокола итератора
#         return self
#
#     def __next__(self):        # возвращает следующий элемент или возбуждает исключение StopIteration
#         value = self.begin
#         self.begin += 2
#         return value
# evens1 = EvenNumbers(10)  # все четные числа от 10 до бесконечности
# for index, num in enumerate(evens1):
#     if index > 5:
#         break
#     print(num)
# evens2 = EvenNumbers(101)  # все четные числа от 102 до бесконечности
#
# Все указанные типы итераторов следуют общепринятому в Python протоколу.
#
# class list_iterator:
#     def __init__(self, ДатаВремя):
#         self.ДатаВремя = ДатаВремя
#         self.index = -1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.index += 1
#         if self.index == len(self.ДатаВремя):
#             raise StopIteration
#         return self.ДатаВремя[self.index]


