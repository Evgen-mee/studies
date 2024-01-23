# Функции высшего порядка
# – это функции, которые принимают и/или возвращают другие функции.
# def speak(text):
#     def whisper(t):                      # объявляем вложенную функцию
#         return t.lower() + '...'
#     return whisper(text)                 # вызываем вложенную функцию и возвращаем ее результат
#
# print(speak('Hello, World'))
#
# Каждый раз, когда мы вызываем функцию speak(),
# она определяет новую внутреннюю функцию whisper(), а затем вызывает ее.
# При этом функция whisper() не существует вне родительской функции speak()
#
#
#
# get_speak_func() определяет две вложенные функции whisper() и yell()
# В зависимости от аргумента volume, переданного родительской функции get_speak_func(),
# она выбирает и возвращает вызывающей стороне одну из вложенных функций:
# def get_speak_func(volume):
#     def whisper(text):
#         return text.lower() + '...'
#     def yell(text):
#         return text.upper() + '!'
#
#     if volume > 0.5:
#         return yell
#     else:
#         return whisper
#
# get_speak_func() на самом деле не вызывает одну из своих вложенных функций
# выбирает подходящую функцию на основе аргумента volume, а затем возвращает объект этой функции.


# Вложенные функции могут захватывать
# и переносить с собой часть состояния родительской функции.
#
# def get_speak_func(text, volume):
#     def whisper():
#         return text.lower() + '...'
#     def yell():
#         return text.upper() + '!'
#     if volume > 0.5:
#         return yell
#     else:
#         return whisper
# whisper() и yell() не имеют параметра text.
# Они его получают и используют через родительскую функцию get_speak_func()
#
#
#
# nonlocal
# Внутренняя функция видит переменные в объемлющей функции,
# но, если она хочет такую переменную изменить, должна объявить ее nonlocal.
#
# def outer_function():
#     num = 5
#     def inner_function():  # определяем вложенную функцию
#         nonlocal num
#         num += 10
#         print(num)
#     inner_function()  # вызываем вложенную функцию
# outer_function()
#
#
# Атрибут __closure__
# Все функции содержат специальный атрибут __closure__
# который представляет из себя кортеж, содержащий данные,
# связанные с вложенными областями видимости,
# то есть с нелокальными переменными.
# def outer_function(arg):
#     num = 5
#     name = 'Timur'
#     numbers = [1, 2, 3]
#     def inner_function():  # определяем вложенную функцию
#         print(arg)
#         print(num)
#         print(numbers)
#     return inner_function  # возвращаем вложенную функцию
#
# inner = outer_function('python')
# for var in inner.__closure__:
#     print(var.cell_contents)
# выводит:
# python
# 5
# [1, 2, 3]
# кортеж __closure__ содержит внутри себя специальный тип данных.
# Для получение самого значения захваченной переменной
# нужно использовать атрибут cell_contents


