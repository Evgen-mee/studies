# datetime
# что бы работать с датой и временем сразу используем datetime
# нужно указать год, месяц, день, часы, минуты, секунды и микросекунды.
# год, месяц и день являются ОБЯЗАТЕЛЬНЫМИ
# часы, минуты, секунды и микросекунды необязательным


# from datetime import datetime
# my_datetime = datetime(1992, 10, 6, 9, 40, 23, 51204)    # создаем полную дату-время
# only_date = datetime(2021, 12, 31)         # создаем дату-время с нулевой временной информацией
# print(my_datetime) == 1992-10-06 09:40:23.051204
# print(only_date) == 2021-12-31 00:00:00
# print(type(my_datetime)) == <class 'datetime.datetime'>


# Методы datetime
# year — год
# month — месяц
# day — день
# hour — час
# minute — минуты
# second — секунды
# microsecond — микросекунды


# Получить date и time из datetime:
# my_datetime = datetime(2022, 10, 7, 14, 15, 45)
# my_date = my_datetime.date()                     # получаем только дату (тип date)
# my_time = my_datetime.time()                     # получаем только время (тип time)