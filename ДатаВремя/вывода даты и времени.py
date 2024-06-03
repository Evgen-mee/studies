# strftime()
# форматированние вывода даты и времени
#
# from datetime import date, time
# my_date = date(2021, 8, 10)
# my_time = time(7, 18, 34)
# print(my_date)                             # вывод в ISO формате 2021-08-10
# print(my_time)                             # вывод в ISO формате 07:18:34
#
# print(my_date.strftime('%d/%m/%y'))        # форматированный вывод даты   10/08/21
# print(my_date.strftime('%A %d, %B %Y'))    # форматированный вывод даты     Tuesday 10, August 2021
# print(my_time.strftime('%H.%M.%S'))        # форматированный вывод времени  07.18.34
#
# %a - Сокращенное название дня недели	Sun, Mon, …, Sat (en_US) Пн, Вт, ..., Вс (ru_RU)
#
# %A - Полное название дня недели	Sunday, Monday, …, Saturday (en_US) понедельник, ..., воскресенье (ru_RU)
#
# %w- Номер дня недели [0, …, 6]	0, 1, …, 6 (0=воскресенье, 6=суббота)
#
# %d- День месяца [01, …, 31]	01, 02, …, 31
#
# %b- Сокращенное название месяца	Jan, Feb, …, Dec (en_US); янв, ..., дек (ru_RU)
#
# %B - Полное название месяца	January, February, …, December (en_US); Январь, ..., Декабрь (ru_RU)
#
# %m- Номер месяца [01, …,12]	01, 02, …, 12
#
# %y - Год без века [00, …, 99]	00, 01, …, 99
#
# %Y- Год с веком	0001, 0002, …, 2013, 2014, …, 9999
# В Linux год выводится без ведущих нулей: 1, 2, …, 2013, 2014, …, 9999
#
# %H - Час (24-часовой формат) [00, …, 23]	00, 01, …, 23
#
# %I - Час (12-часовой формат) [01, …, 12]	01, 02, …, 12
#
# %p - До полудня или после (при 12-часовом формате)	AM, PM (en_US)
#
# %M - Число минут [00, …, 59]	00, 01, …, 59
#
# %S - Число секунд [00, …, 59]	00, 01, …, 59
#
# %f - Число микросекунд	000000, 000001, …, 999999
#
# %z - Разница с UTC в формате ±HHMM[SS[.ffffff]]	+0000, -0400, +1030, +063415,
#
# %Z - Временная зона	UTC, EST, CST
#
# %j - День года [001,366]	001, 002, …, 366
#
# %U- Номер недели в году (неделя начинается с воскр.).
# Неделя, предшествующая первому воскресенью, является нулевой. [00,01, 53]
#
# %W - Номер недели в году (неделя начинается с пон.)
# Неделя, предшествующая первому понедельнику, является нулевой. [00, …, 53] 00, 01, …, 53
#
# %c - Дата и время	Tue Aug 16 21:30:00 1988 (en_US); 03.01.2019 23:18:32 (ru_RU)
#
# %x- Дата	08/16/88 (None); 08/16/1988 (en_US); 03.01.2019 (ru_RU)
#
# %X	Время	21:30:00

# given_date = date(2021, 7, 17)
# print(given_date.strftime('%A %d %B %Y'))
# print(given_date.strftime('%Y/%m/%d'))
# print(given_date.strftime('%d.%m.%Y (%A, %B)'))
# print(given_date.strftime('Day of year: %j, week number: %U'))
# выводит:
# Saturday 17 July 2021
# 2021/07/17
# 17.07.2021 (Saturday, July)
# Day of year: 198, week number: 28
#
# given_time = time(14, 4, 29)
# print(given_time.strftime('Hours: %H, minutes: %M, seconds: %S.'))
# print(given_time.strftime('%H:%M:%S'))
# print(given_time.strftime('%I:%M:%S %p'))
# выыодит:
# Hours: 14, minutes: 04, seconds: 29.
# 14:04:29
# 02:04:29 PM

# Использование локализации locale()
# чтобы использовать конкретную локализацию  нужно использовать модуль locale
#
# устанавливает русскую локализацию:
# from datetime import date
# import locale
# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8') для lunix
# locale.setlocale(locale.LC_ALL, 'Russian_Russia') для Windows
# my_date = date(2021, 8, 10)
# print(my_date.strftime("%A %d, %B %Y"))    # форматированный вывод даты в русской локализации
# выводит: вторник 10, Август 2021
#
# Для установки английской локализации используется код:
# import locale
# locale.setlocale(locale.LC_ALL, 'en_EN.UTF-8')