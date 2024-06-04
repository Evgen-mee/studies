# Функция monthcalendar()
# monthcalendar(year, month) возвращает матрицу, представляющую календарь на месяц. Каждая строка матрицы представляет неделю.
# дни, которые не входят в указанный месяц, представлены нулями. При этом каждая неделя начинается с понедельника,
# если не установлено другое функцией setfirstweekday()

# import calendar
# print(*calendar.monthcalendar(2021, 9), sep='\n')
# выводит:
# [0, 0, 1, 2, 3, 4, 5]
# [6, 7, 8, 9, 10, 11, 12]
# [13, 14, 15, 16, 17, 18, 19]
# [20, 21, 22, 23, 24, 25, 26]
# [27, 28, 29, 30, 0, 0, 0]