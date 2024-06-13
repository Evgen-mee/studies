#  - partial()
# у partial объекта нет явных атрибутов __name__ и __doc__ от начальной функции (вызов приведет к ошибке)
# возвращает partial объект, который при вызове ведет себя как функция
# Сигнатура функции partial(func, *args, **kwargs)
# возвращает специальный partial объект,
# который при вызове вызывается как функция func
# Функция partial() возвращает partial объект, который при вызове ведет себя как функция
# from functools import partial
# def multiply(a, b):
#     return a * b
# double = partial(multiply, 2) #partial объект в качестве первого аргумента передали число 2
# triple = partial(multiply, 3) #partial объект в качестве первого аргумента передали число 3
# print(double(5))        # 2 * 5
# print(triple(10))       # 3 * 10
# мы зафиксировали только один аргумент,
# поэтому новые partial объекты  (double,triple)
# теперь ожидают только один аргумент
#
# зафиксировать оба аргумента в функции multiply()
# multiply_two_and_five = partial(multiply, 2, 5)
# print(multiply_two_and_five())   # вызываем уже без аргументов
#
#
#  - partial содержат три полезных атрибута
# func — исходная функция
# args — зафиксированные позиционныеаргументы(тип tuple)
# keywords — зафиксированные менованные аргументы(типdict)
# from functools import partial
# def pretty_print(text, symbol, count):
#     print(symbol * count)
#     print(text)
#     print(symbol * count)
#
# star_pretty_print = partial(pretty_print, 'Hi!!!', symbol='*')
# star_pretty_print(count=7)
# print(star_pretty_print.args)
# print(star_pretty_print.keywords)
# star_pretty_print.func('Исходная функция', symbol='~', count=20)
#
# выводит:
# *******
# Hi!!!
# *******
# ('Hi!!!',)
# {'symbol': '*'}
# ~~~~~~~~~~~~~~~~~~~~
# Исходная функция
# ~~~~~~~~~~~~~~~~~~~~


#  - update_wrapper()
# partial() работает подобно декоратору
# нет явных атрибутов __name__ и __doc__ от начальной функции
# доступ к этим атрибутам возможен только через исходную функцию с помощью атрибута func.
# from functools import partial
# def multiply(a, b):
#     '''Функция перемножает два числа и возвращает вычисленное значение.'''
#     return a * b
# double = partial(multiply, 2)
# print(double.func.__name__)  # multiply
# print(double.func.__doc__)   # Функция перемножает два числа и возвращает вычисленное значение.
#
# можно скопировать и добавить 1 Атрибуты __name__ и __doc__ из исходной функции в partial объект.
# from functools import partial, update_wrapper
# def multiply(a, b):
#     '''Функция перемножает два числа и возвращает вычисленное значение.'''
#     return a * b
# double = partial(multiply, 2)
# update_wrapper(double, multiply)   # копируем информацию из функции multiply в partial объект double
#
# print(double.__name__) # multiply
# print(double.__doc__)  # Функция перемножает два числа и возвращает вычисленное значение.

# функция partial() лишь запоминает функцию и набор позиционных и именованных аргументов для нее,
# тем самым позволяя вызывать исходную функцию с меньшим количеством аргументов.
# Когда мы вызываем полученный объект partial, он вызывает исходную функцию,
# сначала передавая все сохраненные позиционные аргументы, затем все позиционные аргументы,
# указанные при текущем вызове, затем все сохраненные именованные аргументы,
# затем все именованные аргументы, указанные при текущем вызове:
#
# from functools import partial
# def func1(a, b, c, d, e):
#     return a + b + c + d + e
# func2 = partial(func1, 1, 2)
# func2(3, 4, 5)                      # эквивалентно func1(1, 2, 3, 4, 5)
#
# func3 = partial(func1, d=4, e=5)
# func3(1, 2, 3)                      # эквивалентно func1(1, 2, 3, d=4, e=5)
#
# func4 = partial(func1, 1, e=5)
# func4(2, 3, d=4)                    # эквивалентно func1(1, 2, 3, d=4, e=5)
#
# func5 = partial(func1, a=1, b=2)
# func5(3, 4, 5)                      # эквивалентно func1(3, 4, 5, a=1, b=2), что приводит к ошибке, так как a и b переданы дважды



# Кэширование и мемоизация
# Кэширование – это способ оптимизации хранения данных, при котором операции с данными производятся эффективнее.
# Мемоизация — это разновидность кэширования.
# Обычно под кэшированием понимают довольно широкий набор способов сохранения чего-либо
# для последующего использования. Мемоизация же означает кэширование возвращаемых значений функций.

