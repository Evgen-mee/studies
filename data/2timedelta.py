# Тип данных timedelta
# разница между двумя объектами datetime или date
#
# все аргументы являются необязательными и по умолчанию равны 0
#
# Аргументы могут быть целыми числами или числами с плавающей запятой,
# а также могут быть как положительными, так и отрицательными
#
# внутренне хранит только сочетание days, seconds, microseconds,
# а остальные переданные в конструктор аргументы конвертируются в эти единицы:
# milliseconds преобразуется в 1000
# minutes преобразуется в 60 seconds
# hours преобразуется в 3600 seconds
# weeks преобразуется в 7 days
#
# Операторы сравнения == или != всегда возвращают значение bool,
# независимо от типа сравниваемого объекта
# Для всех других операторов
# операторов с объектом другого типа, возникает ошибка (исключение) TypeError

# При создании объекта timedelta можно указать следующие аргументы:
# недели - (weeks)
# дни - (days)
# часы - (hours)
# минуты - (minutes)
# секунды - (seconds)
# миллисекунды - (milliseconds)
# микросекунды - (microseconds)
#
# from datetime import timedelta
# delta = timedelta(days=7, hours=20, minutes=7, seconds=17)
# print(delta)       == 7 days, 20:07:17
# print(type(delta)) == <class 'datetime.timedelta'>


# Атрибуты
# from datetime import timedelta
# delta = timedelta(days=50, seconds=27, microseconds=10, milliseconds=29000, minutes=5, hours=8, weeks=2)
# print('Количество дней =', delta.days)                     # Количество дней = 64
# print('Количество секунд =', delta.seconds)                # Количество секунд = 29156
# print('Количество микросекунд =', delta.microseconds)      # Количество микросекунд = 10
# print('Общее количество секунд =', delta.total_seconds())  # Общее количество секунд = 5558756.00001
#
# нет атрибутов hours и minutes!!!!
# Достать часы и минуты можно так:
# def hours_minutes(td):
#     return td.seconds // 3600, (td.seconds // 60) % 60
#
# from datetime import timedelta
# def hours_minutes(td):
#     return td.seconds // 3600, (td.seconds // 60) % 60
#
# delta = timedelta(days=7, seconds=125, minutes=10, hours=8, weeks=2)
# hours, minutes = hours_minutes(delta)
# print(delta)    # 21 days, 8:12:05
# print(hours)    # 8
# print(minutes)  # 12


# функции str() и repr()
# для преобразования объектов типа timedelta к строковому типу.
# from datetime import timedelta
# delta1 = timedelta(weeks=1, hours=23, minutes=61)
# delta2 = timedelta(minutes=-300)
# print(str(delta1), str(delta2), sep='\n')     # 8 days, 0:01:00     -1 day, 19:00:00
# print(repr(delta1), repr(delta2), sep='\n')   #datetime.timedelta(days=8, seconds=60)    datetime.timedelta(days=-1, seconds=68400)
#
#
# функция abs()
# возвращает объект timedelta с положительным значением всех атрибутов
# from datetime import timedelta
# delta = timedelta(days=-2, minutes=-300)
# abs_delta = abs(delta)
# print('Исходная:', delta.days, delta.seconds, delta, sep='\n')
# print('С модулем:', abs_delta.days, abs_delta.seconds, abs_delta, sep='\n')

# "15:00" в сразу в объект timedelta
# from datetime import timedelta, time
# s = '15:00'
# # Вариант 1
# hour, minute = map(int, s.split(':'))
# delta1 = timedelta(hours=hour, minutes=minute)
# print(delta1)  # 15:00:00
# # Вариант 2
# t = time.fromisoformat(s)
# delta2 = timedelta(hours=t.hour, minutes=t.minute)
# print(delta2)  # 15:00:00

# Пример вычетание времени из даты
# from datetime import datetime, timedelta
# pattern, td = '%d.%m.%Y', timedelta(days=1)
# dt = datetime.strptime(input(), pattern)
# print((dt - td).strftime(pattern))
# print((dt + td).strftime(pattern))

# Делаем список datetaime из обычного списка с помощью мап
# from datetime import datetime, timedelta
# dates = input().split()
# x = list(map(datetime.strptime,dates, ('%d.%m.%Y',) * len(dates)))
# print(x)

# datetime.combine(date.min,data.time()) - datetime.min
# Приводит time к timedelta.