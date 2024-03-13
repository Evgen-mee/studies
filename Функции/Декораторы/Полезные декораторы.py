#  - измерения времени работы функции
# вычисляет время непосредственно перед запуском функции
# и сразу после ее завершения и выводит разницу подсчитанных времен
# import functools, time
# def timer(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         val = func(*args, **kwargs)
#         end = time.perf_counter()
#         work_time = end - start
#         print(f'Время выполнения {func.__name__}: {round(work_time, 4)} сек.')
#         return val
#     return wrapper
#
# @timer
# def test(n):
#     return sum([(i/99)**2 for i in range(n)])
#
# @timer
# def sleep(n):
#     time.sleep(n)
#
# res1 = test(10000)
# res2 = sleep(4)
#
# print(f'Результат функции test = {res1}')
# print(f'Результат функции sleep = {res2}')
#
#
# отслеживания количества вызовов функции
# может отслеживать состояние вызова функции
# import functools
#
# def counter(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         wrapper.num += 1
#         print(f'Вызов {func.__name__}: {wrapper.num}')
#         val = func(*args, **kwargs)
#         return val
#     wrapper.num = 0
#     return wrapper
#
# @counter
# def greet(name):
#     return f'Hello {name}!'
#
# print(greet('Timur'))
# print(greet('Ruslan'))
# print(greet('Arthur'))
# print(greet('Gvido'))
#
# замедления времени выполнения функции
# добавляет задержку выполнения программы в 1 секунду,
# прежде чем вызовет декорируемую функцию.
#  import functools
#  import time
#
#  def slow_down(func):
#      @functools.wraps(func)
#      def wrapper(*args, **kwargs):
#          time.sleep(1)
#          return func(*args, **kwargs)
#
#      return wrapper
#
#  @slow_down
#  def countdown(number):
#      if number < 1:
#          print('Конец!')
#      else:
#          print(number)
#          countdown(number - 1)
#
#  countdown(5)