#  - для того чтобы функцию можно было подвергнуть мемоизации, она должна быть чистой
#  - мемоизация — это компромисс между производительностью и потреблением памяти
# мемоизация хороша для функций, имеющих сравнительно небольшой диапазон входных значений, что позволяет достаточно
# часто, при повторных вызовах функций, задействовать значения, найденные ранее,
# не тратя на хранение данных слишком много памяти
#  - лучше всего функции с мемоизацией показывают себя там, где выполняются сложные, ресурсоёмкие вычисления
#
# При такой реализации функции fib() сначала происходит проверка на наличие уже вычисленного элемента,
# и если он находится, то сразу возвращается его значение.
# def fib(n):
#     cache = {1: 1, 2: 1}
#     def fib_rec(n):
#         result = cache.get(n)
#         if result is None:
#             result = fib_rec(n - 2) + fib_rec(n - 1)
#             cache[n] = result
#         return result
#     return fib_rec(n)
#
# декоратор общего типа, мемоизирующий любую чистую функцию:
# import functools
# def cached(func):
#     cache = {}
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         key = args + tuple(kwargs.items())
#         result = cache.get(key)
#         if result is None:
#             result = func(*args, **kwargs)
#             cache[key] = result
#         return result
#     return wrapper
#
# проблема: содержимое словаря cache будет
# неограниченно расти при каждом вызове декорируемой функции с новыми аргументами
#
# Стратегии кэширования
# для удаления элементов из кэша и предотвращения превышения его максимального размера
#
# Стратегия 	                       Какую запись удаляем 	        Эти записи чаще других используются повторно
# First-In, First-Out (FIFO) 	           самую старую 	                            новые
# Last-In, First-Out (LIFO) 	           самую недавнюю 	                            старые
# Least Recently Used (LRU) 	которая использовалась наиболее давно 	           недавно прочитанные
# Most Recently Used (MRU) 	которая использовалась последней 	               прочитанные первыми
# Least Frequently Used (LFU) 	которая использовалась наиболее редко 	   которые использовались часто

#
# Декоратор lru_cache
# дает возможность кэшировать результат вычисления функции,
# используя стратегию Least Recently Used
# from functools import lru_cache
# #добавляет кэширование к функции fibonacci()
# @lru_cache()            #cохраняет результаты вызова fibonacci() для каждого уникального значения аргумента
# def fibonacci(n):
#     if n <= 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
# Аргументы декоратора lru_cache
#  - maxsize=128 — максимальный размер кэша (тип int)
# Если для параметра maxsize установлено значение None, то кэш может расти без ограничений
#
#  - typed=False — как кэшировать при разных типах аргументов (тип bool)
# Если для typed задано значение True, то результаты вызовов функции для аргументов
# разных типов будут кэшироваться отдельно.
# Например, f(3) и f(3.0) будут рассматриваться как отдельные вызовы
# с разными результатами. Если для typed задано значение False,
# то вызовы будут рассматриваться как одинаковые.
#
# from functools import lru_cache
#
# @lru_cache(typed=False)
# def concat(text, num):
#     return text + ' ' + str(num)
#
# print(concat('beegeek', 4))    # beegeek 4
# print(concat('beegeek', 5.0))  # beegeek 5.0
# print(concat('beegeek', 4.0))  # beegeek 4      использует закэшированный результат первого вызова
#
#
# метод cache_info()
# озвращает именованный кортеж, показывающий hits, misses, maxsize и currsize
#  - hits – количество значений, которые lru_cache вернул непосредственно из памяти,
# поскольку они присутствовали в кэше
#  - misses – количество значений, которые были вычислены, а не взяты из памяти
#  - maxsize – это размер кэша, который мы определили, передав его декоратору
#  - currsize – текущий размер кэша
# from functools import lru_cache
# @lru_cache(typed=False)
# def concat(text, num):
#     return text + ' ' + str(num)
# print(concat('beegeek', 1))    # beegeek 1
# print(concat('beegeek', 1.0))  # beegeek 1
# print(concat('beegeek', True)) # beegeek 1
# print(concat('beegeek', 4.0))  # beegeek 4.0
# print(concat('beegeek', 5))    # beegeek 5
# print(concat.cache_info())  # CacheInfo(hits=2, misses=3, maxsize=128, currsize=3)
#
#
# cache_clear() для очистки кэша
# from functools import lru_cache
# @lru_cache(typed=False)
# def concat(text, num):
#     return text + ' ' + str(num)
# print(concat('beegeek', 1))     # beegeek 1
# print(concat('beegeek', 1.0))   # beegeek 1
# print(concat('beegeek', True))  # beegeek 1
# print(concat('beegeek', 4.0))   # beegeek 4.0
# print(concat('beegeek', 5))     # beegeek 5
# print(concat.cache_info())                # CacheInfo(hits=2, misses=3, maxsize=128, currsize=3)
# concat.cache_clear()                      # очистили кэш
# print(concat.cache_info())                # CacheInfo(hits=0, misses=0, maxsize=128, currsize=0)





