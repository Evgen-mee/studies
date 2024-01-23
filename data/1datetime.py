# Модуль datetime включает в себя несколько разных типов данных
# date - представляет собой информацию о дате, исключая данные о времени, на основе Григорианского календаря
# time - представляет собой информацию о времени, полностью исключая сведения о дате
# datetime - содержит информацию о времени и дате, основываясь на данных из Григорианского календаря
# timedelta - описывает определенный период во времени, который находится между двумя различными моментами
# tzinfo - представляет различные сведения о часовом поясе
# timezone - описывает время, руководствуясь стандартом UTC


# datetime
# что бы работать с датой и временем сразу используем datetime
# нужно указать год, месяц, день, часы, минуты, секунды и микросекунды.
# год, месяц и день являются ОБЯЗАТЕЛЬНЫМИ
# часы, минуты, секунды и микросекунды необязательным
#
# from datetime import datetime
# my_datetime = datetime(1992, 10, 6, 9, 40, 23, 51204)    # создаем полную дату-время
# only_date = datetime(2021, 12, 31)         # создаем дату-время с нулевой временной информацией
# print(my_datetime) == 1992-10-06 09:40:23.051204
# print(only_date) == 2021-12-31 00:00:00
# print(type(my_datetime)) == <class 'datetime.datetime'>
#
# Методы datetime
# year — год
# month — месяц
# day — день
# hour — час
# minute — минуты
# second — секунды
# microsecond — микросекунды
#
# combine()
# Новый обьект datetime можно сформировать из date и time
#
# from datetime import date, time, datetime
# my_date = date(1992, 10, 6)
# my_time = time(10, 45, 17)
# my_datetime = datetime.combine(my_date, my_time)
# print(my_datetime) == 1992-10-06 10:45:17
#
#
#
# Получить date и time из datetime:
# my_datetime = datetime(2022, 10, 7, 14, 15, 45)
# my_date = my_datetime.date()                     # получаем только дату (тип date)
# my_time = my_datetime.time()                     # получаем только время (тип time)
#
#
# Методы now(), utcnow()
# получить текущее время на момент исполнения программы
# datetime_now = datetime.now()
# datetime_utcnow = datetime.utcnow()
# print(datetime_now)           # текущее локальное время (московское) на момент запуска программы
# print(datetime_utcnow)        # текущее UTC время на момент запуска программы
#
#
# Метод timestamp()
# преобразовать объект типа datetime в количество секунд c 1970 года
# from datetime import datetime
# my_datetime = datetime(2021, 10, 13, 8, 10, 23)
# print(my_datetime.timestamp()) == 1634101823.0
#
#
# Метод fromtimestamp()
# позволяет преобразовать количество секунд, прошедших с момента начала эпохи, в объект типа datetime
# my_datetime = datetime.fromtimestamp(1634101823.0)
# print(my_datetime) == 2021-10-13 08:10:23
#
#
# преобразовать дату-время в строку нужного формата, следует воспользоваться методом strftime()
# my_datetime = datetime(2021, 8, 10, 18, 20, 34)
# print(my_datetime) == 2021-08-10 18:20:34            # вывод в ISO формате
# print(my_datetime.strftime('%d.%m.%y --- %H::%M::%S')) == 10.08.21 --- 18::20::34
# print(my_datetime.strftime('%d/%m/%y')) == 10/08/21
# print(my_datetime.strftime('%A %d, %B %Y')) == Tuesday 10, August 2021
# print(my_datetime.strftime('%H:%M:%S')) == 18:20:34
#
# метод strptime() преобразовать строку в дату ОБЕ СТРОКИ ДОЛЖНЫ БЫТЬ ИНДЕНТИЧНЫМИ КРОМЕ ВРЕМЯ И ФОРМАТА
# преобразует строку (первый аргумент) в объект datetime
# второй аргумент согласно переданному формату
# первый аргумент должен соответствовать формату второго аргумента.
# Если он не соответствует, то возникает исключение
# from datetime import datetime
# datetime_str = input('Введите дату/время в формате ДД.ММ.ГГГГ ЧЧ:ММ:СС')
# my_datetime = datetime.strptime(datetime_str, '%d.%m.%Y %H:%M:%S')
# print(my_datetime)
#
# При создании объекта datetime из строки с помощью метода strptime()
# необязательно, чтобы строка содержала год, месяц и день,
# в отличие от ручного создания объекта datetime
# from datetime import datetime
# d = datetime.strptime('9:00', '%H:%M')
# print(d) == 1900-01-01 09:00:00
#
#
# метод replace()
# Для создания новой даты-времени на основании уже существующей
# возвращает новый объект с переданными  значениями .
# from datetime import datetime
# datetime1 = datetime(1992, 10, 6, 10, 12, 45)
# datetime2 = datetime1.replace(year=1995, month=12)
# datetime3 = datetime1.replace(day=17, hour=14, minute=37)
# print(datetime1) == 1992-10-06 10:12:45
# print(datetime2) == 1995-12-06 10:12:45
# print(datetime3) == 1992-10-17 14:37:45
#
#
# locale. Приведенный ниже код устанавливает русскую локализацию:
# from datetime import datetime
# import locale
# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
# my_datetime = datetime(2021, 8, 10, 12, 34, 15)
# print(my_datetime.strftime('%A %d, %B %Y, %H:%M:%S')) == вторник 10, Август 2021, 12:34:15
#
# Для установки английской локализации
# import locale
# locale.setlocale(locale.LC_ALL, 'en_EN.UTF-8')
