# Атрибут month_abbr вернет сокращенные названия месяцев
# возвращает итерируемый объект, содержащий сокращенные названия месяцев года.

# import calendar, locale
# english_names = list(calendar.month_abbr)
# print(english_names)
# выводит:
# ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
# russian_names = list(calendar.month_abbr)
# print(russian_names)
# выводит:
# ['', 'янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']