# Атрибут month_name
# calendar.month_name возвращает итерируемый объект, содержащий названия месяцев года.
# month_name соответствует обычному соглашению, что январь – это месяц номер 1, поэтому список имеет длину в 13
# элементов, первый из которых – пустая строка.

# import calendar, locale
# english_names = list(calendar.month_name)
# print(english_names)
# выводит:
# ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
# russian_names = list(calendar.month_name)
# print(russian_names)
# выводит:
# ['', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']