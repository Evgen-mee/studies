# import calendar
# Атрибут calendar.day_name
# возвращает итерируемый объект, содержащий названия дней недели на английском языке.
#
# for name in calendar.day_name:
#     print(name)
# выводит:
# Monday
# Tuesday
# Wednesday
# Thursday
# Friday
# Saturday
# Sunday

# Для локализации на русский язык мы используем код:
# import calendar, locale
# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
# for name in calendar.day_name:
#     print(name)
# выводит:
# понедельник
# вторник
# среда
# четверг
# пятница
# суббота
# воскресенье
# а русском языке названия дней недели выводятся с маленькой буквы.
# Для того чтобы сделать первую букву заглавной, можно использовать строковый метод title()


# Для преобразования итерируемого объекта в список мы используем следующий код:
# import calendar
# names = list(calendar.day_name)
# print(names)
# который выводит:
# ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']