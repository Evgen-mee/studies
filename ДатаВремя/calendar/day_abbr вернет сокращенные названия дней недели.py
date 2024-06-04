#day_abbr сокращенные названия дней недели
# alendar.day_abbr возвращает итерируемый объект, содержащий сокращенные названия дней недели.

# import calendar, locale
# for name in calendar.day_abbr:
#     print(name)
# выводит:
# Mon
# Tue
# Wed
# Thu
# Fri
# Sat
# Sun


# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
# for name in calendar.day_abbr:
#     print(name)
# выводит:
# Пн
# Вт
# Ср
# Чт
# Пт
# Сб
# Вс