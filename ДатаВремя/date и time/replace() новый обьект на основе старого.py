# replace() новый обьект на основе старого
# Для создания новой даты на основании уже существующей можно использовать метод replace().
# Он возвращает новую дату с переданными измененными значениями свойств year, month, day

# date1 = date(1992, 10, 6)
# date2 = date1.replace(year=1995)            # заменяем год
# date3 = date1.replace(month=12, day=17)     # заменяем месяц и число
# print(date1) == 1992-10-06
# print(date2) == 1995-10-06
# print(date3) == 1992-12-17

# time1 = time(17, 10, 6)
# time2 = time1.replace(hour=21)                  # заменяем час
# time3 = time1.replace(minute=48, second=59)     # заменяем минуты и секунды
# print(time1) == 17:10:06
# print(time2) == 21:10:06
# print(time3) == 17:48:59
