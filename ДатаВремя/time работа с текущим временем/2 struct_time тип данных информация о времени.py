# является именованным кортежем, представляющий информацию о времени

# Именованные кортежи подобны обычным кортежам за тем исключением,
# что к их полям можно обращаться не только по индексу, но и по названию

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


# import time
# time_tuple = (2021, 8, 31, 5, 31, 58, 1, 243, 0)
# time_obj = time.struct_time(time_tuple)


# Функция localtime()
# принимает в качестве аргумента количество секунд, прошедших с начала эпохи,
# и возвращает кортеж struct_time в локальном времени
# import time
# result = time.localtime(1630387918)
# print('Результат:', result)    # Результат: time.struct_time(tm_year=2021, tm_mon=8, tm_mday=31, tm_hour=8, tm_min=31, tm_sec=58, tm_wday=1, tm_yday=243, tm_isdst=0)
# print('Год:', result.tm_year)  # Год: 2021
# print('Месяц:', result.tm_mon) # Месяц: 8
# print('День:', result.tm_mday) # День: 31
# print('Час:', result.tm_hour)  # Час: 8


# Функция gmtime()
# Принимает в качестве аргумента количество секунд, прошедших с начала эпохи,
# и возвращает кортеж struct_time в UTC.
# import time
# result = time.gmtime(1630387918)
# print('Результат:', result)      # Результат: time.struct_time(tm_year=2021, tm_mon=8, tm_mday=31, tm_hour=5, tm_min=31, tm_sec=58, tm_wday=1, tm_yday=243, tm_isdst=0)
# print('Год:', result.tm_year)    # Год: 2021
# print('Месяц:', result.tm_mon)   # Месяц: 8
# print('День:', result.tm_mday)   # День: 31
# print('Час:', result.tm_hour)    # Час: 5


# Функция mktime()
# принимает struct_time (или кортеж, содержащий 9 значений, относящихся к struct_time)
# в качестве аргумента и возвращает количество секунд,
# прошедших с начала эпохи, в местном времени.
# import time
# time_tuple = (2021, 8, 31, 5, 31, 58, 1, 243, 0)
# time_obj = time.mktime(time_tuple)
# print('Локальное время в секундах:', time_obj)  # Локальное время в секундах: 1630377118.0


# Функция mktime() является обратной к функции localtime().
# Следующий пример показывает их связь:
# import time
# seconds = 1630377118
# time_obj = time.localtime(seconds)            # возвращает struct_time
# print(time_obj)                               # time.struct_time(tm_year=2021, tm_mon=8, tm_mday=31, tm_hour=5, tm_min=31, tm_sec=58, tm_wday=1, tm_yday=243, tm_isdst=0)
# time_seconds = time.mktime(time_obj)          # возвращает секунды из struct_time
# print(time_seconds)                           # 1630377118.0


# Функция asctime()
# ринимает struct_time (или кортеж, содержащий начений, относящихся к struct_time)
# в качестве аргумента и возвращает строку, представляющую собой дату и время.
# import time
# time_tuple = (2021, 8, 31, 5, 31, 58, 1, 243, 0)
# result = time.asctime(time_tuple)
# print('Результат:', result)       # Результат: Tue Aug 31 05:31:58 2021

