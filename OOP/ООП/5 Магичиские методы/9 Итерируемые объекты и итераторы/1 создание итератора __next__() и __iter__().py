# for за кулисами вызывает один раз метод __iter__() у итерируемого объекта для получения итератора,
# а затем метод __next__() до тех пор, пока не будет возбуждено исключение StopIteration

# __iter__() — метод,  возвращающий сам итератор
# __next__() — метод, возвращающий следующий элемент итератора или возбуждающий исключение StopIteration


# генерируем последовательность целых чисел от low до high включительно с шагом один
# class Counter:
#     def __init__(self, low, high):
#         self.low = low
#         self.high = high
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.low > self.high:
#             raise StopIteration
#         self.low += 1
#         return self.low - 1
#
#
# counter1 = Counter(3, 10)               # создаем итератор Counter, передавая значения low=3, high=10
#
# for i in counter1:                      # неявно вызываем функцию next()
#     print(i)
#
# counter2 = Counter(100, 103)            # создаем итератор Counter, передавая значения low=100, high=103
# print(next(counter2))                   # явно вызываем функцию next()
# print(next(counter2))                   # явно вызываем функцию next()


# class EvenNumbers:
#     def __init__(self, begin):
#         self.begin = begin + begin % 2
#
#     def __iter__(self):
#         return self
#
#     def __next__(self) # итератор является бесконечным, так как метод не возбуждает исключение StopIteration
#         value = self.begin
#         self.begin += 2
#         return value
#
#
# evens1 = EvenNumbers(10)  # все четные числа от 10 до бесконечности
#
# for index, num in enumerate(evens1):
#     if index > 5:
#         break
#     print(num)
#
# evens2 = EvenNumbers(101)  # все четные числа от 102 до бесконечности

