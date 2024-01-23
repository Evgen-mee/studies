# - бычно используется при работе с текущим временем.
#
# - С его помощью можно получать информацию о текущих дате и времени,
# выводить эти сведения в необходимом формате, а также управлять ходом
# выполнения программы, добавляя задержки по таймеру.
#
# дает возможность:
# отображать информацию о времени, прошедшем с начала эпохи
# преобразовывать значение системного времени к удобному виду
# прерывать выполнение программы (установка паузы) на заданное количество секунд
# измерять время выполнения программы целиком или ее отдельных модулей
#
# если требуется сравнивать или производить арифметические операции со временем,
# то нужно использовать модуль datetime, а не time
#
#
# функция time()
# import time
# seconds = time.time()    # получаем количество прошедших секунд в виде float числа
# print('Количество секунд с начала эпохи =', seconds)
#
#
# функция time_ns()
# возвращает целочисленное значение, представляющее то же время,
# прошедшее с эпохи, но в наносекундах, а не в секундах.
#
#
# функция ctime()
# принимает в качестве аргумента количество секунд, прошедших с начала эпохи,
# и возвращает строку, представляющую собой местное (локальное) время.
# import time
# seconds = 1630387918.354396
# local_time = time.ctime(seconds)
# print('Местное время:', local_time) == Местное время: Tue Aug 31 08:31:58 2021
#
# Вызывать функцию ctime() можно и без аргументов,
# в этом случае в качестве аргумента подставляется значение вызова функции time()
# import time
# local_time = time.ctime()              # вызов функции без аргумента
# print('Местное время:', local_time)
#
# равнозначен коду:
#
# import time
# seconds = time.time()
# local_time = time.ctime(seconds)
# print('Местное время:', local_time)
#
# результат работы функции ctime() зависит от вашего географического положения
#
#
# Функция sleep()
# используется для добавления задержки в выполнении программы.
# Эта функция принимает в качестве аргумента количество секунд (secs)
# и добавляет задержку в выполнении программы на указанное количество секунд
#
# import time
# print('Before the sleep statement')
# time.sleep(3)
# print('After the sleep statement')
#
# Аргумент secs может быть числом с плавающей точкой (float),
# для указания более точного времени приостановки
#
# import time
# print('Before the sleep statement')
# time.sleep(0.7)
# print('After the sleep statement')
#
# может потребоваться задержка на разное количество секунд.
# Сделать это можно следующим образом:
# import time
# for i in [0.7, 0.5, 1.0, 2.5, 3.3]:
#     print(f'Waiting for {i} seconds')
#     time.sleep(i)
# print('The end')


# time() для получения текущего времени,
# чтобы в итоге выявить, как долго работал блок кода
#
# import time
# start_time = time.time()
# for i in range(5):
#     print(i)
#     time.sleep(1)
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f'Время работы программы = {elapsed_time}')
#
#
# Функция monotonic()
# дает результат, который обладает гарантированной точностью и не зависит от внешних условий
#
# Функция monotonic_ns() похожа на monotonic(),
# но возвращает время в наносекундах.
# Работает не на всех операционных системах.
# import time
# start_time = time.monotonic()
# for i in range(5):
#     print(i)
#     time.sleep(0.5)
# end_time = time.monotonic()
# elapsed_time = end_time - start_time
# print(f'Время работы программы = {elapsed_time}')
#
#
# Функция perf_counter()
# Для самого точного измерения времени выполнения программы
# import time
# start_time = time.perf_counter()
# for i in range(5):
#     print(i)
#     time.sleep(1)
# end_time = time.perf_counter()
# elapsed_time = end_time - start_time
# print(f'Время работы программы = {elapsed_time}')
#
# perf_counter_ns() – работает так же, но длительность выводится в наносекундах,


