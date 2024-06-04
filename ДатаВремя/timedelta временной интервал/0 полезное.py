
# Достать часы и минуты можно так:
# from datetime import timedelta
# def hours_minutes(td):
#     return td.seconds // 3600, (td.seconds // 60) % 60
#
# delta = timedelta(days=7, seconds=125, minutes=10, hours=8, weeks=2)
# hours, minutes = hours_minutes(delta)
# print(delta)    # 21 days, 8:12:05
# print(hours)    # 8
# print(minutes)  # 12


# "15:00" сразу в объект timedelta
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


# функция abs()
# возвращает объект timedelta с положительным значением всех атрибутов
# from datetime import timedelta
# delta = timedelta(days=-2, minutes=-300)
# abs_delta = abs(delta)
# print('Исходная:', delta.days, delta.seconds, delta, sep='\n')
# print('С модулем:', abs_delta.days, abs_delta.seconds, abs_delta, sep='\n')