# Тип данных struct_time
# является именованным кортежем, представляющий информацию о времени
#
# Именованные кортежи подобны обычным кортежам за тем исключением,
# что к их полям можно обращаться не только по индексу, но и по названию
#
# кортеж struct_time состоит из следующих атрибутов
# Номер индекса  	Атрибут	Значение
# 0	tm_year	диапазон от 0000 до 9999
# 1	tm_mon	диапазон от 1 до 12
# 2	tm_mday	диапазон от 1 до 31
# 3	tm_hour	диапазон от 0 до 23
# 4	tm_min	диапазон от 0 до 59
# 5	tm_sec	диапазон от 0 до 61
# 6	tm_wday	диапазон от 0 до 6, понедельник = 0
# 7	tm_yday	диапазон от 1 до 366
# 8	tm_isdst	значения -1, 0, 1
# N/A	tm_zone	сокращение названия часового пояса
# N/A	tm_gmtoff	смещение к востоку от UTC в секундах
#
#
# Создавать объекты типа struct_time можно на основе кортежа
# import time
# time_tuple = (2021, 8, 31, 5, 31, 58, 1, 243, 0)
# time_obj = time.struct_time(time_tuple)
#
# Функция localtime()
# принимает в качестве аргумента количество секунд, прошедших с начала эпохи,
# и возвращает кортеж struct_time в локальном времени
#
# mport time
#
# result = time.localtime(1630387918)
# print('Результат:', result)
# print('Год:', result.tm_year)
# print('Месяц:', result.tm_mon)
# print('День:', result.tm_mday)
# print('Час:', result.tm_hour)
#
# выводит:
#
# Результат: time.struct_time(tm_year=2021, tm_mon=8, tm_mday=31, tm_hour=8, tm_min=31, tm_sec=58, tm_wday=1, tm_yday=243, tm_isdst=0)
# Год: 2021
# Месяц: 8
# День: 31
# Час: 8
#
#
# Функция gmtime()
# ринимает в качестве аргумента количество секунд, прошедших с начала эпохи,
# и возвращает кортеж struct_time в UTC.
#
# import time
#
# result = time.gmtime(1630387918)
# print('Результат:', result)
# print('Год:', result.tm_year)
# print('Месяц:', result.tm_mon)
# print('День:', result.tm_mday)
# print('Час:', result.tm_hour)
#
# выводит:
#
# Результат: time.struct_time(tm_year=2021, tm_mon=8, tm_mday=31, tm_hour=5, tm_min=31, tm_sec=58, tm_wday=1, tm_yday=243, tm_isdst=0)
# Год: 2021
# Месяц: 8
# День: 31
# Час: 5
#
# Функция mktime()
# принимает struct_time (или кортеж, содержащий 9 значений, относящихся к struct_time)
# в качестве аргумента и возвращает количество секунд,
# прошедших с начала эпохи, в местном времени.
#
# import time
#
# time_tuple = (2021, 8, 31, 5, 31, 58, 1, 243, 0)
# time_obj = time.mktime(time_tuple)
# print('Локальное время в секундах:', time_obj)
# выводит:
#
# Локальное время в секундах: 1630377118.0
#
# Функция mktime() является обратной к функции localtime().
# Следующий пример показывает их связь:
# import time
# seconds = 1630377118
# time_obj = time.localtime(seconds)            # возвращает struct_time
# print(time_obj)
# time_seconds = time.mktime(time_obj)          # возвращает секунды из struct_time
# print(time_seconds)
# и выводит:
# time.struct_time(tm_year=2021, tm_mon=8, tm_mday=31, tm_hour=5, tm_min=31, tm_sec=58, tm_wday=1, tm_yday=243, tm_isdst=0)
# 1630377118.0
#
#
# Функция asctime()
# ринимает struct_time (или кортеж, содержащий начений, относящихся к struct_time)
# в качестве аргумента и возвращает строку, представляющую собой дату и время.
# import time
# time_tuple = (2021, 8, 31, 5, 31, 58, 1, 243, 0)
# result = time.asctime(time_tuple)
# print('Результат:', result)
# выводит:
# Результат: Tue Aug 31 05:31:58 2021

